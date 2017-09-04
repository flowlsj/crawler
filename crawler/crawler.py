#! /usr/bin/env python
# --*-- coding:utf-8 --*--

from bs4 import BeautifulSoup
import requests
from logger import logger

class Crawler(object):
    def __init__(self):
        pass
    pass

class UrlManager(object):
    def __init__(self, root_url, look_up_depth=1024):
        first_seq_index = root_url.find('/', start=10)
        if first_seq_index != -1:
            self.base_url = root_url.split('/')[0: first_seq_index]
        else:
            self.base_url = root_url
        self.urls = [root_url]
        self.offset = 0
        self.look_up_depth = look_up_depth

    def has_url(self):
        if self.offset >= len(self.urls):
            return False
        else:
            return True

    def add_url(self, new_url):
        if len(self.urls) < self.look_up_depth:
            if new_url.startwith("http"):
                self.urls.append(new_url)
            else:
                new_url = self.base_url + new_url

    def get_url(self):
        if self.has_url():
            url = self.urls[self.offset]
            self.offset += 1
            return url
        return None

class HtmlDownloader(object):
    def __init__(self):
        pass

    @classmethod
    def getHtml(cls, url, decode="GB2312"):
        html_content = None
        try:
            response = requests.get(url=url)
        except Exception as ex:
            logger.error(ex.message)
        else:
            html_content = response.content.decode(decode, "ignore")
        return html_content

    pass

class HtmlParser(object):
    def __init__(self):
        pass

    @classmethod
    def parse_content(cls, page):

        pass

class contentManager(object):
    pass
