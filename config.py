print("Demarrage 'config.py'")
class config: #Définition des variables reliée à l'objet config définissant les paramètres du gala (guinche)
    codeGuinche         =3456       #Plus jeune Proms + numero gala
#Code du guinche (permet de différentier une carte provenant d'un guinche antérieur, a changer absolument à chaque guinche). Les hashs sont salés avec ce code
    codeAdmin           =139        #Picon KIN 217
#Code Admin permettant d'accéder au menu admin
    codeModerateur      =105132     #Yoshimitchoo KIN 217
#Code modérateur permettant d'accéder au menu modérateur
    codeHelpeur         =217        #Pas trouvé de potes a mettre
#Code helpeur permettant d'accéder au menu helpeur
    codeVP              =144        #PeerToPeer KIN 217
#Code VP permettant d'accéder au menu VP
    codeUser            =111        #Damocles KIN 217
#Code user permettant d'accéder au menu user
    codeCaisse          =53         #Pangoliiiiinnnn KIN 217
#Code permettant de débloquer la box en mode caisse
    codeKve             =151        #Mil'K KIN 217
#Code permettant de débloquer la box en mode Kve
    codeOenols          =102        #Jla'K KIN 217
#Code permettant de débloquer la box en mode Oenols
    codeGazole          =55119      #Echo Tango KIN 217
#Code permettant de débloquer la box en mode Gazole
    codeBar             =79         #BaalBerit KIN 217
#Code permettant de débloquer la box en mode Bar
    codeNourriture      =3466       #Hamsterism KIN 217
#Code permettant de débloquer la box en mode Nourriture
    codeOffline         =56150      #R'force KIN 217
#Code permettant le passage en mode hors ligne de la box
    blockArgent         =5
#Case RFID où sera mis le montant en clair
    blockHashArgent     =7
#Case RIFD où est mis le hash de l'argent (Permet d'éviter la triche montant)
    blockHashUID        =8          
#Case RFID où sera mis le hash de l'UID de la carte (Permet de vérifier que le contenue d'une carte n'a pas été copié sur une autre)
    blockHashCodeGuinche=10          
#Case RFID où sera mis le hash du code guinche (vérifie si la carte est périmée)
    minMontant          =100        
#Montant en centimes minimal à pouvoir mettre pendant une transaction
    maxTransaction      =9999       
#Montant max a pouvoir etremis sur une carte
    maxMontant          =30000      
#Montant en centime maximal à pouvoir être contenu sur une carte
    menuAdmin           =["menuAdmin","resetBDD","resetLogQuerry","resetLogSQL","resetLogError"]
    menuModerateur      =["menuModerateur","githubPull","MAJGitClone"]
    menuVP              =["menuVP","setNumeroBox","setRezalMode","setIPServeur","setNomBox","setLoginBDD","setMDPBDD"]
    menuHelpeur         =["menuHelpeur","fusionCartes","setCaisse","setKve","supprimerTransaction","resetCarte","resetCarteRFID","resetCarteBDD"]
    menuUser            =["menuUser","viewMAC","viewIP","viewIPServeur","viewPing","viewProduits"]
    menuPrincipal       =["menuPrincipal","menuUser","menuHelpeur","menuVP","menuModerateur","menuAdmin"]
#Liste des menus et leurs sous menus associés