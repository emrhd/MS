
import subprocess

import datetime

import time

while True:
    now = datetime.datetime.now()
    print("Current date and time : ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))



    ip_list = [['192.168.30.230', 'Fairfax'],
                   ['192.168.31.231', 'Miami'],
                   ['192.168.32.230', 'New Jersey'],
                   ['192.168.34.230', 'New York'],
                   ['192.168.35.230', 'Pompano Beach'],
                   ['192.168.36.230', 'Chantilly'],
                   ['192.168.37.230', 'Los Angeles'],
                   ['192.168.38.230', 'San Francisco'],
                   ['192.168.39.177', 'San Juan'],
                   ['192.168.40.230', 'Bethesda'],
                   ['192.168.43.231', 'Anaheim'],
                   ['192.168.44.85', 'Dominican Republic'],
                   ['192.168.45.222', 'Monterrey'],
                   ['192.168.63.1', 'Oguz Algan Home']]
    for address, location in ip_list:

        res = subprocess.call(['ping', '-c', '2', address])
        if res == 0:
            # print( location,"is Ok")
            print (" ")
        else:
            print (" ")
            print("********NO CONNECTION**********",address,location)
            print (" ")

    hour = int(now.strftime("%H"))

    if hour == 20:
        exit()
    else:
        time.sleep(600)
        print()           




#for i in {192.168.30.230,192.168.31.231,192.168.32.230,192.168.34.230,192.168.35.230,192.168.36.230,192.168.37.230,192.168.38.230,192.168.40.230,192.168.43.231,192.168.44.9,192.168.45.222,192.168.63.1}  ; do ping -c 2 $i | grep 'bytes' ; done

