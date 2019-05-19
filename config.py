print("Demarrage 'config.py'")
class config:
    codeGuinche         =3299       #Plus jeune Proms + numero gala
    codeAdmin           =139        #Picon KIN 217
    codeModerateur      =105132     #Yoshimitchoo KIN 217
    codeHelpeur         =217        #Pas trouvé de potes a mettre
    codeVP              =144        #PeerToPeer KIN 217
    codeUser            =111        #Damocles KIN 217
    codeCaisse          =53         #Pangoliiiiinnnn KIN 217
    codeKve             =151        #Mil'K KIN 217
    codeOenols          =102        #Jla'K KIN 217
    codeGazole          =55119      #Echo Tango KIN 217
    codeBar             =79         #BaalBerit KIN 217
    codeNourriture      =3466       #Hamsterism KIN 217
    codeOffline         =56150      #R'force KIN 217
    blockArgent         =5          #Case RFID où sera mis le montant en clair
    blockHashArgent     =6          #Case RIFD où est mis le hash de l'argent (Permet d'éviter la triche montant)
    blockHashUID        =7          #Case RFID où sera mis le hash de l'UID de la carte (Permet de vérifier que le contenue d'une carte n'a pas été copié sur une autre)
    blockHashCodeGuinche=8          #Case RFID où sera mis le hash du code guinche (vérifie si la carte est périmée)
    minMontant          =100        #Montant en centimes minimal à pouvoir mettre pendant une transaction
    maxTransaction      =9999       #Montant max a pouvoir etremis sur une carte
    maxMontant          =30000      #Montant en centime maximal à pouvoir être contenu sur une carte
    menuAdmin           =["menuAdmin","resetBDD","resetLogQuerry","resetLogSQL","resetLogError"]
    menuModerateur      =["menuModerateur","githubPull","MAJGitClone"]
    menuVP              =["menuVP","setNumeroBox","setRezalMode","setIPServeur","setNomBox","setLoginBDD","setMDPBDD"]
    menuHelpeur         =["menuHelpeur","fusionCartes","setCaisse","setKve","supprimerTransaction","resetCarte","resetCarteRFID","resetCarteBDD"]
    menuUser            =["menuUser","viewMAC","viewIP","viewIPServeur","viewPing","viewProduits"]
    menuPrincipal       =["menuPrincipal","menuUser","menuHelpeur","menuVP","menuModerateur","menuAdmin"]
