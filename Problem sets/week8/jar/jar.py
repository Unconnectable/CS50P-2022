class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._size = 0
            self._capacity = capacity

    def __str__(self):
        str_ = ""
        for _ in range(1, self._size + 1):
            str_ += "🍪"
        return str_

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self._size:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
