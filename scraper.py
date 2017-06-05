import scraperwiki
import csv
#guidance on csv library at https://scraperwiki.com/docs/python/python_csv_guide/

#scrape the csv file into new variable 'data'
data = scraperwiki.scrape('https://data.birmingham.gov.uk/dataset/e9c314fc-fb6d-4189-a19c-7eec962733a8/resource/6b00d8f0-3855-4be0-ae2b-6775df64010a/download/traffic-signals-dec2016.csv')

#first attempt generated an error: "SqliteError: Binary strings must be utf-8 encoded"
#So we need to trace which part of our data is responsible. We're going to 

#use .reader function and .splitlines() method to put 'data' into csv object 'reader'
reader = csv.reader(data.splitlines())
print reader

record = {}

idno = 0
#Some code that decodes UTF-8
#http://yosaito.co.uk/scraperlibs/python/scraperwiki/sqlite.py

for row in reader:
    print type(row[0])
    print type(row[1])
    print type(row[2])
    print type(row[3])
    print type(row[4])
    print type(row[5])
    print type(row[6])
    record['usrn'] = row[0]
    record['row'] = row[1]
    record['district'] = row[2]
    record['ward'] = row[3]
    record['captured by'] = row[4]
    record['longitude'] = row[5]
    record['latitude'] = row[6]
    idno += 1
    record['ID'] = idno
    print record
    scraperwiki.sqlite.save(['ID'], record)

#This will generate an error with this data:
#SqliteError: Binary strings must be utf-8 encoded


# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
