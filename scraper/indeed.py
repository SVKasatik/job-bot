# scraper/indeed.py

import requests
from bs4 import BeautifulSoup

def search_indeed_jobs(keywords, location="Berlin"):
    query = "+".join(keywords)
    url = f"https://de.indeed.com/jobs?q={query}&l={location}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("[ERROR] Не удалось загрузить Indeed")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("a", class_="tapItem")

    results = []
    for card in job_cards:
        title = card.find("h2", class_="jobTitle")
        company = card.find("span", class_="companyName")
        link = card["href"]
        full_link = f"https://de.indeed.com{link}"

        if title and company:
            results.append({
                "title": title.text.strip(),
                "company": company.text.strip(),
                "link": full_link,
                "contact_email": None  # пока нет, позже можно доставать
            })

    return results
