import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, features="html.parser")
products = soup.select(".product_pod")
example = products[0]
print(example.select("a")[1]["title"])
two_star_titles = []
for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)
print(two_star_titles)
