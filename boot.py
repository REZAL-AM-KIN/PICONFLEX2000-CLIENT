print("Demarrage 'boot.py'")
exec(open('/home/pi/PICONFLEX2000/client/launch.py').read())
try:
    exec(open('/home/pi/PICONFLEX2000/client/init.py').read())
except:
    exec(open('/home/pi/PICONFLEX2000/client/error.py').read())
while True:
    try:
        exec(open('/home/pi/PICONFLEX2000/client/loop.py').read())
    except:
        exec(open('/home/pi/PICONFLEX2000/client/error.py').read())