
class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size

    def put(self, item):
        """
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise (no available slots, table is full)
        """

        hashvalue = self.hash(item)
        slot_placed = -1
        if self.slots[hashvalue] == None or self.slots[hashvalue] == item:  # empty slot or slot contains item already
            self.slots[hashvalue] = item
            slot_placed = hashvalue
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] != None and self.slots[nextslot] != item:
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue:  # we have done a full circle through the hash table
                    # no available slots
                    return slot_placed

            self.slots[nextslot] = item
            slot_placed = nextslot
        return slot_placed

    def get(self, item):
        """
        returns slot position if item in hashtable, -1 otherwise
        """
        startslot = self.hash(item)

        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1

    def remove(self, item):
        '''
        Removes item.
        Returns slot position if item in hashtable, -1 otherwise
        '''
        startslot = self.hash(item)

        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == item:
                found = True
                self.slots[position] = None
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        if found:
            return position
        return -1

    def hash(self, item):
        """
        Remainder method
        """
        return item % self.size

    def rehash(self, oldhash):
        """
        Plus 1 rehash for linear probing
        """
        return (oldhash + 1) % self.size


