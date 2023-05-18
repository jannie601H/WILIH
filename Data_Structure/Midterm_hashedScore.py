# code from groom
class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while (self.keys[i] != None) and (self.keys[i] != key):
            i = (i + 1) % self.size
            if i == start:
                return None # if Table is Full return None
        return i

    def set(self, key):
        i = self.find_slot(key)
        if i == None: # if Table is Full return None
            return None
        self.keys[i] = key
        return key
	
    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] == None:
            return None # if no key in Table, return None
        j = i
        while True:
            self.keys[i] = None
            self.values[i] = None
            while True:
                j = (j + 1) % self.size
                if self.keys[j] == None: # if j is unoccupied, move done
                    return key
                k = self.hash_function(self.keys[j])
                if not (i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i] = self.keys[j]
            self.values[i] = self.values[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None: # if i is occupied
            return self.values[i]
        else:
            return None

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)

Table = HashOpenAddr(80)

Table.values = [33.2, 19.7, 28, 21, 33, 6, 12, 15.5, 4.5, 29.2, 11.5, 15.5, 18.3, 15, 6, 6, 26.2, None, None, None, 19.5, 33, 13, 32.5, 14, 22.5, 9, 17, 50.7, 38.3, 4, 34, 22, 40, 38.6, 4.5, 47, 11.5, 24, 6, None, 35.5, 18, 12.2, 18.2, None, 31.5, None, 26.7, 34.5, None, None, 24.7, None, 9, None, 0, 24.9, 12, 9.5, 30.2, 28.5, 25.5, 15.2, 53.5, 28.5, 16.7, None, 13, 25.7, 30.5, None, None, None, None, 26.2, 25, None, None, 33.5]
Table.keys = [1455840, 1826080, 2176482, 9100563, 3080004, 8564800, 560726, 3506720, 8653680, 921769, 706650, 3805680, 5245362, 9039933, 8863760, 8963135, 5510560, None, None, None, 511060, 2708820, 8550660, 8817623, 4138980, 4207462, 4761140, 8776900, 1074108, 2366268, 5825382, 5884260, 4730192, 8825707, 9107709, 1261875, 2829236, 8356835, 811638, 1883878, None, 2305961, 2580282, 6983721, 8471724, None, 6901086, None, 6033648, 7333008, None, None, 2893812, None, 8855334, None, 6309176, 2180377, 1253178, 7934776, 505500, 717100, 1332540, 1832140, 6752860, 8051820, 7215906, None, 8423268, 3396628, 4017748, None, None, None, None, 3603915, 6668556, None, None, 7633839]

my_key = 2019 * 532 # myStudent id first 4 num * last 3 num
print('My score:', Table[my_key])
