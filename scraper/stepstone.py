# scraper/stepstone.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def search_stepstone_jobs(keywords, location="Berlin"):
    query = "+".join(keywords)
    url = f"https://www.stepstone.de/jobs/{query}/in-{location}"

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    # options.add_argument("--headless")  # можно включить потом

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(5)  # ждём загрузку

    results = []
    job_cards = driver.find_elements(By.CSS_SELECTOR, "a[data-at='job-card']")

    for card in job_cards[:10]:  # ограничим до 10 для скорости
        try:
            title = card.find_element(By.CSS_SELECTOR, "span[class*='JobCard-title']").text
            company = card.find_element(By.CSS_SELECTOR, "span[class*='JobCard-company']").text
            link = card.get_attribute("href")

            results.append({
                "title": title,
                "company": company,
                "link": link,
                "contact_email": None
            })
        except Exception as e:
            print(f"[WARN] Skipped job: {e}")
            continue

    driver.quit()
    return results
