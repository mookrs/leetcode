# https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
# https://leetcode.com/problems/lru-cache/description/

import collections


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
