#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import csv
import time
import re
# from urllib.error import HTTPError


PARTIAL = 3659
TOTAL = 7058
ERRORS = 7
# Pretty much the same as midlevel.
with open('pre_half.csv', 'w') as f:
    with open('pre_half_link.csv', 'r') as file:
        print("Starting scraper...")
        courselinks = csv.reader(file, delimiter='\n')
        p = 0
        t = 3397
        print("Current status: partials:", PARTIAL, "TOTAL: t", t, "of TOTAL", TOTAL)
        for link in courselinks:
            NEDLAGD = False
            course = link[0]

            # Catch error see: https://docs.python.org/3/howto/urllib2.html#httperror
            req = urllib.request.Request(course)
            try:
                content = urllib.request.urlopen(req)
            except urllib.error.HTTPError as e:
                print("Error on", course)
                ERRORS += 1
                with open('error500.csv', 'a') as er:
                    er.write(course + "\n")
                continue
            p += 1
            t += 1
            print("Scraping: no.", p, "of", PARTIAL, "(", t, TOTAL, ")", "PUT ASIDE:", ERRORS)
            print(course)
            # We want to be kind to KTH -- sleep.
            time.sleep(3)
            soup = BeautifulSoup(content, "html.parser")
            obs = soup.find('div', {'class':'information'})
            title = soup.find('span', {'property':'teach:courseTitle'}).text
            # We need to know if whether or not this course is NEDLAGD (I will ignore other attributes for now; like "course info for an unstarted term")
            if obs != None:
                # The child (the 'p') of the  div>class:information will have some text containing "nedlagd" if it is nedlagd.
                if 'nedlagd' in obs.find_next('p').text:
                    NEDLAGD = True
            header = soup.find('h2', text='Behörighet')
            requirements = ''
            if header != None:
                requirements = header.find_next('p').text
            #Write to output
            f.write(str(NEDLAGD) + ";" + str(title.encode('utf-8')) + ";" + str(course.encode('utf-8')) + ";" + str(requirements.encode('utf-8')) + "\n")
