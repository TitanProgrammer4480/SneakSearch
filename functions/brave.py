from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs


def brave_search(s_term):
  session = HTMLSession()
  s_results = []
  results = session.get(f"https://search.brave.com/search?q={s_term}&offset=0")
  results.html.render()
  soup = bs(results.text, 'html.parser')
  divs = soup.find_all("div", attrs={"data-type": "web"}, class_="snippet svelte-wmqx28")
  for i in divs:
    url = i.find("a", class_="h svelte-8pffig l1")["href"]
    title = i.find("div", class_="sitename svelte-11ps6r1").text
    description = i.find("div", class_="snippet-description desktop-default-regular")
    s_results.append({"url": url, "title": title, "description": description})
  return s_results