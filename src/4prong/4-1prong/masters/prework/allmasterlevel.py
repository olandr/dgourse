from bs4 import BeautifulSoup
import urllib.request

allmasterlink = "https://www.kth.se/utbildning/master-magisterutbildning/engelska-program"
content = urllib.request.urlopen(allmasterlink)
soup = BeautifulSoup(content, "html.parser")
# Locate the div with desiered info:
div = soup.find('div', {'class' : 'paragraphs'})


href_tags = [];
# Extract the relevant data:
for anc in div.find_all('a', href=True):
    href_tags.append(anc['href'])
# Write to output
with open('test.csv', 'w') as file:
    for href_tag in href_tags:
        file.write(href_tag +"\n")
