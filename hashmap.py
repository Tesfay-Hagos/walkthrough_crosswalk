from hashtable import HashTable


class Map(HashTable):
    """

    """

    def __init__(self, size=11):
        """

        """
        super().__init__(size)
        self.values = [None] * self.size  # holds values

    def __str__(self):
        """

        """
        s = ""
        for slot, key in enumerate(self.slots):
            value = self.values[slot]
            s += str(key) + ":" + str(value) + ", "
        return s

    def __len__(self):
        """
        Return the number of key-value pairs stored in the map.
        """
        count = 0
        for item in self.slots:
            if item is not None:
                count += 1
        return count

    def __getitem__(self, key):
        """

        """
        return self.get(key)

    def __setitem__(self, key, value):
        """

        """
        self.put(key, value)

    def __delitem__(self, key):
        '''

        '''
        self.remove(key)

    def __contains__(self, key):
        '''

        '''
        return self.get(key) != -1

    def put(self, key, value):
        """
        Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
        """
        slot = super().put(key)
        if slot != -1:
            self.values[slot] = value
        return -1

    def get(self, key):
        """

        """
        slot = super().get(key)
        if slot != -1:
            return self.values[slot]
        return -1

    def remove(self, key):
        """
        Removes key:value pair.
        Returns slot location if item in hashtable, -1 otherwise
        """
        slot = super().remove(key)
        if slot != -1:
            self.values[slot] = None
        return slot

    def hash(self, item):
        """
        Remainder method
        """
        key = 0
        for x in item:
            key += ord(x)
        return key % self.size

