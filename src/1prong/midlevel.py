from bs4 import BeautifulSoup
import urllib.request
import csv
import time
import re
# Open the output file to append all the data
with open('courses.csv', 'w') as f:
    # Open the file with links to scrape
    with open('top_link_file.csv', 'r') as file:
        print("Starting scraper...")
        # It is a .csv so use relevant module
        deplinks = csv.reader(file, delimiter='\n')
        # Well pretty obvious, the file is a collection of links, the csv.read
        # outputs a nested array, access the first element in this matrix.
        for deparr in deplinks:
            # We want to be kind to KTH -- sleep.
            print("Scraping")
            time.sleep(60)
            dep = deparr[0]
            print(dep)
            content = urllib.request.urlopen(dep)
            soup = BeautifulSoup(content, "html.parser")
            table = soup.find('tbody')
            # Matrix (nested array) of all courses [prob redundant]
            data = []
            # All subsequent links (link to course sites)
            href_tags = []
            # Use regex to extract the departement of the current deplink
            departement = re.search('((?!/))(.\w*)$', dep).group(2)
            # Scrape the table of the departement
            for d in table.find_all('tr'):
                course = []
                raw = d.find_all('td')
                link = "https://www.kth.se" + d.find('a', href=True)['href']
                hp = raw[1].text
                code = raw[2].text
                level = raw[3].text
                href_tags.append(link)
                course.append([link, hp, code, level])
                data.append(course)
                # Write to output
                f.write(departement + ";" + link + ";" + hp + ";" + code + ";" + level + "\n")
