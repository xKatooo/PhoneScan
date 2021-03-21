from colorama import Fore, init
import requests
from bs4 import BeautifulSoup
init(autoreset=True)
def dorkeo(p, n):
    print("")
    print(Fore.YELLOW + "Dorkeando {}{}...".format(p, n))
    print(Fore.RED + """
Por razones de que google es capaz de rastrear el trafico de una persona y bloquearla si esta
se mueve muy rapido y tambien porque no he encontrado una buena herramienta de proxys te dare 
los dorks a buscar a ti y tu los buscaras, esto tambien abre la posibilidad de que tu puedas 
investigar conexiones por tu cuenta y ser mas preciso
""")
    print(Fore.LIGHTYELLOW_EX + "Redes Sociales:")
    print(Fore.LIGHTGREEN_EX+"Whatsapp "+Fore.RED+"(enlace directo)"+Fore.LIGHTGREEN_EX+": " + Fore.LIGHTMAGENTA_EX+"https://api.whatsapp.com/send?phone="+p[1:3]+n)
    print(Fore.CYAN+"Facebook: "+Fore.LIGHTMAGENTA_EX+ "https://www.google.com/search?q=site%3Afacebook.com+intext%3A%22"+p+n+"%22+OR+intext%3A%22%2B"+p[1:10]+n+"%22+OR+intext%3A%22"+n+"%22")
    print(Fore.CYAN+"Instagram: "+Fore.LIGHTMAGENTA_EX+ "https://www.google.com/search?q=site%3Ainstagram.com+intext%3A%22"+p+n+"%22+OR+intext%3A%22%2B"+p[1:10]+n+"%22+OR+intext%3A%22"+n+"%22")
    print(Fore.CYAN+"Twitter: "+Fore.LIGHTMAGENTA_EX+ "https://www.google.com/search?q=site%3Atwitter.com+intext%3A%22"+p+n+"%22+OR+intext%3A%22%2B"+p[1:10]+n+"%22+OR+intext%3A%22"+n+"%22")
    print(Fore.CYAN+"Linkedin: "+Fore.LIGHTMAGENTA_EX+ "https://www.google.com/search?q=site%3Alinkedin.com+intext%3A%22"+p+n+"%22+OR+intext%3A%22%2B"+p[1:10]+n+"%22+OR+intext%3A%22"+n+"%22")
    print(Fore.CYAN+"vk: "+Fore.LIGHTMAGENTA_EX+ "https://www.google.com/search?q=site%3Avk.com+intext%3A%22"+p+n+"%22+OR+intext%3A%22%2B"+p[1:10]+n+"%22+OR+intext%3A%22"+n+"%22"+"""
    
    """)
    print(Fore.LIGHTYELLOW_EX + "")