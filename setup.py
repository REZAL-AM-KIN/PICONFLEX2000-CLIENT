print("Demarrage 'setup.py'")
print("Importation Drivers")
exec(open('/home/pi/PICONFLEX2000-CLIENT/HD44780.py').read())
exec(open('/home/pi/PICONFLEX2000-CLIENT/MFRC522.py').read())
print("Importation Fonctions")
for root, dirs, files in os.walk("/home/pi/PICONFLEX2000-FONCTIONS"):
        for names in files:
            exec(open(os.path.join(root, names)).read())