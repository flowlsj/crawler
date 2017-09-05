#! /usr/bin/env python
# --*-- coding:utf-8 --*--

import sys
from time import sleep

# from file_parser import FileParser
from crawler.crawler import UrlManager, HtmlDownloader, HtmlParser

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__=="__main__":
    # file_parser = FileParser(CONFIG.WORDS_INDEX)
    # words_list = file_parser.parse()
    # print words_list
    # mongodb = MongoDBHelper(database=CONFIG.MONGODB_DATABASE, host=CONFIG.MONGODB_SERVER, port=CONFIG.MONGODB_PROT)
    #
    # mongodb.insert_documnets(collection=CONFIG.MONGODB_COLLECTION, documnets=words_list)

    if len(sys.argv) != 2:
        print """
            Usage: python main.py url_to_craw
        """

    data_file = open("data.txt", 'w')
    word_set = set()

    url_manager = UrlManager(root_url=sys.argv[1], look_up_depth=100000)

    while url_manager.has_url():
        next_url = url_manager.get_url()
        page = HtmlDownloader.getHtml(url=next_url)
        print "Getting content from link: %s\n" % next_url
        word_dict = HtmlParser.parse_content(page)
        if word_dict is not None:
            for word, link in word_dict.items():
                if word not in word_set:
                    data_file.write("Title: %s -- Link: %s\n" % (word, link))
                    url_manager.add_url(current_url=next_url, new_url=link)
                    word_set.add(word)
            sleep(1)
    data_file.close()

    pass
