import psycopg2


def get_most_popular_articles():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("""select a.title as title, paths.views as views from articles a
    inner join
    (select substring(l.path from 10) as path, count(l.id) as views
    from log l
    where l.status = '200 OK'
    and l.path not like '/'
    group by path) as paths on paths.path = a.slug
    order by paths.views desc
    limit 3""")
    articles = c.fetchall()
    for article in articles:
        print article[0] + " - " + str(article[1]) + " views"
    db.close()


def get_most_popular_authors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("""select au.name, sum(paths.views) as views
    from articles a
    inner join authors au on a.author = au.id
    inner join
    (select substring(l.path from 10) as path, count(l.id) as views
    from log l
    where l.status = '200 OK'
    and l.path not like '/'
    group by path) as paths on paths.path = a.slug
    group by au.name
    order by views desc""")
    authors = c.fetchall()
    for author in authors:
        print author[0] + " - " + str(author[1]) + " views"
    db.close()


def get_days_with_more_errors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute("""select to_char(percentage.date, 'FMMonth dd, YYYY') as date,
    percentage.errors || '% ' as percentage
    from ( select data.date,
    round(sum(data.qtderrors)/sum(data.requests)*100, 1) as errors
    from ( select distinct date_trunc('day', time) as date,
    0 requests, count(*) as qtderrors
    from log l
    where l.status = '404 NOT FOUND'
    group by date
    union
    select date_trunc('day', time) date, count(*) requests, 0 as qtderrors
    from log
    group by date
    ) as data
    group by data.date
    ) as percentage
    where percentage.errors > 1""")
    percentage_list = c.fetchall()
    for percentage in percentage_list:
        print str(percentage[0])+" - "+percentage[1]+' errors'
    db.close()


print "1. What are the three most popular articles of all time? "
get_most_popular_articles()

print "\n"
print "2. Who are the most popular article authors of all time? "
get_most_popular_authors()


print "\n"
print "3. On which days did more than 1% of requests lead to errors?  "
get_days_with_more_errors()
