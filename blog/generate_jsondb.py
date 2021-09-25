import json
import function

POSTS = function.get_articles()

articles_db = []
for i in POSTS:
    tags, date, lecture_time, key, title, extra, preview = i.tag()
    json_article = {
        "title": title,
        "date": date,
        "link": "htttps://blog.xtraorbitals.xyz/#" + key,
        "preview": preview,
        "tag": tags
    }
    articles_db.append(json_article)

with open("articles_db.json", "w") as write_file:
    json.dump(articles_db, write_file, indent=4)
