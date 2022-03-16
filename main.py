nested_list = [
	['a', 'b', 'c', [1,2,3,4, [1,3,5,7, [9,9, ["r"]]]]],
	['d', 'e', 'f', 'h', False, [1,2,3]],
	[1, 2, None],
    [1, 2, None]
]

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

def deepListsGenerator (obj):
    for item in obj:
        if isinstance(item, list):
            yield from deepListsGenerator(item)
        else:    
            yield item

def mySimpleGenerator (obj):
    for cursor in range(len(obj)):
        current_obj = obj[cursor]
        for item in current_obj:
            yield item


def walk(node):
        if (isinstance(node, (str, bytes))):
            yield node
            return
        try:
            tree = iter(node)
        except TypeError:
            yield node
            return
        else:
            for child in tree:
                yield from walk(child)

   
class myIterSimple():
    def __init__(self, collection):
        self._collection = collection
        self.start = -1
        self.arr = []
        self.stop = 0
        self.arr1 = self.flat_arr()
       
    def __iter__(self):
        return self
    
    def __next__(self):
        
        self.start +=1
        
        if self.start == len(self.arr):
            raise StopIteration
        return self.arr[self.start]

    def flat_arr(self):
        self.arr = []
        for item in self._collection:
            if isinstance(item, list):
                for i in item:
                    self.arr.append(i)
            else:
                self.arr.append(item)
        return self.arr

class myIterDeep():
    def __init__(self, collection):
        self._collection = collection
        self.child = 0

    def __iter__(self):
        yield from walk(self._collection)

    def walk(self):
        if (isinstance(self._collection, (str, bytes))):
            yield self._collection
            return
        try:
            tree = iter(self._collection)
        except TypeError:
            yield self._collection
            return
        else:
            for child in tree:
                yield from walk(child)

if __name__ == '__main__':
    

    for item in deepListsGenerator(nested_list):
        print(item)
    print('*' * 50)

    flat_list = [item for item in deepListsGenerator(nested_list)]
    print(flat_list)
    print('*' * 50)

    for j in myIterDeep(nested_list):
        print(j)
    print('*' * 50)
    
    flat_list = [item for item in myIterDeep(nested_list)]
    print(flat_list)
    print('*' * 50)
    
    for j in myIterSimple(nested_list_1):
        print(j)
    print('*' * 50)
    
    flat_list = [item for item in myIterSimple(nested_list_1)]
    print(flat_list)
    print('*' * 50)