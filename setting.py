print("Demarrage 'setting.py'")
class setting: #Définition des variables reliée à l'objet setting définissant les paramètres de la box. Ces paramètres sont sauvegardés et résistent au reboot
    nomBox='' 
#Nom de la box (Données par la BDD au démarrage), il définie le rôle de la box selon la première lettre (ATTENTION: Première lettre toujours en majuscule)
    numeroBox=0 
#Numéro de la box, permet d'identifié de façon unique les boxs (clé primaire) pour la BDD
    version=0
#Version du système, permet de savoir quand une MAJ est a faire
    rezalOn=False
#Paramètre indiquand au système si la box a ping le serveur
    rezalMode=False
#Paramètre indiquand si la box est en mode hors ligne ou pas
    rezalNet=False
#Paramètre indiquant si la box à ping un réseau internet
    IP="0.0.0.0"
#IP de la box
    MAC="00:00:00:00:00"
#Adresse MAC de la box
    produits={}
#Dictionnaire des produits de la box
    connection={}
#Définition du dictionnaire de connection à la BDD
    connection["user"]='pi'
#Nom d'utilisateur
    connection["password"]='pi'
#Mot de passe du nom d'utilisateur
    connection["database"]='Guinche'
#Nom de la BDD
    connection["host"]="192.168.139.139"
#IP du serveur BDD
    serveurNet="8.8.8.8"
#Adresse IP DNS google qui répond au ping