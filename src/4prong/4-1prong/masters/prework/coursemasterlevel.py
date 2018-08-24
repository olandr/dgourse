from bs4 import BeautifulSoup
import urllib.request
import time
import csv
import re


ERROR = 0
i = 0
TOT = 67

def gather(master, content):

        print("Scraping,", master, "Current errors", ERROR)
        print("Scrape no.", i, "of", TOT)
        time.sleep(2)
        soup = BeautifulSoup(content, "html.parser")
        # Locate the div with desiered info:
        try:
            div = soup.find('a', href=True, text='Courses')

            with open('collective.csv', 'a') as output:
                output.write("https://www.kth.se/" + div.attrs['href'] + "\n")

            return 1
        except AttributeError as error:
                print("Error on", master)
                with open('error404courselist.csv', 'a') as er:
                    er.write(master + "\n")
                return 0


with open('allmasterRemoving.csv', 'r') as am:
    masters = csv.reader(am, delimiter='\n')
    print("Starting scraper...")
    for mast in masters:
        master = mast[0]

        try:
            req = urllib.request.Request(master)
            content = urllib.request.urlopen(req)
            out = gather(master, content)
            if (out == 0):
                i += 1
            else:
                ERROR += 1

        except urllib.error.HTTPError as e:
            print("Error on", master)

            ERROR += 1
            with open('error404courselist.csv', 'a') as er:
                er.write(master + "\n")
            continue
