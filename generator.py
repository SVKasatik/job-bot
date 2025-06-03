# generator.py

from jinja2 import Template

def generate_cover_letter(job):
    with open("templates/cover_letter_template.txt", "r", encoding="utf-8") as file:
        template = Template(file.read())
    letter = template.render(
        job_title=job.get("title", "Ihre Stelle"),
        company=job.get("company", "Ihr Unternehmen")
    )
    return letter
