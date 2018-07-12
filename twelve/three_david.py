from collections import OrderedDict

class LRUCache(object):
    
    def __init__(self, size_limit):
        self.size_limit = size_limit
        self._cache = OrderedDict()
        
    def _update(self, key):
        if key in self._cache:
            val = self._cache[key]
            self.remove(key)
            self._cache[key] = val
        return self
        
    def insert(self, key, val):
        if key in self._cache:
            self._update(key)
        else:
            if len(self._cache) == self.size_limit:
                self._cache.popitem(0)
            self._cache[key] = val
        return self
    
    def lookup(self, key):
        self._update(key)
        return self._cache.get(key)
    
    def remove(self, key):
        self._cache.pop(key)
        return self