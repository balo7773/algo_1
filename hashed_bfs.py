#/usr/bin/python3

class Hash():
    """ Custom made hash table.

    Attributes:
        arr (list): array to be stored with values for respective keys
        key_arr (set): storing keys ensuring no duplicate
        key_hash (set): key hash storage
        special_arr (list): special key for collision handling
        same_hash (set): storing special key hash
    """
    def __init__(self) :
        self.arr = [None] * 100
        self.key_arr = set()
        self.key_hash = set()
        self.special_arr = [None] * 100
        self.same_hash = set()

    def add(self, *args):
        """ Map key to values, using hash function to hash the keys

        Args:
            *args (postional argument): stores key-value pairs
            
        """

        hsh = None # hash variablw

        # check if args is not odd
        if len(args) % 2 != 0:
            raise ValueError('Arguments must be in key-value pairs')

        for i in range(0,len(args),2):

            if args[i] in self.key_arr: # check if key exists
                raise ValueError('Key exists, choose a different one')
            elif isinstance(args[i], int): # check if key is of type int
                raise TypeError("integers are not allowed as keys")
            else:
                key = sum( ord(j) for j in args[i]) # turn keys to values and summing them
                hsh = (key * 103) % len(self.arr) # hashing the key through arithmetic operation

                if hsh in self.key_hash or self.arr[hsh] is not None: # handlng collision

                    hsh = (key**2 * 103) % len(self.arr)
                    if hsh in self.key_hash or self.arr[hsh] is not None: 
                        if self.special_arr[hsh] is not None: # checks if special array isn't filled up 
                            self.special_arr[hsh] = args[i + 1]
                        else:
                            raise Exception('Memory Block is full')
                    self.same_hash.add(args[i])

                self.key_arr.add(args[i])
                self.key_hash.add(hsh)
                self.arr[hsh] = args[i + 1]
    
    def get(self, key):
        ''' Get values for keys

        Args:
            keys (string)

        Return:
            Value to corresponding key or None
        '''
        if key not in self.key_arr:
            return None
        if key in self.same_hash:
            index = ((sum(ord(j) for j in key) ** 2) * 103) % len(self.arr)
        else:
            index = (sum(ord(j) for j in key) * 103) % len(self.arr)
        
        if index in self.key_hash:
            return self.arr[index]

        return None

def run_tests():
    ''' Test case'''
    h = Hash()

    # Test 1: Add and retrieve single key-value pair
    h.add("apple", "fruit")
    assert h.get("apple") == "fruit"

    # Test 2: Multiple key-value pairs
    h.add("banana", "yellow", "carrot", "orange", "dog", "animal")
    assert h.get("banana") == "yellow"
    assert h.get("carrot") == "orange"
    assert h.get("dog") == "animal"

    # Test 3: Overwriting not allowed (should raise ValueError)
    try:
        h.add("apple", "new_fruit")
    except ValueError:
        print("Test 3 Passed: Duplicate key correctly blocked")
    else:
        print("Test 3 Failed: Duplicate key was added")

    # Test 4: Non-string key (should raise TypeError)
    try:
        h.add(123, "number")
    except TypeError:
        print("Test 4 Passed: Non-string key blocked")
    else:
        print("Test 4 Failed: Non-string key allowed")

    # Test 5: Odd number of arguments (should raise ValueError)
    try:
        h.add("key1", "value1", "key2")  # Missing value for key2
    except ValueError:
        print("Test 5 Passed: Odd number of arguments blocked")
    else:
        print("Test 5 Failed: Odd number of arguments allowed")

    # Test 6: Handling collisions properly
    h.add("aaaa", "first_value")
    h.add("aaab", "collision_value")  # This should hash similarly
    assert h.get("aaaa") == "first_value"
    assert h.get("aaab") == "collision_value"

    # Test 7: Getting a non-existing key should return None
    assert h.get("nonexistent") is None

    print("All assertions passed. Other tests manually checked!")


# def bfs

