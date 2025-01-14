# In this data-scraping script we are definiting a function that
# will scrape the most recent headlines from espn and return them

from selenium import webdriver
import re

def get_headlines():
    """
    Scrapes headlines from espn while printing status messages.
    """
    url = 'https://www.espn.com/nba/'

    # Set up the webdriver (you need to have the appropriate browser driver installed)
    driver = webdriver.Chrome()  # For Chrome, you need ChromeDriver: https://sites.google.com/chromium.org/driver/
    driver.get(url)

    # Wait for the page's javascripts to load
    driver.implicitly_wait(30)

    # Get the page source
    html_content = driver.page_source

    # Close the browser window
    driver.quit()

    # Define a regular expression pattern to match the script content
    pattern = re.compile(r'<script type="text/javascript">(.*?)</script>', re.DOTALL)

    # Search for the javascripts in the HTML content
    javascripts = pattern.findall(html_content)

    for script in javascripts:
        # from jsbeautifier import beautify
        # print(beautify(match))
        
        # Look for headlines in each of the javascripts because the order
        # of the javascripts might change
        headline_pattern = re.compile(r'"headline":\s*"([^"]+)"')
        headlines = headline_pattern.findall(script)

        # If headlines are found, then this is the javascript that we are
        # looking for. Keep them in the headlines variable so it can be imported
        if headlines:
            print("Headlines scraped from ESPN.", "\n")
            break

    return headlines