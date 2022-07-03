import requests
import json
import wget

url = 'https://filterlists.com/api/directory'
whitelist = ['4','7','17']
blacklist = ['21']
class FilterLists:
    def init(self,lists,maintainers,syntaxes,tags):
        self.getLists()
        self.getMaintainers()
        self.getSyntaxes()
        self.getTags()

    def getLists(self):
        response_info = requests.get(url + '/lists').json()
        for list in response_info:
            list_name = list['name']
            list_syntax_ids = list['syntaxIds']
            list_url = list['primaryViewUrl']
            #print(list_name)
            #print(syntax_ids)
            #print(list_url)
            for id in list['syntaxIds']:
                if(id in whitelist):
                    print(id)
                    if(list['syntaxIds'] not in blacklist):
                        if (list['primaryViewUrl'].endswith('.txt')):
                            try:
                                print("Downloading: \n"+ list['primaryViewUrl'])
                                wget.download(list['primaryViewUrl'], out='filters/')
                            except:
                                continue

    def getMaintainers(self):
        maintainers = []
        response_info = requests.get(url + '/maintainers').json()
        for maintainer in response_info:
            print(
                maintainer['id'],
                maintainer['name'],
                maintainer['url'],
                maintainer['filterListIds'],
            )
    def getSyntaxes(self):
        response_info = requests.get(url + '/syntaxes').json()
        for list in response_info:
            print(
                list['id'],
                list['name'],
            )
    def getTags(self):
        response_info = requests.get(url + '/tags').json()
        print(responseinfo)

#    def getSoftware(self):
#        response_info = requests.get(url + '/software').json()
#        for list in response_info:
#            print(
#                list['id'],
#                list['name'],
#                list['']
#            )
#    def getLanguages(self):
#        response_info = requests.get(url + '/languages').json()
#        print(responseinfo)

#    def getLicenses(self):
#        response_info = requests.get(url + '/licenses').json()
#        print(responseinfo)