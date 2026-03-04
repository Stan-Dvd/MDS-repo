import requests

def get_weather():
    # Coordonate pentru București
    lat, lon = 44.43, 26.10
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Verifică dacă cererea a reușit
        data = response.json()
        temp = data['current_weather']['temperature']
        print(f"Salut! În București sunt acum {temp}°C.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")

if __name__ == "__main__":
    get_weather()