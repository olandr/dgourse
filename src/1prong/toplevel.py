from bs4 import BeautifulSoup
import urllib.request

toplink = "https://www.kth.se/student/kurser/org"
content = urllib.request.urlopen(toplink)
soup = BeautifulSoup(content, "html.parser")
# Locate the div with desiered info:
div = soup.find('div', {'class' : 'paragraphs departmentslist'})
href_tags = [];
# Extract the relevant data:
for anc in div.find_all('a', href=True):
    href_tags.append("https://www.kth.se" + anc['href'])
# Write to output
with open('top_link_file.csv', 'w') as file:
    for href_tag in href_tags:
        file.write(href_tag +"\n")
