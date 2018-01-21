#from flask import Flask
import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/331078540726047"
f = "fields=posts.limit(2){likes.summary(true),link,picture}"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{f}&{params}".format(host=host, path=path, f=f, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype (dictionary)
me = json.loads(resp)

#me is a dictionary, me.keys() is a list, me.values() is a list

# display the result
#pprint.pprint(me)

#num_of_posts = number of posts, in most-recent to least-recent order
#in the most recent number (given) of posts, gives the immage urls of better half 
def meme_getter(num_of_posts):
	li = []
	d = {}

	# of the two keys in the dictionary, the first is the posts; the second is the user id
	print(me.keys())
	posts, user_id = me.keys()

	for i in range(num_of_posts):
 		meme_url =  me[posts]["data"][i]["link"]
 		likes_summary = me[posts]["data"][i]["likes"][2]
 		total_count = likes_summary[summary][total_count]

 		#print(meme_url)
 		#picture_preview = me[posts]["data"][i]["picture"]
 		#print(picture_preview)
 		#full_meme_package = [meme_url, picture_preview]
 		li.append(meme_url)

 		d[meme_url] = total_count

	print(li)
	return li

#queue has a dictionary of meme urls paired with total number of likes per meme url
def best_meme_list(d):
	import operator
	queue = []

	max(d.iteritems(), key=operator.itemgetter(1))[0]

print(meme_getter(2))