print("Demarrage 'error.py'")
error=traceback.format_exc()
errorList=error.replace(" ","").replace("File","").replace("line","").replace("in","").split("\n")
errortype=errorList[-2]
hint(errortype,1)
hint("",2)
hint("",3)
hint("",4)
if errortype in ["SystemExit","KeyboardInterrupt"]:
    hint("Systeme Interrompu",2)
    hint("Le shell est a vous!",3)
    hint("Prenez en soin",4)
    REZAL_exit()
DATA_add("/home/pi/PICONFLEX2000/log/LOG_ERROR.txt",error)
for i in range(len(errorList)):
    if i<=2:
        hint(errorList[i],i+2)
    else:
        CLAVIER_get()
        hint(errorList[i-2],2)
        hint(errorList[i-1],3)
        hint(errorList[i],4)
CLAVIER_get()
REZAL_restart()