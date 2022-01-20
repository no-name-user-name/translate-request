import requests

headers = {
    'Host': 'libretranslate.com',   
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Accept': '*/*',
    'Origin': 'https://libretranslate.com',
    'Content-Type': 'application/json',
}

postjson = {
    'q': "hello my friend",
    'source': "en",
    'target': "ru",
    'format': "text"
}

r = requests.post('https://libretranslate.com/translate', headers=headers, json=postjson)

print(r.json()['translatedText'])