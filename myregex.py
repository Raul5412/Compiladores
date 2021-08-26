#Víctor Antonio Godínez Rodríguez A01339529
#Raúl González Cardona A01654995

import re

def email(str):
    match = re.search(r'(\w+)\@(\w+)\.(\w+)', str)
    if match:
        print("Sí funcionó")
        return True
    else:
        print("No funcionó")
        return False

def phone_number(str):
    match = re.search(r'\+1\(52\)55[0-9]{8}$|55[0-9]{8}$|\+1 \(52\) 55 [0-9]{4} [0-9]{4}$', str)
    if match:
        print("Sí funcionó")
        return True
    else:
        print("No funcionó")
        return False
    
def hexadecimal(str):
    match = re.match(r'0x[0-9a-fA-F]{8}', str)
    if match: 
        print("Sí funcionó")
        return True
    else:
        print("No funcionó")
        return False