#!/usr/bin/env python3

import socket,time,threading,sys,random,os,subprocess,requests
from os import getcwd

url = "https://raw.githubusercontent.com/Patonia/Patonia/main/target.txt"
directory = getcwd()
filename = directory + 'target.txt'
r = requests.get(url)

f = open(filename,'w')
f.write(r.content)

