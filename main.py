from web_driver import initialize_web_driver
from scraper import scrape_votes
from data_handler import save_data_to_csv
import os
import pandas as pd

def main():
    driver = initialize_web_driver()

    try:
        #SZÜKSÉGES ADATOK SCRAPELÉSE
        roll_call_votes, tally = scrape_votes(driver)

        # LISTÁK ÁTALAKÁTÁSA -> DATAFRAME
        df_roll_call_votes = pd.DataFrame(roll_call_votes)
        df_tally = pd.DataFrame(tally)

        # A KÉT DATAFRAME EGYESÍTÉSE
        merged_df = pd.merge(df_roll_call_votes, df_tally, on="Measure/Nominant Number", how="inner")

        # CSV MENTÉSE
        current_folder = os.path.dirname(os.path.abspath(__file__))
        merged_file_path = os.path.join(current_folder, "merged_votes.csv")
        save_data_to_csv(merged_df, merged_file_path)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
