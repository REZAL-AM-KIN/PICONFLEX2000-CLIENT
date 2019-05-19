print("Demarrage 'loop.py'")
while True:
    if setting.rezalMode:
        DATA_setVariable("rezalOn",bool(REZAL_pingServeur()))
    else:
        DATA_setVariable("rezalOn",False)
    if setting.rezalOn:
        REZAL_synchQUERRYToSQL()
    RFID_waitRetireCarte()
    MENU_menuPrincipal()
    UID,argent,codeCarte,hashUID,hashArgent=RFID_readCarte()
    hint("Credit: "+STRING_montant(argent),2)
    hint("UID: "+str(UID),3)
    hint("",4)
    if setting.rezalOn:
        try:
            argentSQL=SQL_SELECT(QUERRY_getArgent(UID))[0][0]
        except:
            hint("RESET CARTE BDD",4)
            argentSQL=0
            SQL_EXECUTE(QUERRY_addCarte(UID))
        if argent!=argentSQL:
            hint("RESET ARGENT RFID",4)
            RFID_setArgent(argentSQL)
            argent=argentSQL
        if argentSQL<0:
            hint("Triche BDD",2)
            DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"Triche BDD",str(UID)+" - "+STRING_montant(argent)))
            break
        if codeCarte!=int(CRYPT_hashage(config.codeGuinche)):
            hint("RESET CODE GUINCHE",4)
            RFID_write(config.blockHashCodeGuinche,str(int(CRYPT_hashage(config.codeGuinche))))
        if hashUID!=int(CRYPT_hashage(UID)):
            hint("RESET HASH UID",4)
            RFID_write(config.blockHashUID,str(int(CRYPT_hashage(UID))))
    else:
        if codeCarte!=int(CRYPT_hashage(config.codeGuinche)):
            hint("Carte perimee",3)
            hint(str(codeCarte)+"/"+str(int(CRYPT_hashage(config.codeGuinche))),4)
            if not(setting.nomBox[0]=="C"):
                break
            hint("ENTRER POUR RESET",4)
            if not(CLAVIER_getRFID()==10):
                break
            RFID_resetCarte()
            hashUID=int(CRYPT_hashage(UID))
            hashArgent!=int(CRYPT_hashage(argent))
            DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addCarte(UID))
        if hashUID!=int(CRYPT_hashage(UID)):
            hint("PROBLEME UID",2)
            DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"TRICHE UID",str(UID)+" - "+STRING_montant(argent)))
            break
        if hashArgent!=int(CRYPT_hashage(argent)):
            hint("PROBLEME MONTANT",2)
            DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"Triche montant",str(UID)+" - "+STRING_montant(argent)))
            break
        if argent>config.maxMontant:
            hint("PRBLEME MONTANT MAX",2)
            DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"Triche MONTANT_MAX",str(UID)+" - "+STRING_montant(argent)))
            break
    if setting.nomBox[0]=="C":
        montant=MENU_getMontant(argent)
        produit="RechargeMontant"
        nombre=1
        reference=-1
    elif setting.nomBox[0]=="K":
        montant=-MENU_getMontant(argent)
        produit="VenteMontant"
        nombre=1
        reference=-1
    else:
        reference,nombre,produit,montant=MENU_getCommande(argent)
    if montant==0:
        break
    newMontant=argent+montant
    if newMontant<0:
        hint("Credit: "+STRING_montant(argent),2)
        hint("Montant: "+STRING_montant(abs(montant)),3)
        hint("Manque: "+STRING_montant(newMontant),4)
        break
    hint(STRING_montant(argent)+" -> "+STRING_montant(newMontant),3)
    hint("NE PAS RETIRER CARTE",4)
    if not(RFID_carteCheck()) and montant==newMontant:
        break
    if (UID!=RFID_getUID()):
        hint("Triche PG",2)
        hint("Changement de carte",3)
        DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"Triche PG",str(UID)+" - "+STRING_montant(montant)))
        break
    DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addArgent(UID,montant))
    DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addTransaction(produit,nombre,setting.numeroBox,UID,montant,reference))
    hint("Credit: "+STRING_montant(newMontant),2)
    RFID_setArgent(argent+montant)
    break