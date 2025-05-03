import requests
from bs4 import BeautifulSoup
import csv

def scrape_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    # Save response HTML locally for debugging purpose
    with open("debug_response.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    # For Hacker News front page, titles are in <a class="storylink"> or just <a> inside <td class="title">
    headlines = []
    # Try to find title links inside <a> tags with class 'storylink' or newer, just <a> inside <td class="title">
    for td in soup.find_all('td', class_='title'):
        a_tag = td.find('a')
        if a_tag:
            title = a_tag.get_text(strip=True)
            if title and title != 'More':  # skip "More" link at bottom
                headlines.append(title)

    # Remove duplicates preserving order
    headlines = list(dict.fromkeys(headlines))

    return headlines

def save_to_csv(data, filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Headline'])
            for row in data:
                writer.writerow([row])
        print(f"Saved {len(data)} headlines to {filename}")
    except IOError as e:
        print(f"Error saving to {filename}: {e}")

if __name__ == "__main__":
    url = 'https://news.ycombinator.com/'
    headlines = scrape_headlines(url)
    if headlines:
        save_to_csv(headlines, 'headlines.csv')
    else:
        print("No headlines found or error occurred.")





