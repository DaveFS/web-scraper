from urllib.request import urlopen
import re

#link to page section: https://realpython.com/python-web-scraping-practical-introduction/#get-to-know-regular-expressions

#url = "https://www.bbc.co.uk/news/articles/cwyv8y68e25o" #bbc news article page
#url = "http://olympus.realpython.org/profiles/aphrodite" # tutorial site
#url = "http://olympus.realpython.org/profiles/poseidon" # tutorial site - causes error with simple positional extract because of blank space.
url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

print(title)

#re.findall("pattern","string",optional 3rd) - locates pattern in indicated string, 3rd argument can be applied e.g. IGNORECASE
#re.search("pattern","string",optional 3rd) - every possible result, even within other matches
#re.sub("pattern","replacement","string") - replaces everything in the indicated match with the 2nd argument