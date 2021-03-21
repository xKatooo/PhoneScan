from colorama import Fore, init
init(autoreset=True)
from proceso.motor.scrapeo import *
def enviar (n):
    n = n.replace(" ", "")
    n = n.replace("(", "")
    n = n.replace(")", "")
    n = n.replace("-", "")
    if(len(n) < 13):
        print(Fore.RED+"Le faltan numeros a este telefono.")
        return
    if(len(n)>12):
        pais = n[0:3]
        numero = n[3:20]
    else:
        numero = n[0:20]
        print(Fore.RED+"No has escrito un codigo de pais!, escoje el pais de este numero de telefono.")
        print("""
1.- MX (Mexico) 
2.- CO (Colombia)
3.- EC (Ecuador)
4.- EEUU (Estados Unidos)
5.- ARG (Argentina)
        """)
        pais_n = str(input(Fore.RED + "Escoje un numero: "))
        if(pais_n == "1"):
            pais = "+52"
        if(pais_n == "2"):
            pais = "+57"
        if(pais_n == "3"):
            pais = "+59"
        if(pais_n == "4"):
            pais = "+1"
    print (Fore.GREEN + "enviando...")
    scra(pais, numero)