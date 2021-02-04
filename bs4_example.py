from bs4 import BeautifulSoup
import requests

# ---------- usage de BeautifulSoup
helloworld = "<p>Hello World</p>"
soup_string = BeautifulSoup(helloworld, "html.parser")
print(soup_string)


# --- utilidation de requests
url = "https://www.barnesandnoble.com/b/barnes-noble-classics/_/N-rqv"
response = requests.get(url)
soup_page = BeautifulSoup(response.content,"html.parser")
print(soup_page)

# -------- lecture d'un fichier html
with open("foo.html") as foo_file:
	soup = BeautifulSoup(foo_file, "html.parser")
print(soup)

#--- example de parsing -----------------------------------
html_atag = """<html><body><p>Test html a tag example</p>
<a href="http://www.test.com">Home</a>
<a href="http;//www.test.com/books">Books</a>
</body>
</html>"""
soup  = BeautifulSoup(html_atag,"html.parser")
atag = soup.a   # recupere la balise a, soup est suffixe par le nom de la balise
print(atag)     # affichage de la balise a
print(atag.string) # affichage de la valeur associee a la balise a
print(atag['href'])  # affichage de la valeur de href