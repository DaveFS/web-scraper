from urllib.request import urlopen
import re

#link to page section: https://realpython.com/python-web-scraping-practical-introduction/#get-to-know-regular-expressions

#url = "https://www.bbc.co.uk/news/articles/cwyv8y68e25o" #bbc news article page
#url = "http://olympus.realpython.org/profiles/aphrodite" # tutorial site
url = "http://olympus.realpython.org/profiles/poseidon" # tutorial site - causes error with simple positional extract because of blank space.

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

print(title)
