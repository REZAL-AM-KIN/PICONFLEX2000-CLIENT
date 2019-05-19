print("Demarrage 'boot.py'")
exec(open('/home/pi/PICONFLEX2000-CLIENT/launch.py').read())
try:
    exec(open('/home/pi/PICONFLEX2000-CLIENT/init.py').read())
except:
    exec(open('/home/pi/PICONFLEX2000-CLIENT/error.py').read())
while True:
    try:
        exec(open('/home/pi/PICONFLEX2000-CLIENT/loop.py').read())
    except:
        exec(open('/home/pi/PICONFLEX2000-CLIENT/error.py').read())