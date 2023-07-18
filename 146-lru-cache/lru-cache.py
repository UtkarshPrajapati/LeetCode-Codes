class LRUCache:
    def __init__(self, capacity):
        self.odict, self.capacity = OrderedDict(), capacity
    def get(self, key):
        if key in self.odict:
            self.odict.move_to_end(key)
            return self.odict[key]
        return -1
    def put(self, key, value):
        if key in self.odict: self.odict[key] = value;self.odict.move_to_end(key)
        else:
            self.odict[key] = value
            if len(self.odict) > self.capacity: self.odict.popitem(last=False)