from colorama import Fore, init
import requests

init()

banner = '''

 /$$$$$$$$ /$$   /$$ /$$$$$$$$
|__  $$__/| $$  | $$|__  $$__/
   | $$   | $$  | $$   | $$   
   | $$   | $$$$$$$$   | $$   
   | $$   | $$__  $$   | $$   
   | $$   | $$  | $$   | $$   
   | $$   | $$  | $$   | $$   
   |__/   |__/  |__/   |__/   
                               

@Privarp / ADMİN PANEL FİNDER
\n'''

print(banner)

while True:
    url = input("URL: ")
    urlbasharf = url[0]
    if urlbasharf == "h":
        wordlists = "wordlist.txt"
        urlsonharf = url[-1]

        file = open(wordlists, "r") 
        wordlistyazilari = file.readlines()
        file.close() 

        for line in wordlistyazilari:
            try: 
                line = line.replace("\n", "") 
                if urlsonharf == "/": 
                    request = url + line 
                else:
                    request = url + "/" + line

                islemibaslat = requests.get(request, timeout=5) 
                durumkodlari = islemibaslat.status_code
                yazdir = str(durumkodlari) 



                if durumkodlari == 200: 
                    print(Fore.LIGHTGREEN_EX + "[+] Sayfa Bulundu: " + request)
                else:
                    print(Fore.RED + "[-] Sayfa Bulunamadı: " + request + " --> " + "[" + yazdir + "]") 

            except requests.exceptions.ReadTimeout: 
                print(Fore.YELLOW + "[!] Zaman Aşımı: " + request)
            except requests.exceptions.RequestException as e:
                print(Fore.RED + "[-] İstek Hatası:", e)
        break      
    else:
        print("URL'yi Küçük Harflerle HTTP/HTTPS Formatında (https://) Yazınız")
