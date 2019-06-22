print("Demarrage 'setup.py'")
print("Importation Drivers")
exec(open('/home/pi/PICONFLEX2000-CLIENT/HD44780.py').read()) #Execute le script de contrôl de l'écran (Si beug de la box, l'écran est mal branché ou mort)
exec(open('/home/pi/PICONFLEX2000-CLIENT/MFRC522.py').read()) #Execute le script de contrôl du lecteur RFID
print("Importation Fonctions")
for root, dirs, files in os.walk("/home/pi/PICONFLEX2000-FONCTIONS"): #Scan toute les scripts du dossier des fonctions du système
        for names in files:
            if names[-3:]==".py": #Evite l'execution du dossier .git
                print(names)
                exec(open(os.path.join(root, names)).read()) #Execute toute ces scripts pour définir les fonctions dans la console actuelle