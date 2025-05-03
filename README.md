🕸️ Web Scraper – News Headlines Extractor
This Python script is a simple web scraper built to extract the latest news headlines from Hacker News and save them into a CSV file.

🎯 Objectives
 ✅ Use the requests library to retrieve HTML content of a webpage.
 ✅ Parse the HTML using BeautifulSoup.
 ✅ Extract specific data (news article titles).
 ✅ Save the scraped data into a CSV file.
 ✅ Handle exceptions such as connection errors or HTML parsing issues.

🛠️ Tech Stack
 Python 3.x
 requests
 beautifulsoup4
 csv

📂 How It Works
 Sends an HTTP request to Hacker News using requests.
Parses the returned HTML using BeautifulSoup.
Extracts news headlines from <td class="title"> elements.
Stores the results in a CSV file named headlines.csv.

🚀 How to Run
Clone this repository:
git clone https://github.com/your-username/web-scraper-task2.git
cd web-scraper-task2

Install required libraries:
pip install requests beautifulsoup4

Run the script:
python scraper.py
Check the headlines.csv file for output.

📁 Output
The script saves the extracted headlines into a CSV file in this format:

⚠️ Error Handling
Proper exceptions are handled during network requests and file writing.
Invalid or unexpected HTML structures are managed gracefully.

📌 Notes
The script is currently tailored for Hacker News.
You can modify the scraping logic for other websites by adjusting the BeautifulSoup parsing section.

🤝 Contributions
Feel free to fork this repo, make improvements, and submit a pull request!
