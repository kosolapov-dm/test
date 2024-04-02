#Надо скачать файл из поля для решения, там будет ссылка, по ссылке файл с названием следующего документа внутри.
#Чтобы получить очередной документ, допишите его название к "https://stepik.org/media/attachments/course67/3.6.3/" .
#И так пока не упретесь в последний файл, там текст, начинается с "We",  его надо написать как ответ.



import requests
proxies = {
    'http': 'http://kosolapov_dm:dh2bun*oM!n9@10.3.1.2:3128',
    'https': 'http://kosolapov_dm:dh2bun*oM!n9@10.3.1.2:3128',
}

with open('C:\\Users\\kosolapov_dm\\Downloads\\dataset_3378_3.txt') as ouf:
    url = ouf.read().strip()

r = requests.get(url, proxies=proxies)
while True:
    if not r.text.startswith('We'):
        r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/' + r.text, proxies=proxies)
        continue
    else:
        if r.text.startswith('We'):
            print(r.text)
            break

