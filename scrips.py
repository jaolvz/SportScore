import requests




key_apiFootball="x"

def pegando_tabela_por_cod (cod_liga):
    url = f"http://api.football-data.org/v4/competitions/{cod_liga}/standings"
    headers = {"X-Auth-Token": f"{key_apiFootball}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data

    else:
        print("Falha na requisição. Código de status:", response.status_code)



def artilheiros_Campeonato(cod_liga):
    url = f"http://api.football-data.org/v4/competitions/{cod_liga}/scorers"
    headers = {"X-Auth-Token": f"{key_apiFootball}"}

    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        jogadores = response.json()
        jogadores= jogadores["scorers"]
        return jogadores
    else:
        print(f"Erro {response.status_code}")

def pegar_proximo3jogos(id_time):
    url = f"https://api.football-data.org/v4/teams/{id_time}/matches?&status=SCHEDULED"
    headers = {'X-Auth-Token': key_apiFootball}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        matches = data['matches']
        next_matches = matches[:3]
        return next_matches
    else:
        print(f"Erro")


