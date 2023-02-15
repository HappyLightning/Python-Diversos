import requests
import json
import pandas as pd

header = {'X-MAL-CLIENT-ID': '58b0bf09130f3ae6159af85a49c0d223'}


# Listagem geral de todos os animes, retorna lista de 'ids'.
def anime_list():
    url = 'https://api.myanimelist.net/v2/anime?q=one&limit=20'
    req = requests.get(url, headers=header)
    ids = []
    iterations = len(req.json()['data'])

    # Iteração.
    for x in range(iterations):
        response = json.dumps(req.json()['data'][x]['node']['id'])
        ids.append(response)
    return ids


# Requisição para detalhes de cada anime com base no 'id'.
def anime(id):
    url = f'https://api.myanimelist.net/v2/anime/{id}?fields=title,main_picture,alternative_titles,genres,num_episodes,start_season,pictures,related_anime,recommendations,studios'
    req = requests.get(url, headers=header)
    response = req.json()
    return response


# Chamadas.
ids = anime_list()
animes = [anime(x) for x in ids]
data = pd.json_normalize(animes)
data.to_excel(r'C:\Users\Felipe Lopes\Desktop\anime.xlsx')  # Salva como excel.
