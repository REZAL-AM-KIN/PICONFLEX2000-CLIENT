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
    hint("Lecture Carte",4)
    UID,argent,codeCarte,hashUID,hashArgent=RFID_readCarte()
    hint("",4)
    hint("Credit: "+STRING_montant(argent),2)
    hint("UID: "+str(UID),3)
    if codeCarte!=int(CRYPT_hashage(config.codeGuinche)):
        hint("Carte perimee",3)
        hint(str(codeCarte)+"/"+str(int(CRYPT_hashage(config.codeGuinche))),4)
        if (setting.nomBox[0]=="C"):
            hint("ENTRER POUR RESET",4)
            if CLAVIER_getRFID()==10:
                RFID_resetCarte()
                hint("Synchronisation",4)
                DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addCarte(UID))
                if setting.rezalOn:
                    REZAL_synchQUERRYToSQL()
            else:
                break
        else:
            break
    if hashUID!=int(CRYPT_hashage(UID)):
        hint("Triche UID",2)
        DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"TRICHE UID",str(UID)+" - "+STRING_montant(argent)))
        break
    if hashArgent!=int(CRYPT_hashage(argent)):
        hint("Triche MONTANT",2)
        DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"Triche montant",str(UID)+" - "+STRING_montant(argent)))
        break
    if setting.rezalOn:
        try:
            argentSQL=SQL_SELECT(QUERRY_getArgent(UID))[0][0]
        except:
            argentSQL=0
            SQL_EXECUTE(QUERRY_addCarte(UID))
        if argent!=argentSQL:
            hint("Desynch BDD",2)
            hint(STRING_montant(argent)+" -> "+STRING_montant(argentSQL),3)
            hint("ENTRER POUR SYNCH",4)
            CLAVIER_get()
            RFID_setArgent(argentSQL)
            argent=argentSQL
            break
        if argentSQL<0:
            hint("Triche BDD",2)
            DATA_add('/home/pi/PICONFLEX2000/log/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"Triche BDD",str(UID)+" - "+STRING_montant(argent)))
            break
    if argent>config.maxMontant:
        hint("Triche MONTANT_MAX",2)
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