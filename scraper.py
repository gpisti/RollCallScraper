from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def clean_labels(text):
    """Remove known labels from the text, handling extra spaces and line breaks."""
    labels = [
        "Vote Date:",
        "Vote Result:",
        "Measure Title:",
        "Nomination Description:",
        "Measure Number:",
        "Nomination Number:",
    ]

    for label in labels:
        if label in text:
            text = text.replace(label, "").strip()

    return text.strip()

def scrape_votes(driver):
    """Scraping multiple datas from the given website"""
    roll_call_votes = []
    tally = []

    # Kattint -> https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_118_2.htm URL-t tartalmazó linkre
    new_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="secondary_col2"]/div[1]/p[1]/a'))
    )
    new_page.click()

    dropdown = Select(driver.find_element(By.XPATH, '//*[@id="listOfVotes_length"]/label/select'))
    dropdown.select_by_visible_text("All")

    # AZ ÖSSZES RÉSZLETET TARTALMAZÓ LINKEK GYŰJTÉSE
    votes_table = driver.find_elements(By.XPATH, '//*[@id="listOfVotes"]/tbody/tr')
    vote_links = [row.find_element(By.XPATH, "./td[1]/a").get_attribute("href") for row in votes_table]

    for link in vote_links:
        driver.get(link)
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        # BS4 SETUPJA
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        # SZAVAZATI ADATOK SCRAPELÉSE
        date_element = soup.select_one("#secondary_col2 > div:nth-of-type(1) > div:nth-of-type(3)")
        date = clean_labels(date_element.get_text(strip=True)) if date_element else ""

        result_element = soup.select_one("#secondary_col2 > div:nth-of-type(1) > div:nth-of-type(6)")
        result = clean_labels(result_element.get_text(strip=True)) if result_element else "---"

        number_element = soup.select_one("#secondary_col2 > div:nth-of-type(1) > div:nth-of-type(8) > a")
        number = clean_labels(number_element.get_text(strip=True)) if number_element else "---"

        title_element = soup.select_one("#secondary_col2 > div:nth-of-type(1) > div:nth-of-type(9)")
        title = clean_labels(title_element.get_text(strip=True)) if title_element else "---"

        roll_call_votes.append({
            "Measure/Nominant Number": number,
            "Date of the vote": date,
            "Vote Result": result,
            "Measure Title/Nomination Description": title,
        })

        # SENÁTOR ADATAINAK SCRAPELÉSE
        div_content = soup.find("div", class_="newspaperDisplay_3column")
        span_content = div_content.find("span", class_="contenttext")
        text_content = span_content.get_text(separator="\n")
        senator_lines = [line for line in text_content.split("\n") if line]

        for index in range(0, len(senator_lines), 2):
            name_aff_state = senator_lines[index].split("(")
            senators_name = name_aff_state[0].strip()
            affiliation = name_aff_state[1][0]
            state = name_aff_state[1][2:4]
            vote = senator_lines[index + 1]

            tally.append({
                "Measure/Nominant Number": number,
                "Senator's name": senators_name,
                "Vote result": vote,
                "Senator's party affiliation": affiliation,
                "Senator's state": state,
            })

    return roll_call_votes, tally
