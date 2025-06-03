# scraper/indeed.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def search_indeed_jobs(keywords, location="Berlin"):
    query = "+".join(keywords)
    url = f"https://de.indeed.com/jobs?q={query}&l={location}"

    # Настройка браузера
    options = Options()
    # options.add_argument("--headless")  # убрать, если хочешь видеть браузер
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Дать сайту время загрузиться (обходит Cloudflare/JS защиту)
    time.sleep(10)

    results = []
    job_cards = driver.find_elements(By.CLASS_NAME, "tapItem")

    for card in job_cards:
        try:
            title = card.find_element(By.CLASS_NAME, "jobTitle").text
            company = card.find_element(By.CLASS_NAME, "companyName").text
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
    print(f"[INFO] Found {len(results)} jobs on Indeed")

    return results
