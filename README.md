# Personal portfolio

A professional, academic-first portfolio built with Flask and Bootstrap. There is no database: all content is simple and local.

## Run locally

```powershell
py -m pip install -r requirements.txt
py app.py
```

Open `http://127.0.0.1:5000`.

## Where to edit things

| Update | Location |
| --- | --- |
| Name, biography, education, skills, projects and links | `content/portfolio.py` |
| Profile picture | `static/assets/images/profile/` |
| School/university logos | `static/assets/images/education/` |
| Certificates | `static/assets/documents/certificates/` |
| Transcripts | `static/assets/documents/transcripts/` |
| CV/resume | `static/assets/documents/resume/` |
| Colours and small visual refinements | `static/css/site.css` |

When you add a document or image, put it in the relevant folder and update its `file` value in `content/portfolio.py`. Do not store sensitive documents in a public website repository.
