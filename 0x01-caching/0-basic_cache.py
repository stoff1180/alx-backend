#!/usr/bin/python3
"""Creates BasicCache class that inherits from BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defines BasicCache """

    def put(self, key, item):
        """ Assigns the item to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value associated with the given key """
        return self.cache_data.get(key)
