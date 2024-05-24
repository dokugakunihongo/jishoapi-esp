import requests
from bs4 import BeautifulSoup


URL = "https://www.nichiza.com/rui/rui.php"
def Search(query):
    arrayDict = []
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }

    data = {
        'busqueda': query, 
        'enviar': 'Buscar / 検索' 
    }
    
    soup = BeautifulSoup(requests.post(URL, data = data, headers=headers).content, "html.parser")
    article = soup.find_all("article")

    for mean in article:
        if not mean:
            continue
        array = mean.text.split(" ",3)
        if (array[1] == ":"):
            a = array.pop()
            b = array.pop()
            del array[1]
            array.append(a+b)
        else:
            del array[2]
        
        if len(array) == 2:
            dictionary = {
                "kotoba": array[0],
                "yomikata": "",
                "imi": array[1]
            }
        else:
            dictionary = {
                "kotoba": array[0],
                "yomikata": array[1],
                "imi": array[2]
            }
        arrayDict.append(dictionary)
          
    return arrayDict  