#! /usr/bin/env python
# --*-- coding:utf-8 --*--

from config.config import CONFIG
from database.mongo import MongoDBHelper
from file_parser import FileParser

if __name__=="__main__":
    file_parser = FileParser(CONFIG.WORDS_INDEX)
    words_list = file_parser.parse()
    print words_list

    mongodb = MongoDBHelper(database=CONFIG.MONGODB_DATABASE, host=CONFIG.MONGODB_SERVER, port=CONFIG.MONGODB_PROT)

    mongodb.insert_documnets(collection=CONFIG.MONGODB_COLLECTION, documnets=words_list)
