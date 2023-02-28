#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size= 0 ):
        self.brand = brand
        self.size = size

    def get_int_size(self):
        return self._size

    def set_int_size(self, size):
        if(isinstance(size, int)):
            self._size = size

        else:
            print("size must be an integer")

    size = property(get_int_size, set_int_size)

    def cobble(self):
        self.condition = "New"
        print('Your shoe is as good as new!')


