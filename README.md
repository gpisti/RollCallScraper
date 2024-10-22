# RollCallScraper

RollCallScraper is a Python-based web scraping tool designed to extract data about US senators' roll call votes from [Senate.gov](https://www.senate.gov/legislative/votes_new.htm). This project automates the collection of vote records and exports them into a structured format, such as CSV, for analysis or reporting.

## Features
- Scrapes attendance data from a target website
- Exports data to CSV
- Simple and customizable scraping logic
- Easy to configure for different attendance systems

## Prerequisites

Make sure you have the following installed before using this project:

- Python 3.x
- Required Python libraries (see [requirements.txt](requirements.txt))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gpisti/RollCallScraper.git
   ```
2. Navigate to the project directory:

```bash
cd RollCallScraper
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python scraper.py
```
  Update the scraping logic or configuration to match your target website. Modify the scraping script in ```scraper.py``` as necessary. If your target attendance system requires specific headers, login credentials, or a different scraping approach, you can update the necessary settings within the script.

6. Run the script:

   ```bash
   python scraper.py
   ```
7. The attendance data will be extracted and saved to a CSV file in the project directory.
