from bs4 import BeautifulSoup
import urllib.request
import time
import csv



ERROR = 0
i = 0
TOT = 67

def gather(master, content):
        print("Scraping,", master, "\nCurrent errors", ERROR)
        print("Scrape no.", i, "of", TOT)
        time.sleep(2)
        soup = BeautifulSoup(content, "html.parser")
        # Locate the div with desiered info:
        div = soup.find('div', {'class': 'paragraphs'})

        listelem = soup.find_all('ul', {'class':'courseList'})

        with open('collective.csv', 'a') as output:
            output.write(master + "\n")
            for L in listelem:
                output.write("\n" + L.text)
            output.write("+++++++++++++++++" + "\n")
        return 1

with open('masterUnderCourse.csv', 'r') as am:
    masters = csv.reader(am, delimiter='\n')
    print("Starting scraper...")
    for mast in masters:
        master = mast[0]
        try:
            req = urllib.request.Request(master)
            content = urllib.request.urlopen(req)
            i += gather(master, content)
        except urllib.error.HTTPError as e:
            print("Error on", master)
            ERROR += 1
            with open('error404courselist.csv', 'a') as er:
                er.write(master + "\n")
            continue
