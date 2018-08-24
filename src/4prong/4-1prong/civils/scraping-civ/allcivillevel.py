from bs4 import BeautifulSoup
import urllib.request
import time
import csv

ERROR = 0
i = 0
TOT = 18
with open('civlink.csv', 'r') as am:
    civilprograms = csv.reader(am, delimiter='\n')
    print("Starting scraper...")
    for civil in civilprograms:
        civ = 'https://www.kth.se/student/kurser/program/' + civil[0] + '/20172/kurslista'
        req = urllib.request.Request(civ)
        try:
            content = urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            print("Error on", civ)
            ERROR += 1
            with open('error404.csv', 'a') as er:
                er.write(civ + "\n")
            continue
        i += 1
        print("Scraping,", civ, "Current errors", ERROR)
        print("Scrape no.", i, "of", TOT)
        time.sleep(3)
        soup = BeautifulSoup(content, "html.parser")
        # Locate the div with desiered info:
        div = soup.find('div', {'class': 'paragraphs'})
        with open(civil[0] + '.csv', 'w+') as output:
                output.write(civ +"\n" + str(div.encode('utf-8')))
