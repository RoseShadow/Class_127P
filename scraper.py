from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/"

# Webdriver
browser = webdriver.Chrome("C:/Users/pc/Desktop/Whitehat junior/class/After Class100/python/Class 127 P/c127-Web-scrapping-1-main/chromedriver.exe")

browser.get(START_URL)

time.sleep(10)

scarped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )
        
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star_table= soup.find("table",attrs["class","wikitable"])
        table_body= bright_star_table.find('tbody')
        table_rows= table_body.find('tr')

        for rows in table_rows:
            table_cols=row.find_all('td')
            print(table_cols)

            for cols_data in table_cols:
                data= call






        # Find all elements on the page and click to move to the next page
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(planets_data, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
