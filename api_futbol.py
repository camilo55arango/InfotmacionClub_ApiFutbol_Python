import requests
import json

def get_team_info(team_id):
    url = f"https://api.football-data.org/v2/teams/{team_id}"
    headers = {"Auth-Token": "<API key>"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("No se pudo obtener la información del equipo.")

    data = json.loads(response.text)

    name = data["name"]
    founded = data["founded"]
    venue_name = data["venue"]["name"]
    venue_capacity = data["venue"]["capacity"]
    coach = data["squad"][0]["name"]
    players = [player["name"] for player in data["squad"]]

    print(f"Nombre: {name}")
    print(f"Año de fundación: {founded}")
    print(f"Estadio: {venue_name} (Capacidad: {venue_capacity})")
    print(f"Entrenador: {coach}")
    print(f"Jugadores:")
    for player in players:
        print(f"  - {player}")

get_team_info(66) # Ejemplo: ID del equipo del Barcelona es 66
