
from api.FilterLists import FilterLists
filter = FilterLists()
filter.getLists()






        for list in response_info:
            if (list['primaryViewUrl'].endswith('.txt')):
                try:
                    wget.download(url, out='filters/')
                except:
                    continue