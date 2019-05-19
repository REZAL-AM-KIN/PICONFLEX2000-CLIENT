print("Demarrage 'init.py'")
MENU_clear()

DATA_setVariable("rezalOn",bool(REZAL_pingServeur()))
DATA_setVariable("rezalNet",bool(REZAL_pingInternet()))
DATA_setVariable("version",REZAL_getVersion())
DATA_setVariable("IP",REZAL_getIP())
DATA_setVariable("MAC",REZAL_getMAC())

if setting.rezalOn:
    SQL_EXECUTE(QUERRY_setOnline(setting.IP,1))
    SQL_EXECUTE(QUERRY_setMAC(setting.MAC,setting.numeroBox))
    SQL_EXECUTE(QUERRY_setVersion(setting.version,setting.numeroBox))
    SQL_EXECUTE(QUERRY_setIP(setting.IP,setting.numeroBox))
    
    DATA_setVariable("rezalMode",bool(SQL_SELECT(QUERRY_getMode(setting.numeroBox))[0][0]))
    DATA_setVariable("nomBox",SQL_SELECT(QUERRY_getNomBox(setting.numeroBox))[0][0])
    DATA_setVariable("produits",SQL_getProduits(setting.numeroBox))

elif setting.rezalMode:
    MENU_getCode(config.codeOffline,"Code Offline")
    DATA_setVariable("rezalMode",False)

hint(setting.IP,1)
hint(setting.MAC,2)
if   (setting.nomBox[0] in ["c","C"]):
    MENU_getCode(config.codeCaisse,"Code Caisse")
elif (setting.nomBox[0] in ["k","K"]):
    MENU_getCode(config.codeKve,"Code Kve")
elif (setting.nomBox[0] in ["o","O"]):
    MENU_getCode(config.codeOenols,"Code Oenols")
elif (setting.nomBox[0] in ["g","G"]):
    MENU_getCode(config.codeGazole,"Code Gazole")
elif (setting.nomBox[0] in ["b","B"]):
    MENU_getCode(config.codeBar,"Code Bar")
elif (setting.nomBox[0] in ["n","N"]):
    MENU_getCode(config.codeNourriture,"Code Nourriture")
else:
    REZAL_exit()