# Written by Christopher Butler
# CS361
# Written by Christopher Butler
# CS361
# Microservice for Final Project
# Description: (First Draft) Takes in a website to be scraped for recipe via text document currently.
# Scrapes out the title, ingredients and instructions. No formatting done to the data. It is output in a txt document.

import requests
import time
from bs4 import BeautifulSoup

# Opens document to receive the URL of the website to scrape
while True:
    try:
        g = open("input.txt", 'r')
        URL = g.read()
        page = requests.get(URL)
        g.close()

        # Starts the parsing process and the information we want to find
        soup = BeautifulSoup(page.content, "html.parser")
        header = soup.find(class_="heading__title")
        ingredients = soup.find(id="section--ingredients_1-0")
        instructions = soup.find(id="section--instructions_1-0")

        # Instructions are listed as different elements, we find all elements with the required class tag
        tester = instructions.find_all("p", class_="comp mntl-sc-block mntl-sc-block-html")

        # Process information. Strip the text of all the unneeded tags. Write to document.
        w = header.text.strip()
        x = ingredients.text.strip()
        f = open("tester.txt", "r+")

        f.write(w)
        f.write("\n\n")  # Spaces for visual clarity
        f.write(x)

        for item in tester:
            f.write("\n\n")
            w = item.text.strip()
            f.write(w)

        f.close()

    except IOError:
        print("File not found.")
        time.sleep(3)
