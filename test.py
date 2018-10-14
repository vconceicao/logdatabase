
import psycopg2


def get_articles():
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute("select * from articles ")
  articles = c.fetchall()
  db.close()
  return articles
  
print get_articles()