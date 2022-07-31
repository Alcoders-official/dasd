import requests
from colorama import Fore, Back, Style

print(Fore.GREEN + '''
 _____                        _____                                
|  __ \                      / ____|                               
| |__) | __ _____  ___   _  | (___   ___ _ __ __ _ _ __   ___ _ __ 
|  ___/ '__/ _ \ \/ / | | |  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
| |   | | | (_) >  <| |_| |  ____) | (__| | | (_| | |_) |  __/ |   
|_|   |_|  \___/_/\_\\__, | |_____/ \___|_|  \__,_| .__/ \___|_|   
                      __/ |                       | |              
                     |___/                        |_|              
''')
print (Fore.RED + "BY PPLO @YOUSSEF_DEV")
print (Fore.BLUE + """
HTTPS = '1'
SOCKS4 = '2'
SOCKS5 = '3'
""")
prox = input(Fore.YELLOW + "Enter Type U Want(: \n")
if (prox == "1"):

    fhand = ("http://youssef.clouduz.ru/http.php")

    r = requests.get(fhand)
    c = (r.text.replace('<pre style="word-wrap: break-word; white-space: pre-wrap;" data-copier-init="true" class="">',''))
    v = (c.replace('Free proxies from free-proxy-list.net',''))
    r = (v.replace('</pre>', ''))
    s = (r.replace('Updated at 2022-07-31 16:02:02 UTC.', ''))
    with open('https.txt', 'w') as f:
        f.write(s)
    print(s)
    print(Fore.RED + 'Saved as https.txt')
elif (prox == "2"):

    fhand = ("http://youssef.clouduz.ru/socks4.php")

    r = requests.get(fhand)
    c = (r.text.replace('<pre style="word-wrap: break-word; white-space: pre-wrap;" data-copier-init="true" class="">',''))
    v = (c.replace('Free proxies from free-proxy-list.net',''))
    r = (v.replace('</pre>', ''))
    s = (r.replace('Updated at 2022-07-31 16:02:02 UTC.', ''))
    with open('socks4.txt', 'w') as f:
        f.write(s)
    print(s)
    print(Fore.RED + 'Saved as socks4.txt')
elif (prox == "3"):

    fhand = ("http://youssef.clouduz.ru/socks5.php")
    r = requests.get(fhand)
    c = (r.text.replace('<pre style="word-wrap: break-word; white-space: pre-wrap;" data-copier-init="true" class="">',''))
    v = (c.replace('Free proxies from free-proxy-list.net',''))
    r = (v.replace('</pre>', ''))
    s = (r.replace('Updated at 2022-07-31 16:02:02 UTC.', ''))
    with open('socks5.txt', 'w') as f:
        f.write(s)
    print(s)
    print(Fore.RED + 'Saved as socks5.txt')
