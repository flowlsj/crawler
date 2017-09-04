#! /usr/bin/env python
# --*-- coding:utf-8 --*--

import sys

# from file_parser import FileParser
from crawler.crawler import UrlManager, HtmlDownloader

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    # file_parser = FileParser(CONFIG.WORDS_INDEX)
    # words_list = file_parser.parse()
    # print words_list
    # mongodb = MongoDBHelper(database=CONFIG.MONGODB_DATABASE, host=CONFIG.MONGODB_SERVER, port=CONFIG.MONGODB_PROT)
    #
    # mongodb.insert_documnets(collection=CONFIG.MONGODB_COLLECTION, documnets=words_list)

    url_manager = UrlManager(root_url="http://www.chengyudaquan.net/feisizichengyu/list_1.html", look_up_depth=100000)

    while url_manager.has_url():
        next_url = url_manager.get_url()
        page = HtmlDownloader.getHtml(url=next_url)
        print page

    pass
