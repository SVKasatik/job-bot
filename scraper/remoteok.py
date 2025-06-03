import requests
from bs4 import BeautifulSoup

print("[DEBUG] Парсим RemoteOK...")

def search_remoteok_jobs(keywords, location=None):
    print("[DEBUG] Загружаем вакансии с RemoteOK...")
    query = "+".join(keywords).lower()
    url = f"https://remoteok.com/remote-{query}-jobs"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://google.com",
        "DNT": "1",
        "Connection": "keep-alive"
    }


    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("[ERROR] Failed to load RemoteOK")
        return []

    with open("remoteok_debug.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("[DEBUG] Сохранён файл remoteok_debug.html")

    print("[DEBUG] Content-Type:", response.headers.get("Content-Type"))


    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="job")

    print(f"[INFO] Найдено карточек на RemoteOK: {len(jobs)}")

    results = []
    for job in jobs[:10]:
        try:
            title = job.find("h2").text.strip()
            company = job.find("h3").text.strip()
            link = "https://remoteok.com" + job.find("a", href=True)["href"]

            results.append({
                "title": title,
                "company": company,
                "link": link,
                "contact_email": None  # email мы не знаем, пока ставим None
            })
        except Exception as e:
            print(f"[WARN] Ошибка при разборе карточки: {e}")
            continue

    print(f"[DEBUG] Вернули {len(results)} вакансий")

    return results
