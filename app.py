import requests
from bs4 import BeautifulSoup

def scrape_weather_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        xpath_element = soup.select_one(
            'html body app-root app-today one-column-layout wu-header sidenav mat-sidenav-container mat-sidenav-content div section div:nth-of-type(3) div:nth-of-type(1) div div:nth-of-type(1) div:nth-of-type(1) lib-city-current-conditions div div:nth-of-type(2) div div div:nth-of-type(3) span')
        
        if xpath_element:
            return xpath_element.text.strip()
        else:
            return "Data not found."
    else:
        print("Error accessing the website.")
        return None

def post_data_to_website(url, data):
    # Replace 'your_endpoint_url' with the actual URL where you want to post the data
    endpoint_url = "https://nicolelaine.github.io/temperature"
    payload = {"data": data}

    try:
        response = requests.post(endpoint_url, data=payload)
        if response.status_code == 200:
            print("Data posted successfully.")
        else:
            print("Failed to post data. Status Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error posting data:", e)

if __name__ == "__main__":
    url = "https://www.wunderground.com/weather/us/az/tucson/KAZTUCSO658"
    scraped_data = scrape_weather_data(url)

    # If data is not found, don't post to the website
    if scraped_data != "Data not found.":
        post_data_to_website("https://nicolelaine.github.io/temperature", scraped_data)
