
import psycopg2


def get_most_popular_articles():
  db = psycopg2.connect(database="news")
  c = db.cursor()
  c.execute(" select a.title as title, paths.views as views " + 
  "from articles a " +
  "inner join  ( " + 
  "select substring(l.path from 10) as path, count(l.id) as views " +
  "from log l " +
  "where l.status = '200 OK' " +
  "and l.path not like '/' " +
  "group by path) as paths on paths.path = a.slug " +
  "order by paths.views desc " +
  "limit 3 " )  
  
  articles= c.fetchall()
  for article in articles:
	print article[0] + " - " + str(article[1]) + " views"  
  db.close()

def get_most_popular_authors():
 db = psycopg2.connect(database="news")
 c = db.cursor()
 c.execute("select au.name, sum(paths.views) as views " +
 "from articles a " +
 "inner join authors au on a.author = au.id " +
 "inner join  ( " +
 "select substring(l.path from 10) as path, count(l.id) as views  " +
 "from log l " +
 "where l.status = '200 OK' " +
 "and l.path not like '/' " +
 "group by path) as paths on paths.path = a.slug " +
 "group by au.name " +
 "order by views desc " )

 authors = c.fetchall()
 for author in authors:
	print author[0] + " - " + str(author[1]) + " views"  
 db.close()

print "1. What are the three most popular articles of all time? "  
get_most_popular_articles()

print "\n"
print "2. Who are the most popular article authors of all time? "
get_most_popular_authors()