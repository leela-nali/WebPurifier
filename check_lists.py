def checkWhitelist(list):
    with open('whitelist.json', 'r') as whitelist:
        wl_data = json.load(whitelist)
        if(list not in wl_data):
            return False
        else:
            return True
def checkBlacklist(list):
    with open('blacklist.json', 'r') as blacklist:
        bl_data = json.load(blacklist)
        if(list not in bl_data):
            return False
        else:
            return True