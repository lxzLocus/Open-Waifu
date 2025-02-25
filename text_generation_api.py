import requests

def generate_text(prompt):
    url = 'http://localhost:50596/generate'
    response = requests.post(url, json={'prompt': prompt})
    return response.json()
