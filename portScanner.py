from socket import *
from sys import argv
from threading import *
import optparse

def portScan(targethost, targetport):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((targethost,targetport))
        print(f"[+] {targetport} => Open")

    except:
        print(f"[-] {targetport} => Close")
    finally:
        sock.close()

def hostScan(targethost, targetports):
    try:
        targetIp = gethostbyname(targethost)
        print(f"[+] Ip Adress: {targetIp}")
        try:
            targetName = gethostbyaddr(targetIp)
            print(f"[+] Makina adı: {targetName[0]}")
            
        except:
            print("makina adı bulunamadı")
    except:
        print(f"Host bulunamadı: {targethost}")

    setdefaulttimeout(1)
    for targetport in targetports:
        try:
            t = Thread(target=portScan,args=(targethost, int(targetport)))
            t.start()
        except:
            print("hatalı işlem")

def main():
    parser = optparse.OptionParser("Program Use: -H <Host Address> -p <Port Address>")
    parser.add_option("-H", dest="targethost",type="string", help="hedef ana makina")
    parser.add_option("-p", dest="targetport",type="string",help= "(,) veya (,) olmadan port belirtin")
    (options,argv)= parser.parse_args()
    targethost = options.targethost
    targetports = str(options.targetport).split(",")
    if (targethost== None) or (targetports[0] == None):
        print(parser.usage)
        exit(0)
    hostScan(targethost,targetports)
     
if __name__ == "__main__":
    main()
