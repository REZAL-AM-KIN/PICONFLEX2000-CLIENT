# Configuration client
## Paramétrage Raspbian
- Telecharger Raspbian sur https://www.raspberrypi.org/downloads/raspbian/  
- Ouvrir le partitionneur de disque de windows  
- Supprimer les volumes de la carte  
- Créer Une partition la plus faible possible (2 Go)  
- Televerser Raspbian sur la carte SD avec Win32DiskImager  
### Setup de Raspbian  
- Pour la premiere connection:  
> Login: "pi"  
> Mot de passe: "raspberry" (Attention au qwerty, taper "rqspberry")  
> raspi-config (Attention au qwerty, taper "rqspi)config")  
- Changer le clavier en AZERTY dans Le menu 3  
- Changer le mot de passe dans le menu 1  
- Activer le SSH-SPI-I2C-Serial-GPIO dans le menu 5  
- Activer le console Autologin dans le menu 2  
- Update le raspberry dans le menu 7  
## Paramétrage des librairies
### Installer Git-pip3-spidev-mfrc522-smbus-MySQL connector-SPI-PICONFLEX2000  
> sudo apt install git -y  
> sudo apt-get install python3-pip -y   
> sudo pip3 install spidev  
> sudo pip3 install mfrc522  
> sudo apt-get install python3-smbus -y  
> sudo apt-get install python3-mysql.connector -y  
> git clone https://github.com/lthiery/SPI-Py.git  
> cd SPI-Py  
> sudo python3 setup.py install  
> cd ../  
> sudo rm -r SPI-Py  
> git clone https://github.com/REZALKIN/PICONFLEX2000-CLIENT.git  
> git clone https://github.com/REZALKIN/PICONFLEX2000-FONCTIONS.git
## Paramétrage du script  
### Activation NumLock au démarrage (Permet d'utiliser le pavé numérique)  
> sudo nano /etc/rc.local  
- Remplacer le contenu par:
> #!/bin/sh -e  
> printf "Lancement du rc.local\n"  
> printf "Attribution adresse IP\n"  
> _IP=$(hostname -I) || true  
> if [ "$_IP" ]; then  
> printf "%s\n" "$_IP"  
> fi  
> printf "Activation Num-lock\n"  
> for tty in /dev/tty[1-1]; do  
> sudo /usr/bin/setleds -D +num < "$tty";  
> done  
> exit 0;
### Mise en route automatique  
- Accéder au fichier .profile  
> sudo nano /home/pi/.profile  
- Remplacer le contenu par:  
> sudo python3 /home/pi/PICONFLEX2000-CLIENT/boot.py  
## Branchement des composants  
Les coordonnées (X:Y) des PINs fonctionnent de la manière suivante:  
X est le numéro de la rangée  
Y est le numéro de la ligne  
La première ranger se trouve vers le centre du raspberry  
La première ligne se trouve à l'opposé des ports USB  
### Branchements du lecteur RFID MFRC522
(1:1/2:11/2:3/X:X/1:11/1:10/1:12/2:12)<=>(VCC/RST/GND/X/MISO/MOST/SCK/SDA)  
### Branchements de l'ecran LCD HD44780 2004A
(1:3/1:2/2:2/1:5)<=>(SCL/SDA/VCC/GND)  
