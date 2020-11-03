import requests
import json
import numpy as np

class instaTag():
    def __init__(self):
        self.homeUri = 'https://www.instagram.com/directory/hashtags/'
        self.tagSearch = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23'
        self.navUri = 'https://www.instagram.com/explore/tags/'
        self.tagDict = None
        self.tagListParsed = {}
        self.compNumber = [100000, 1000000]
        self.compList = []

    def tagQuery(self, tag):
        formedUri = self.tagSearch+tag
        countTrack = 0
        headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

        response = requests.get(formedUri, headers=headers)
        self.tagDict = json.loads(response.text)

        for item in self.tagDict['hashtags']:
            self.tagListParsed[item['hashtag']['name']] = item['hashtag']['media_count']
            ++countTrack

        self.tagDictParsed = sorted(self.tagListParsed.items(), key=lambda x: x[1], reverse=True)
        list = self.tagListParsed

        for tag,count in list.items():
            if count <= self.compNumber[0]:
                lst = np.array(['Low', tag, count])
                self.compList.append(lst)
            elif count > self.compNumber[0] and count <= self.compNumber[1]:
                lst = np.array(['Medium', tag, count])
                self.compList.append(lst)
            elif count >= self.compNumber[1]:
                lst = np.array(['High', tag, count])
                self.compList.append(lst)
        self.compList = np.array(self.compList)