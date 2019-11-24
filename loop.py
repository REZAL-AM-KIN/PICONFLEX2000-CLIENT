print("Demarrage 'loop.py'")
while True: #Seconde boucle infinie permettant d'utiliser la commande "break" pour arreter la transaction
    if setting.rezalOn and setting.rezalMode:
        REZAL_synchQUERRYToSQL() #Synchronisation des requêtes SQL de la box avec le serveur BDD
    RFID_waitRetireCarte() #Attente d'absence de cartes
    MENU_menuPrincipal() #Attente d'une carte et possibilité de naviguer dans les menus
    UID,argent,codeCarte,hashUID,hashArgent=RFID_readCarte() #Multi lecture des données de la carte
    DATA_setVariable("rezalOn",bool(REZAL_pingServeur())) #Ping du serveur pour s'assurer que la connection est toujours présente
    if setting.rezalOn: #Bloc de traitement des données si la box est en ligne avec le serveur
        if not(setting.rezalMode): #Le rezal est revenu sur une box en mode hors ligne
            hint("REZAL REVENU",3) #Affichage du problème
            hint("TOUCHE POUR CONTINUER",4)
            _touche=CLAVIER_getRFID()
            if _touche==0: #La carte a été retirée
                break
            else:
                hint("",3); hint("",4) #On efface le message
        else: #rezalMode est à True, donc on fait la synchronisation
            hint("UID: "+str(UID),2) #Affichage UID de la carte
            try: #Essais de récupération de l'argent de la carte de la BDD:
                argentSQL=SQL_SELECT(QUERRY_getArgent(UID))[0][0]
            except: #Echec (la carte (UID) est absente de la BDD):
                hint("SYNCH CARTE BDD",4) #Affichage utilisateur de l'initialisation de la carte dans la BDD
                argentSQL=0 #Montant nul pour la carte
                SQL_EXECUTE(QUERRY_addCarte(UID)) #Création de la carte dans la BDD
            if argent!=argentSQL: #Cas où les montants RFID et BDD sont différents:
                hint("SYNCH RFID ARGENT",4) #Affichage synchronisation
                argent=argentSQL #Synchronisation des variables
                RFID_setArgent(argent) #Synchronisaton RFID
            if codeCarte!=int(CRYPT_hashage(config.codeGuinche)): #Le codeGuinche est périmé:
                hint("SYNCH RFID H CODE",4) #Affichage synchronisation
                RFID_write(config.blockHashCodeGuinche,str(int(CRYPT_hashage(config.codeGuinche)))) #Ecriture RFID du Hash du codeGuinche sur la carte
            if hashUID!=int(CRYPT_hashage(UID)): #Le hash de l'UID ne correspond pas au hash stocké sur la carte
                hint("SYNCH RFID H UID",4) #Affichage synchronisation
                RFID_write(config.blockHashUID,str(int(CRYPT_hashage(UID)))) #Ecriture du hash de l'UID sur la carte
            if hashArgent!=int(CRYPT_hashage(argent)):
                hint("SYNCH RFID ARGENT",4) #Affichage synchronisation
                RFID_setArgent(argent) #Ecriture de l'argent sur la carte (Réecrit le hash de l'argent)
            if argent<0: #Si le montant de la carte dans la BDD est inérieur à 0 (Une triche pendant un mode hors ligne a été réalisé ou une désynchronisation a été faite)
                hint("APPELLER REZAL",3) #Le rezal doit regarder l'historique de la carte et vérifier que toute les caisses sont synchro
                hint("DESYNCH BDD",4) #Affichage problème (Si ce message s'affiche pendant un gala c'est pas bon: soit la personne est un tricheur, soit une box fonctionne en mode hors ligne)
                DATA_add('/home/pi/PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addLog(setting.numeroBox,setting.nomBox,"DESYNCH BDD",str(UID))) #Ajout du message dans les logs
                break #Arret de la transaction
    if not(setting.rezalOn) or not(setting.rezalMode): #Bloc de traitement des données de la carte en mode hors ligne ou sans réseau
        if setting.rezalMode: #Si la box ne ping plus mais est en rezalMode On
            hint("PERTE DU REZAL",4) #Affichage du problème
            REZAL_restart() #Redémarrage du système
        #Sinon la box est en rezalMode Off, qu'elle pingue ou non
        if codeCarte!=int(CRYPT_hashage(config.codeGuinche)): #Le codeGuinche est périmé:
            hint("DESYNCH RFID H CODE",2) #Affichage désynchronisation
            if not(setting.nomBox[0]=="C"): #Si la box n'est pas une caisse:
                break #Arret de la transaction
            hint("ENTRER POUR RESET",3) #Instruction pour l'utilisateur
            if not(CLAVIER_getRFID()==10): #Une autre touche que ENTER est saisie:
                break #Arret de la transaction
            hint("SYNCH RFID H CODE",4) #Affichage synchronisation
            RFID_write(config.blockHashCodeGuinche,str(int(CRYPT_hashage(config.codeGuinche)))) #Ecriture RFID du Hash du codeGuinche sur la carte
            DATA_add('/home/pi/PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addCarte(UID)) #Ajout de la carte dans la BDD pour une future synchronisation
            hint("SYNCH RFID H UID",4) #Affichage synchronisation
            RFID_write(config.blockHashUID,str(int(CRYPT_hashage(RFID_getUID()))))
            hint("SYNCH RFID ARGENT",4) #Affichage synchronisation
            RFID_setArgent(0) #Mise à zero de l'argent RFID de la carte
            argent=0 #Synchronisation de la variable argent
            hashUID=int(CRYPT_hashage(UID)) #Recalcul de la variable hash UID
            hashArgent=int(CRYPT_hashage(argent)) #Recalcul de la variable hash argent
            hint("",3)
            hint("",4)
        if hashUID!=int(CRYPT_hashage(UID)): #Vérification du hash UID
            hint("DESYNCH H UID",2) #Affichage problème
            hint("APPELLER REZAL",3)
            break #Arret transaction
        if hashArgent!=int(CRYPT_hashage(argent)): #Vérification du hash argent
            hint("DESYNCH H ARGENT",2) #Affichage problème
            hint("APPELLER REZAL",3)
            break #Arret transaction
    hint("Credit: "+STRING_montant(argent),3)
    if setting.nomBox[0]=="C": #Si la box est une caisse
        montant=MENU_getMontant(argent) #Demande du montant à ajouter sur la carte
        produit="RechargeMontant" #Le produit est nommé RechargeMontant(utiliser pour différentier les requêtes SQL)
        nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
        reference=-1 #Pas de référence
    elif setting.nomBox[0]=="K": #Si la box est une Kve (Mode permettant de retirer un montant)
        montant=-MENU_getMontant(argent)#Demande du montant à retirer sur la carte
        produit="VenteMontant"#Le produit est nommé RechargeMontant(utiliser pour différentier les requêtes SQL)
        nombre=1 #Une seule recharge (permet de standardiser les transactions mais est inutile ici)
        reference=-1 #Pas de référence
    else:
        reference,nombre,produit,montant=MENU_getCommande(argent) #Paramètres de la commande
    if montant==0: #Si la carte a été retirée
        break #Arret de la transaction
    newMontant=argent+montant #Calcul du nouveau montant de la carte
    if newMontant<0: #Si le nouveau montant est négatif:
        hint("CREDIT INSIFFISANT",2)
        hint("NE PAS SERVIR",3)
        break #Arret de la transaction
    DATA_add('/home/pi/PICONFLEX2000-LOGS/LOG_QUERRY.txt',QUERRY_addArgent(UID,montant)+QUERRY_addTransaction(produit,nombre,setting.numeroBox,UID,montant,reference)) #Ajout des requetes pour la BDD
    hint("NE PAS RETIRER CARTE",4) #Avertissement sur lequel il faut lourdement insister en mode hors ligne!
    RFID_setArgent(newMontant) #Ecriture du nouveau montant
