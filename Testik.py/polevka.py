from bs4 import BeautifulSoup
import requests

url = "https://js-trebesin.github.io/bsoup-exam/"

# all_h = soup.find_all("h2")

# list = []


def main():

    response = requests.get(url)

    BeautifulSoup(response.content, "html.parser")
    # <--- Úkol: popiš krátce, co tohle dělá ==> Parser dává omáčku do polévky U: kdo chce omáčku v polévce?
    # U: chybí vytvoření proměnné soup

    all_p = soup.find_all("p")
    # U: odkazujete se na proměnnou soup, kterou jste nikdy nevytvořil
    # Na stránce navíc není jediný <p>

    list_p = []

    for p in all_p:
        list_p.append(h2.text)

    with open("polevka_ingredience.json", mode="w") as file:
        all_p = json.dump(all_h, file, indent=4)
        # U: proč přepisujete proměnnou all_p?


if __name__ == "__main__":
    main()
