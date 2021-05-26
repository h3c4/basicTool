#!/usr/bin/python3
#coding:utf-8

import os
import sys
import time
import signal
import pyqrcode


def handler(signum, frame):
    print("Exit..")
    time.sleep(1) 
    sys.exit(0)
signal.signal(signal.SIGINT, handler)

def error():
    if len(sys.argv) != 2:
        print("[!] Options\n") 
        print("\t[1] Create directory")
        print("\n\t[2] Create QR code")
        print("\n\t[3] Make to host discovery\n")

        print("\n[*]Uso: python3 " + sys.argv[0] + " option\n")
        sys.exit(1)  

def createDirectory():
    try :
        path=input("Write the name of directory: ")
        os.mkdir(path)
        time.sleep(1)
        print("\n[!] Directory created in the current path whit the name:" + path +"\n")
    except OSError:
        print("\n[x] Sorry, the directory alredy exist in the current path")

def createQrcode():
    try :
        QRstring =input("Insert the url of the page: ")
        file =input("Insert the name of qr: ")
        img=file+'.png'
        genereate=pyqrcode.create(QRstring)       
        save=genereate.png(img,scale=8)
        save
        print ("\n[!]Creating QR code for: ",QRstring)
        time.sleep(2)
        print("\n\t[*]Succes, QR code created")
        time.sleep(1)
        print("\n[!]Show in ",img)
    except OSError:
        print("[x] Sorry couldn't to create the qr ")    

def hostDiscovery():
    ip = input("Insert the name host or ip : ")
    print(f"[!] Sending trace ICMP to {ip}")
    time.sleep(0.5)
    print (os.system(f"ping {ip}"))

if __name__ == '__main__':
   
    try:
        
        if int(sys.argv[1]) == 1:
            createDirectory()
        elif int(sys.argv[1]) == 2:
            createQrcode()
        elif int(sys.argv[1]) == 3:        
            hostDiscovery()
    except:
        error()        

