import time
from scraper.remoteok import search_remoteok_jobs
from scraper.arbeitnow import search_arbeitnow_jobs
from generator import generate_cover_letter
# from sender import send_email  ← временно отключено

KEYWORDS = ["Design", "System"]
CHECK_INTERVAL = 1800  # 30 минут
TEST_EMAIL = "svk3004@gmail.com"

def main():
    print("[DEBUG] Парсим RemoteOK...")
    print("[INFO] Job Bot started")

    jobs = search_remoteok_jobs(KEYWORDS)
    print(f"[INFO] Получено {len(jobs)} вакансий")

    for job in jobs:
        print(f"[FOUND] {job['title']} @ {job['company']}")
        job["contact_email"] = TEST_EMAIL
        letter = generate_cover_letter(job)
        print(f"\n--- COVER LETTER for {job['title']} @ {job['company']} ---\n")
        print(letter)
        print("\n---------------------------------------------\n")
        # send_email(job["contact_email"], letter, job)

    print("[DEBUG] Парсим Arbeitnow...")
    jobs = search_arbeitnow_jobs(KEYWORDS)
    print(f"[INFO] Получено {len(jobs)} вакансий")

    for job in jobs:
        print(f"[FOUND] {job['title']} @ {job['company']}")
        job["contact_email"] = TEST_EMAIL
        letter = generate_cover_letter(job)
        print(f"\n--- COVER LETTER for {job['title']} @ {job['company']} ---\n")
        print(letter)
        print("\n---------------------------------------------\n")
        # send_email(job["contact_email"], letter, job)

    print(f"[WAIT] Sleeping for {CHECK_INTERVAL / 60} minutes...")
    time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
