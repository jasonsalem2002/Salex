from modules.salex_functions import check_updates, local_ip, machine_os, clear
from modules.salex_create import show_payloads_windows,show_payloads_mac,show_payloads_linux, check_payload, create_payload
from modules.salex_listen import listen

version = "1.0"

def logo():

    clear()

    print("""\n
                                        
              mmmm    mm   m      mmmmmm m    m
             #"   "   ##   #      #       #  # 
             "#mmm   #  #  #      #mmmmm   ##  
                 "#  #mm#  #      #       m""m 
             "mmm#" #    # #mmmmm #mmmmm m"  "m
                                   
                                                 Created by: Jason Salem, [!] Beta Version \n""")

def main():
    try:

        host = None
        port = None

        payload_name = None
        payload_host = None
        payload_port = None

        logo()

        check_updates(version)

        while True:
            command = input("\nSalex: ").lower()

            if command == "create":
                while True:

                    command = input("\nSalex>create_payload: ").lower()
                
                    if command == "help":
                        print(f"\n[+] show payloads   : Show Available Payloads\n[+] set payload     : Use Payload\n[+] clear           : Clear\n[+] back            : Return To The Home Menu")

                    elif command == "show payload windows":
                        print(show_payloads_windows())

                    elif command == "show payload mac":
                        print(show_payloads_mac())

                    elif command == "show payload linux":
                        print(show_payloads_linux())

                    elif command == "set payload":
                        payload = input("\n[-] Enter Payload Path: ").lower()

                        if check_payload(payload) == True:
                            print(f"\n[+] Payload => {payload}")

                            while True:
                                command = input(f"\nSalex>{payload}: ").lower()

                                if command == "help":
                                    print("""\n[+] set name        : Change Your Payload Name\n[+] set host        : Change Your Host (Ex: set host IP Manually)\n[+] set port        : Change Your Port (Ex: set port 4444)\n[+] show options    : Show Payload Options [Name, Host, Port]\n[+] create          : Build Payload\n[+] clear           : Clear\n[+] back            : Return To The Create Menu""")

                                elif command == "set name":
                                    print("\n[+] Change Your Payload Name.")
                                    command = input("\n[-] Enter Payload Name: ").lower()
                                    
                                    if command == "":
                                        print("\n[!] Please Enter A Valid Name.")

                                    else:
                                        payload_name = command
                                        print(f"\n[+] Payload Name => {payload_name}")

                                elif command == "set host":
                                    print("\n[+] Change Your Host (Ex: set host IP Manually).")
                                    command = input("\n[-] Enter Payload Host: ")

                                    if command == "":
                                        print("\n[!] Please Enter A Valid Host")

                                    else:
                                        payload_host = command
                                        print(f"\n[+] Payload Host => {payload_host}")

                                elif command == "set port":
                                    print(f"\n[+] Change Your Port (Ex: set port 4444)")

                                    try:
                                        payload_port = int(input("\n[-] Enter Payload Port: "))
                                        print(f"\n[+] Payload Port => {payload_port}")

                                    except:
                                        print("\n[!] Please Enter A Valid Port.")

                                elif command == "show options":
                                    print(f"\n[+] Payload         : {payload}\n[+] Payload Name    : {payload_name}\n[+] Payload Host    : {payload_host}\n[+] Payload Port    : {payload_port}")
                                
                                elif command == "create":
                                    if payload_name == None:
                                        print("\n[!] Please Add Payload Name.")

                                    elif payload_host == None:
                                        print("\n[!] Please Add Payload Host.")

                                    elif payload_port == None:
                                        print("\n[!] Please Add Payload Port.")
                                    
                                    else:
                                        create_payload(payload, payload_name, payload_host, payload_port)

                                elif command == "clear":
                                    logo()

                                elif command == "back":
                                    break

                                else:
                                    print("\n[!] Wrong Command")

                        elif check_payload(payload) == False:
                            print("\n[!] Payload Dosen't Exist.")

                    elif command == "clear":
                        logo()

                    elif command == "back":
                        break

                    else:
                        print("\n[!] Wrong Command.")

            elif command == "listen":
                while True:
                    command = input("\nSalex>listen: ").lower()

                    if command == "help":
                        print("\n[+] set host		: Change Your Host (Ex: set host IP Manually) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network\n[+] set port		: Change Your Port (Ex: set port 4444)\n[+] show options	: Show Listening Options [Host,Port]\n[+] run			: Start Listeneing\n[+] clear		: Clear\n[+] back		: Return To The Home Menu")

                    elif command == "set host":
                        print("\n[+] Change Your Host (Ex: set host IP Manually) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network.\n")
                        
                        host = input("[-] Enter Host: ").lower()
                        if host == "l":
                            host = local_ip()

                        elif host == "p":
                            host = "0.0.0.0"

                        print(f"\n[+] Host => {host}")

                    elif command == "set port":
                        print("\n[+] Change Your Port (Ex: set port 4444).\n")
                        try:
                            port = int(input("[-] Enter Port: "))
                            print(f"\n[+] Port => {port}")

                        except:
                            print("\n[!] Please Enter A Valid Port.")

                    elif command == "show options":
                        print(f"\n[+] Your Host: {host}\n[+] Your Port: {port}")

                    elif command == 'run':
                        if host == None:
                            print("\n[!] Please Add Host.")

                        elif port == None:
                            print("\n[!] Please Add Port.")

                        else:
                            listen(host, port)
                
                    elif command == "clear":
                        logo()

                    elif command == "back":
                        break
                
                    else:
                        print("\n[!] Wrong Command.")

            elif command == "help":
                print("""\n[+] create  : Create A New Payload\n[+] listen  : Start Listening\n[+] Salex  : View Salex information\n[+] clear   : Clear\n[+] close   : Exit""")

            elif command == "Salex":
                check_updates(version)
                print(f"\n[+] Machine Os      : {machine_os()}\n[+] Your Local Ip   : {local_ip()}\n[+] Salex Version  : {version}\n[+] Salex Link     : to update \n[+] Salex Author   : Jason Salem")

            elif command == "clear":
                logo()

            elif command == "exit":
                print("\n[+] Always keep it halal brother")
                break

            else:
                print("\n[!] Wrong Command.")
    
    except KeyboardInterrupt:
        print("\n\n[+] Always keep it halal brother")


if __name__ == "__main__":
    main()
