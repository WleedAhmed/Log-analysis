#!/usr/bin/env python2

import psycopg2


conn = psycopg2.connect("dbname=news")
c = conn.cursor()


q1 = """
select title, count(*) as views
from articles join log 
    on concat('/article/', articles.slug) = log.path
where log.status like '%200%'
group by log.path, articles.title 
order by views desc limit 3;
"""

c.execute(q1)
print("\n" * 10)
print("Most popular three articles:\n")
for (title, view) in c.fetchall():
    print("  {} - {} views".format(title, view))
print("\n \n")


q2 = """
select authors.name, count(*) as views
from articles join authors 
    on articles.author = authors.id 
    join log on concat('/article/', articles.slug) = log.path 
where log.status = '200 OK' 
group by authors.name 
order by views desc;
"""

c.execute(q2)
print("Most popular authors:\n")
for (name, view) in c.fetchall():
    print("  {} - {} views".format(name, view))
print("\n \n")


q3 = """
select * from (
    select a.day,
    round(cast((100*b.views) as numeric) / cast(a.views as numeric), 1)
    as val from
        (select date(time) as day, count(*) as views from log group by day) as a
        join
        (select date(time) as day, count(*) as views from log 
        where status = '404 NOT FOUND' group by day) as b
            on a.day = b.day) as errors 
where val > 1;
"""

c.execute(q3)
print("days at which more than 1% of requests led to errors:\n")
for (date, percentage) in c.fetchall():
    print("  {} - {}% errors\n \n \n \n \n \n".format(date, percentage))


conn.close()
