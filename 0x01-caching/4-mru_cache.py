#!/usr/bin/python3
"""Creates MRUCache class that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Defines MRUCache """

    def __init__(self):
        """ Initializes MRUCache """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """ Assigns the item to the dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value associated with the given key """
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
