import re, json

def getStringFromFile():
    #Returns a long string with all the file's contents
    #fileName = "C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\Weblogs\\History.txt"
    fileName = "C:\\Users\\John\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\history"
    with open(fileName, encoding="latin-1") as f: #"utf-8"
        data = f.read()
        return data
        #firstbit = data[0:5000]
        #print(firstbit)

def findBBCURLs(inputString):
    #Returns all unique BBC URLs, removing slashes from the end and removing 'BBC' which shouldn't be there.
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', inputString)
    #cut down to just bbc urls
    bbcURLSomeWithForwardSlash = [url for url in urls if (url.startswith("http://bbc.co.uk") or url.startswith("http://www.bbc.co.uk"))]
    #remove slash from the end
    bbcURLsSomeWithWWW = [(url if not url.endswith("/") else url[:-1]) for url in bbcURLSomeWithForwardSlash ]
    #replace www.bbc.co.uk with bbc.co.uk
    bbcURLsMayEndInBBC = [url.replace("www.bbc.co.uk", "bbc.co.uk").replace("bbc.co.uk", "www.bbc.co.uk") for url in bbcURLsSomeWithWWW] #first replace www.bbc.co.uk with bbc.co.uk, then change all of them to www.bbc.co.uk
    # remove BBC from end of URL
    bbcURLsMayEndInSlashAgain = [url if not url.endswith("BBC") else url[:-3] for url in bbcURLsMayEndInBBC]
    # Remove slashes again in case BBC occurred after a slash.
    listURLs = [(url if not url.endswith("/") else url[:-1]) for url in bbcURLsMayEndInSlashAgain ]
    setURLs = set(listURLs)
    dictWithCount = {}
    for url in setURLs:
        if(listURLs.count(url)>5):
            print(url)
        dictWithCount[url] = listURLs.count(url)

    return dictWithCount  #convert to a set to remove duplicates
dict = findBBCURLs(getStringFromFile())
print(dict)
values = set(list(dict.values()))
print(values)


def get_url_dict_list():
    # create a tuple containing useful info about the url, for example is it a home page,
    # what are the various sections of the URL etc.
    bbc_url_dict_list = []
    url_dict = findBBCURLs(getStringFromFile())
    urls = url_dict.keys()
    for url in urls:
        url_split = url.split('/')[3:]  #3: removes ['http:', '',  from the start
        #print (len(url_split))
        #print (url_split)
        my_len = len(url_split)
        if my_len == 0:
            myCategories = ('','','','')
        else:
            if (url_split[0].startswith("search")):
                myCategories = ('search','','','')
            else:
                #print (url_split)
                #print (my_len)

                myCategories = (
                    url_split[0],
                    '' if my_len < 2 else url_split[1],
                    '' if my_len < 3 else url_split[2],
                    '' if my_len < 4 else url_split[3]
                )
        cat0 = myCategories[0]
        tuple = platformHomepageDict.get(myCategories[0])
        is_homepage = 1 if my_len < 2 else 0
        if tuple is not None:
            myPlatform = platformHomepageDict.get(cat0)
            bbc_url_dict_list.append({'platform': myPlatform,
                                     'is_homepage': is_homepage,
                                     'category_0': myCategories[0],
                                     'category_1': myCategories[1],
                                     'category_2': myCategories[2],
                                     'category_3': myCategories[3],
                                     'url': url,
                                     'proportion': url_dict[url]})
            # bbc_url_tuples.append([myPlatform, is_homepage, myCategories[0], myCategories[1], myCategories[2], myCategories[3], url, url_dict[url]])
        else:
            print ("---Not found in list - " + cat0)
    return bbc_url_dict_list


#tuple becomes list
#platform:
# app_name
# homepage
# o   news news, newsHome
# o   sport sport, sportHome
# o   cbbc cbbc
# o   iplayer  iplayer
# o   rm radio
# search search
# food food
# weather
# programmes ??
# blogs
platformHomepageDict = {"news":     "news",
                        "newsHome": "news",
                        "sport":    "sport",
                        "sportHome":"sport",
                        "cbbc":     "cbbc",
                        "cbbcThe":  "cbbc",
                        "music":    "rm",
                        "radio":    "rm",
                        "radio4":   "rm",
                        "iplayer":  "iplayer",
                        "food":     "food",
                        "search":   "search",
                        "blogs":    "blogs",
                        "programmes": "programmes",
                        "id":       "id",
                        "weather":  "weather",
                        "tv":       "tv",
                        "":         "main_home_page",
                        None:       "---",
                        }


url_dict_list = get_url_dict_list()
#myListOfTuples.sort(key=lambda tup: tup[0])  #sort by key
# url_dict.sort(key = lambda tup: len(tup[6]))
# print (url_dict_list)
# for dict_list in url_dict_list:
    # print (dict_list)

# with open('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\output_files\\urls.json', 'w') as outfile:
#     json.dump(url_dict_list, outfile, indent = 3)

print('---result')
with open('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\output_files\\urls.json', 'w') as outfile:
    for dict in url_dict_list:
        print(dict)
        outfile.write(json.dumps(dict))