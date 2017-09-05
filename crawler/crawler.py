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
        first_seq_index = str(root_url).find('/', 10)
        if first_seq_index != -1:
            self.base_url = root_url[0: first_seq_index]
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

    def add_url(self, current_url, new_url):
        if current_url is None or new_url is None:
            return
        if len(self.urls) < self.look_up_depth:
            if new_url.startswith("http") or new_url.startswith("www"):
                self.urls.append(new_url)
            elif new_url.startswith("/"):
                new_url = self.base_url + new_url
                self.urls.append(new_url)
            else:
                last_slash_index = current_url.rfind('/')
                new_url = current_url[0: last_slash_index + 1] + new_url
                self.urls.append(new_url)

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
            response = requests.get(url=url, timeout=5)
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
    def parse_content(cls, page, tag='a'):
        if page is None:
            return None
        word_dict = dict()
        bs = BeautifulSoup(page, 'lxml')
        nodes = bs.find_all(tag)
        for node in nodes:
            if node.string is not None:
                word_dict[node.string] = node.get('href')
        return word_dict
class contentManager(object):
    pass
