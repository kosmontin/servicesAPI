import requests


def main():
    cities = ['London', 'svo', 'Череповец']
    for city in cities:
        response = requests.get(f'https://wttr.in/{city}', params={'nT': '', 'lang': 'ru'})
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()