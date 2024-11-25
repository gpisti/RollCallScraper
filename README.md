# RollCallScraper

RollCallScraper is a Python-based web scraping tool designed to extract data about US senators' roll call votes from [Senate.gov](https://www.senate.gov/legislative/votes_new.htm). This project automates the collection of vote records and exports them into a structured format, such as CSV, for analysis or reporting.

## Features

- Scrapes detailed voting data from the US Senate website.
- Exports data to CSV for easy analysis.
- Simple and customizable scraping logic.
- Easy to configure for different attendance systems.
- Includes a machine learning model to predict voting behavior based on historical data.

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

## Usage

### Scraping Data

1. Run the scraper script to collect voting data:

    ```bash
    python scraper.py
    ```

2. The attendance data will be extracted and saved to a CSV file in the project directory.

### Machine Learning Model

The `senate_vote_model.py` script processes the scraped data and trains a machine learning model to predict senators' voting behavior.

1. Ensure the `RollCallVotes.csv` file is present in the directory.

2. Run the model training script:

    ```bash
    python senate_vote_model.py
    ```

3. The script will:

    - Load and preprocess the data.
    - Train a RandomForestClassifier on the voting data.
    - Evaluate the model's performance using accuracy, confusion matrix, and classification report.
    - Save the trained model as `senate_vote_classifier.pkl`.

## Customization

- Update the scraping logic or configuration in `scraper.py` to match your target website. If your target attendance system requires specific headers, login credentials, or a different scraping approach, you can update the necessary settings within the script.
- Modify the machine learning model parameters in `senate_vote_model.py` to improve prediction accuracy or adapt to different datasets.


## License

This project is licensed under the MIT License.
