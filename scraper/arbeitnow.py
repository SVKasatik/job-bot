from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def search_arbeitnow_jobs(keywords, location=None):
    print("[DEBUG] Парсим RemoteOK...")
    print("[INFO] Job Bot started")
    print("[DEBUG] Запускаем Selenium для Arbeitnow...")

    options = Options()
    options.add_argument("--window-size=1200,800")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.arbeitnow.com/remote-jobs")
        time.sleep(4)

        job_links = driver.find_elements(By.CSS_SELECTOR, "h2 > a[href*='/jobs/']")
        print(f"[INFO] Найдено карточек: {len(job_links)}")

        results = []
        for link_el in job_links[:10]:
            try:
                title = link_el.text.strip()
                company_el = link_el.find_element(By.XPATH, '../../../..//a[contains(@href, \"/companies/\")]')
                company = company_el.text.strip()
                href = link_el.get_attribute("href")

                if True:
                    results.append({
                        "title": title,
                        "company": company,
                        "link": href,
                        "contact_email": None
                    })
            except Exception as e:
                print(f"[WARN] Ошибка при парсинге карточки: {e}")
                continue

        print(f"[DEBUG] Вернули {len(results)} вакансий")
        return results

    finally:
        driver.save_screenshot("arbeitnow_debug_final.png")
        driver.quit()
