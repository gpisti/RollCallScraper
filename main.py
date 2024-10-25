from web_driver import initialize_web_driver
from scraper import scrape_votes
from data_handler import save_data_to_csv
import os
import pandas as pd


def main():
    driver = initialize_web_driver()

    try:
        # SZÜKSÉGES ADATOK SCRAPELÉSE
        data = scrape_votes(driver)

        flat_data = []
        for roll_call in data:
            for vote in roll_call["votes"]:
                
                # ÖSSZEÁGYAZOTT ADATHALMAT KISIMÍTÁSA A CSV-HEZ
                flat_data.append(
                    {
                        "Date of the vote": roll_call["date"],
                        "Vote result": roll_call["vote result"],
                        "Measure/Nominant Number": roll_call["m/n.number"],
                        "Measure Title/Nomination Description": roll_call["title/description"],
                        "Senator's name": vote["Senator's name"],
                        "Senator's voting record": vote["Vote"],
                        "Senator's party affiliation": vote["Affiliation"],
                        "Senator's state": vote["State"],
                    }
                )

        df_data = pd.DataFrame(flat_data)

        # CSV MENTÉSE
        current_folder = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_folder, "RollCallVotes.csv")
        save_data_to_csv(df_data, file_path)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
