import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# URL de la página web que queremos scrape
url = "https://es.wikipedia.org/wiki/Python"

# Obtener el contenido HTML de la página web
response = requests.get(url)
html = response.content

# Parsear el contenido HTML utilizando Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Obtener el texto de la página
texto_original = soup.get_text()

# Crear un objeto Translator para traducir el texto
translator = Translator()

# Traducir el texto a inglés
texto_traducido = translator.translate(texto_original, dest='en').text

# Crear una nueva instancia de BeautifulSoup con el texto traducido
soup_traducido = BeautifulSoup(texto_traducido, 'html.parser')

# Reemplazar el texto original con el texto traducido en el objeto soup
for tag in soup.find_all():
    tag.string = tag.string.replace(texto_original, texto_traducido)

# Crear un nuevo archivo HTML con el contenido traducido
with open('pagina_traducida.html', 'w') as file:
    file.write(str(soup))
