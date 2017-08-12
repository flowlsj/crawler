#! /usr/bin/env python
# --*-- coding:utf-8 --*--

from pymongo import MongoClient

class MongoDBHelper(object):
    def __init__(self, database, host='localhost', port=27017):
        self.mongo_client = MongoClient(host, port)
        self.database = self.mongo_client[database]

    def insert_documnets(self, collection, documnets):
        """
        Insert documents to collection
        :param collection: the collection to insert documents to
        :param documnets: the documents to insert, could be one dic or list of dic
        :return: document id
        """
        document_id = self.database[collection].insert(documnets)
        print document_id

    def get_documnets(self, collection, condition=None):
        if condition is not None:
            documents = self.database[collection].find(condition)
            return documents
        else:
            return self.database[collection].find()

    def remove_documnets(self, collection, condition):
        self.database[collection].remove(condition)

    def update_documents(self, collection, condition, properties):
        self.database[collection].update_one(condition, properties)

if __name__=="__main__":
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client['word']
    pass