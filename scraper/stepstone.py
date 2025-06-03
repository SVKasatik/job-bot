from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def search_stepstone_jobs(keywords, location="Berlin"):
    query = "+".join(keywords)
    url = f"https://www.stepstone.de/jobs/{query}/in-{location}"

    options = Options()
    options.add_argument("--window-size=1920x1080")
    # options.add_argument("--headless")  # включи, если не хочешь видеть окно браузера

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(3)

    # Удаляем cookie-баннер ДО прокрутки
    try:
        button = driver.find_element(By.XPATH, "//div[contains(text(), 'Alles akzeptieren')]")
        driver.execute_script("arguments[0].click();", button)
        print("[INFO] Cookie button clicked via JS on visible text")
        time.sleep(4)
    except Exception as e:
        print(f"[WARN] Cookie button click failed: {e}")


    # Прокручиваем вниз, чтобы подтянулись вакансии
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)

    # Ищем карточки вакансий
    job_cards = driver.find_elements(By.CSS_SELECTOR, "article[data-testid='job-element']")
    print(f"[INFO] Найдено карточек на StepStone: {len(job_cards)}")

    results = []
    for card in job_cards[:10]:
        try:
            title = card.find_element(By.CSS_SELECTOR, "h2").text
            company = card.find_element(By.CSS_SELECTOR, "div[data-genesis-element='COMPANY_NAME']").text
            link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

            results.append({
                "title": title,
                "company": company,
                "link": link,
                "contact_email": None
            })
        except Exception as e:
            print(f"[WARN] Skipped card: {e}")
            continue

    driver.quit()
    return results
