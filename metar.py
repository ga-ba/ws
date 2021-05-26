import sys

import requests
from bs4 import BeautifulSoup

HTTP_STRING = 'http://'
STRONA = '.infometeo.pl/'

escape_table = {'ą': 'a', 'ć': 'c',
                'ę': 'e', 'ł': 'l', 
                'ó': 'o', 'ń': 'n',
                'ś': 's', 'ź': 'z',
                'ż': 'z', ' ': '-'}

def escape(tekst):
    return ''.join(escape_table.get(znak, znak) for znak in tekst.lower())

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Użycie: python metar.py <miejscowość>')
        sys.exit(0)

    miasto = sys.argv[1]
    url = HTTP_STRING + escape(miasto) + STRONA
    r = requests.get(url)

    if r.status_code != 200:
        print('Nie udało się pobrać strony :-/')
        sys.exit(0)

    zupa = BeautifulSoup(r.content, 'html.parser')
    metar = zupa.find('pre', class_='metar')
    
    if metar:
        print(metar.string)
    else:
        print(f'{miasto} nie posiada depeszy METAR.')
