class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]
    

    def _hash(self, key):
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)

        for pair in self.bucket[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.bucket[idx].append([key, value])
        

    def get(self, key: int) -> int:
        idx = self._hash(key)

        for k, v in self.bucket[idx]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)

        bucket = self.bucket[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)