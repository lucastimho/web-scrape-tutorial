import requests
import bs4

# results = requests.get("https://example.com/")
# print(results.status_code)
# print(results.text)
# soup = bs4.BeautifulSoup(results.text, features="html.parser")
# print(soup.select("title")[0].getText())
# site_paragraphs = soup.select("p")
# print(site_paragraphs[0].getText())
res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, features="html.parser")
for txt in soup.select(".toctext"):
    print(txt.getText())
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, features="html.parser")
computer = soup.select(".thumbimage")[0]["src"]
image_link = requests.get("https:" + computer)
print(image_link.content)
f = open("my_computer_image.png", "wb")
f.write(image_link.content)
f.close()
