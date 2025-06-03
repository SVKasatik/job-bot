# main.py

import time
from scraper.stepstone import search_stepstone_jobs
from scraper.indeed import search_indeed_jobs
from generator import generate_cover_letter
from sender import send_email

KEYWORDS = ["Design", "System"]
LOCATION = "Berlin"
CHECK_INTERVAL = 1800  # 30 минут

# для теста можно вставить email напрямую
TEST_EMAIL = "svk3004@gmail.com"

def main():
    print("[INFO] Job Bot started")
    while True:
        jobs = search_indeed_jobs(KEYWORDS, LOCATION)
        for job in jobs:
            print(f"[FOUND] {job['title']} @ {job['company']}")
            # временно указываем email вручную
            job["contact_email"] = TEST_EMAIL
            letter = generate_cover_letter(job)
            send_email(job["contact_email"], letter, job)

        jobs_stepstone = search_stepstone_jobs(KEYWORDS, LOCATION)
        for job in jobs_stepstone:
            print(f"[FOUND] (StepStone) {job['title']} @ {job['company']}")
            job["contact_email"] = TEST_EMAIL
            letter = generate_cover_letter(job)
            send_email(job["contact_email"], letter, job)


        print(f"[WAIT] Sleeping for {CHECK_INTERVAL / 60} minutes...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
