print("Demarrage 'init.py'")
MENU_clear() #Nettoie l'écran
DATA_setVariable("rezalOn",bool(REZAL_pingServeur())) #Ping le serveur et enregistre le résultat
DATA_setVariable("rezalNet",bool(REZAL_pingInternet())) #Ping le DNS désiré et enrigistre le résultat
DATA_setVariable("version",REZAL_getVersion()) #Calcul la version du script et enregistre le résultat
DATA_setVariable("IP",REZAL_getIP()) #Récupère son addresse IP sur le réseau et enregistre le résultat
DATA_setVariable("MAC",REZAL_getMAC()) #Récupère l'addresse MAC de la carte réseau Ethernet et enregistre le résultat
hint(setting.IP,1) #Affichage de L'IP de la box à la première ligne
hint(setting.MAC,2) #Affichage de l'addresse MAC de la box à la deuxième ligne
if setting.numeroBox==0: #Si le numero de la box est 0 (comme après un git clone)
    MENU_setNumeroBox() #Demande d'inscription d'un numéro de box
    if setting.rezalOn: #Si une machine a répondu au ping de l'IP serveur
        MENU_setLoginBDD() #Demande du Login BDD
        MENU_setMDPBDD() #Demande du MDP BDD
    else:
        MENU_setNomBox() #Demande d'un nom de box
        MENU_setIPServeur() #Demande de l'IP du serveur
if setting.rezalOn: #Si la box à ping l'addresse IP déclarée du serveur:
    SQL_EXECUTE(QUERRY_setOnline(setting.IP,1)) #Se déclare Online auprès de la BDD
    SQL_EXECUTE(QUERRY_setMAC(setting.MAC,setting.numeroBox)) #Donne sa MAC à la BDD
    SQL_EXECUTE(QUERRY_setVersion(setting.version,setting.numeroBox)) #Donne sa version à la BDD
    SQL_EXECUTE(QUERRY_setIP(setting.IP,setting.numeroBox)) #Donne son IP à la BDD
    #Si il y a un bug dans la ligne suivante, la box n'est pas ajoutée dans la BDD
    #Si il y a un bug dans la deuxième ligne, la box n'a pas de comptoir associée
    #Si il y a un bug dans la troisième ligne, la comptoir n'as pas de produits associés
    DATA_setVariable("rezalMode",bool(SQL_SELECT(QUERRY_getMode(setting.numeroBox))[0][0])) #Récupère le mode REZAL de la BDD (Variable empêchant à la box de communiquer avec le serveur)
    DATA_setVariable("nomBox",SQL_SELECT(QUERRY_getNomBox(setting.numeroBox))[0][0]) #Récupère le nom du comptoir dans la BDD 
    DATA_setVariable("produits",SQL_getProduits(setting.numeroBox)) #Récupère les produits de la box
else: #Si le serveur n'a pas répondu au ping:
    MENU_getCode(config.codeOffline,"Code Offline") #Demande du code Offline pour permettre à la box d'effectuer des actions sans le serveur (Les requêtes de modification de la BDD seront sauvegardées et synchroniser à la prochaine connection)
    DATA_setVariable("rezalMode",False) #Enregistrement du passage en mode hors ligne de la box
#Vérification de la première lettre des noms de comptoir et demande du code associé (Il est possible de ne taper que le code Guinche quand un mot de passe est demandé)
if   setting.nomBox[0]=="C":
    MENU_getCode(config.codeCaisse,"Code Caisse")
elif setting.nomBox[0]=="K":
    MENU_getCode(config.codeKve,"Code Kve")
elif setting.nomBox[0]=="O":
    MENU_getCode(config.codeOenols,"Code Oenols")
elif setting.nomBox[0]=="G":
    MENU_getCode(config.codeGazole,"Code Gazole")
elif setting.nomBox[0]=="B":
    MENU_getCode(config.codeBar,"Code Bar")
elif setting.nomBox[0]=="N":
    MENU_getCode(config.codeNourriture,"Code Nourriture")
else: #La premère lettre du nom de la box de correspond pas aux attentes du script, le script se ferme
    MENU_setNomBox() #Demande d'un nom de box
    REZAL_restart() #Redemarrage système