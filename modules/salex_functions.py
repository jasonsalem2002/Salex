import socket
import platform
import os

try:
    import requests
except:
    
    print("\n[!] Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def check_updates(version):
    try:
        version_update_source = requests.get("https://raw.githubusercontent.com/whoami-99/whoami/main/version.txt")
        version_update_source = version_update_source.text
        
        if version_update_source != version:
            print(f"\n[!] Your Current Version Is {version} And The Available Update Version Is {version_update_source}, You Can Type 'whoami' And You Will See Our Github Link So You Can Use It To Install The Latest Version.")

        if version_update_source == version:
            print("\n[+] Whoami Is Uptodate.")
    except:
        print("\n[!] Failed To Check For Updates.")

def local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
        
    except:
        print("\n[!] Error While Getting Your Local Ip")


def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as e:
        print("Failed To Get The Machine Os")

def clear():
    """Clear the terminal screen regardless of platform."""
    if machine_os() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
