# Find python codes (e.g. on github) and read it
# find out what it does
# identify the parts of the code and comment

# package that collects several modules for working with URLs
import urllib
# json library-> parsing 'json'-code into python
import json
# import sys library
import sys
# imports os library
import os

accessToken = 'TOKENVALUE'  # YOUR ACCESS TOKEN GETS INSERTED HERE

	#list, contains command-line arguments -> passed to function
userId = sys.argv[1]          #USERID
	# limited to 100 users?
limit=100


url='https://graph.facebook.com/'+userId+'/posts?access_token='+accessToken +'&limit='+str(limit) #FB Link
	#var 'data' = url defined above
data = json.load(urllib.urlopen(url))
id=0

print str(id)
	# parsing 'time', 'date', 'year' out of var "data"
for item in data['data']:
   time=item['created_time'][11:19]
   date=item['created_time'][5:10]
   year=item['created_time'][0:4]

   # counting 'shares' if parsed from url
if 'shares' in item:
    num_share=item['shares']['count']
else:
    num_share=0
    # counting 'likes' if parsed in url
if 'likes' in item:
            num_like=item['likes']['count']
else:
            num_like=0


id+=1

print str(id)+'\t'+ time.encode('utf-8')+'\t'+date.encode('utf-8')+'\t'+year.encode('utf-8')+'\t'+ str(num_share)+'\t'+str(num_like)
