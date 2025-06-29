import requests
from bs4 import BeautifulSoup
import json

url = "https://icons.getbootstrap.com/"

# Descargar HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Buscar íconos dentro de la lista
icons = []
icon_divs = soup.select("#icons-list > li > a >div>i")
for div in icon_divs:
   
    classes = div.get("class", [])
    for c in classes:
        print(c)
        print(c.startswith("bi-"))
        if c.startswith("bi-"):
            icons.append(c)

# Eliminar duplicados y ordenar
icons = sorted(set(icons))

# Guardar JSON
with open("bootstrap-icons.json", "w", encoding="utf-8") as f:
    json.dump(icons, f, indent=2)

print(f"{len(icons)} íconos guardados en bootstrap-icons.json")
