import scraperwiki
import csv
#guidance on csv library at https://scraperwiki.com/docs/python/python_csv_guide/

#scrape the csv file into new variable 'data'
data = scraperwiki.scrape('https://data.birmingham.gov.uk/dataset/14492d37-1a77-4d46-9204-27363fc62149/resource/bacf38dd-3530-4c95-a0c3-83e21c9b2259/download/sgmsreportsvcsfreportsvcsfreports201415vcsfreport2014qtr1final.csv')

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
    print type(row[7])
    if row['funding'] is not None:
      row['funding'] = row['funding'].decode("latin-1")
    record['ref'] = row[0]
    record['organisation'] = row[1]
    record['status'] = row[2]
    record['start_date'] = row[3]
    record['end_date'] = row[4]
    record['revised_end'] = row[5]
    record['directorate'] = row[6]
    record['funding'] = row[7].decode("latin-1")
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
