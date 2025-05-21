import os
import glob

try:
    from pathlib import Path
except:
    print("\n[!] Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def show_payloads():
    
    for p in Path( 'payloads/*/*.py' ).iterdir():
        print( p )
    else:
        return("\n[!] There Is No Payloads Right Now.")

def check_payload(payload):
    if os.path.isfile(payload):
        return True
    else:
        return False

def create_payload(payload , payload_name, payload_host, payload_port):
    # Correct the misspelled output file name so generated payloads are
    # consistently written to 'payload.txt'.
    file = open('payload.txt', 'w')
    file.write(f"{payload}")
    file.write(f"\n{payload_name}")
    file.write(f"\n{payload_host}")
    file.write(f"\n{payload_port}")
    print("Created")
