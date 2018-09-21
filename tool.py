#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
DBNAME = 'news'


def connect(DBNAME, query):
    ''''''

    # connect to the data base execute query return data

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    data = c.fetchall()
    db.close()
    return data


def topviews():
    ''''''


sql_query = \
    '''SELECT title, COUNT(path) as views\
     FROM log join articles on '/article/' || articles.slug = log.path \
     WHERE left(path,9)='/article/'group by path,title\
     order by views desc limit 3'''

data = connect(DBNAME, sql_query)
print '''
 Popular Articles:
'''
for i in range(0, len(data), 1):
    print '"' + data[i][0] + '" - ' + str(data[i][1]) + ' views'


def topauthors():
    ''''''


sql_query = \
    '''
      SELECT name ,sum(articlevies.views) as autorviews FROM (
      SELECT name , COUNT(path) as views
      FROM log,articles,authors WHERE '/article/' || articles.slug = log.path
       and articles.author = authors.id  group by path, name) as articlevies 
      group by name order by autorviews desc
                                         '''
data = connect(DBNAME, sql_query)
print '''
 popular Authors:
'''
for i in range(0, len(data), 1):
    print '"' + data[i][0] + '" - ' + str(data[i][1]) + ' views'


def error_percentage():
    ''''''


sql_query = \
    '''
     SELECT  daylogs.time , 
    (errors.errorsaday::float*100 / daylogs.logsaday::float) 
     as errorsp from (select (time :: date) , count (time ) 
     as errorsaday from log
     where status = '404 NOT FOUND'
     group by (time :: date))as errors ,
     (SELECT (time :: date) , 
     count (time ) as logsaday from log
     group by (time :: date)) as daylogs 
     where daylogs.time = errors.time and 
     (errors.errorsaday::float*100 / daylogs.logsaday::float) > 1
     group by daylogs.time,errors.errorsaday,daylogs.logsaday

     '''
data = connect(DBNAME, sql_query)
print '''
Days with more than 1% of errors:
'''
for i in range(0, len(data), 1):
    print str(data[i][0]) + ' - ' + str(round(data[i][1], 2)) \
        + '% Errors'

if __name__ == '__main__':
    topviews()
topauthors()
error_percentage()
print '''
Success!
'''
