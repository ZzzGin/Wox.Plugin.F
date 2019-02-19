# -*- coding: utf-8 -*-

from wox import Wox
from fuzzywuzzy import process
import json
import webbrowser

class FastStart(Wox):

    def query(self, query):
        with open('urls.json') as json_file:  
            urls = json.load(json_file)
        websites = list(urls)
        guess, simi = process.extractOne(query, websites)
        results = []
        results.append({
            "Title": "ff {}".format(guess),
            "SubTitle": "Similarity: {}, urls: {}".format(simi, urls[guess]),
            "IcoPath":"Images/app.png",
            "JsonRPCAction":{
                "method": "newBrowserTab",
                "parameters":[guess],
                "dontHideAfterAction":False
            }
        })
        return results
    
    def newBrowserTab(self, ws):
        with open('urls.json') as json_file:  
            urls = json.load(json_file)
        url = urls[ws]
        with open('browsers.json') as json_file:  
            browsers_path = json.load(json_file)
        br_path = browsers_path["defaultBrowser"]
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(br_path), 1)
        webbrowser.get('chrome').open_new_tab(url)


if __name__ == "__main__":
    FastStart()
    
# >>> url = 'https://www.google.com'
# >>> chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# >>> chrome_path
# 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
# >>> webbrowser.register('chrome', None, None,webbrowser.BackgroundBrowser(chrome_path), 1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: register() takes from 2 to 4 positional arguments but 5 were given
# >>> webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path), 1)
# >>> webbrowser.get('chrome').open_new_tab(url)
# True