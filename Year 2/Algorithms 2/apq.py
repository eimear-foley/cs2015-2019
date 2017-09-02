class Element:
    """ A key, value and index. """
    def __init__(self, k, v, i):
        self._key = k
        self._value = v
        self._index = i

    def __str__(self):

        return ("k: %i, v: %s, i: %i" % (self._key, self._value, self._index))

    __repr__ = __str__

    def __eq__(self, other):
        return self._key == other._key

    def __lt__(self, other):
        return self._key < other._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

class APQ:
    def __init__(self):
        self._heap = []

    def __str__(self):

        outstr = ""
        for item in self._heap:
            elt = ("k: %i, v: %s, i: %i" % (item._key, item._value, item._index))
            outstr += elt
            outstr += " --> \n"
        return outstr

    __repr__ = __str__

    def add(self, key, item):

        if len(self._heap) == 0:
            i = 0
        else:
            i = len(self._heap)
        elt = Element(key, item, i)
        self._heap.append(elt)
        if len(self._heap) > 1:
            self.bubbleUpHeapSort(elt)
        return elt

    def swap(self, element, other):

        i = element._index
        other_i = other._index
        self._heap[i] = other
        self._heap[other_i] = element
        element._index = other_i
        other._index = i

    def bubbleUpHeapSort(self, elt):

        parent_i = (elt._index-1)//2
        if parent_i >= 0 and parent_i < len(self._heap)-1:
            p = self._heap[parent_i]
            if elt._key < p._key:
                self.swap(elt, p)
                self.bubbleUpHeapSort(elt)
        return self._heap

    def bubbleDownHeapSort(self, elt):

        i = elt._index
        left = 2*i + 1
        right = 2*i +2
        if right < self.length():
            if self._heap[left] and self._heap[right]:
                if self._heap[left] < self._heap[right]:
                    if elt > self._heap[left]:
                        self.swap(elt, self._heap[left])
                        self.bubbleDownHeapSort(self._heap[left])
                elif self._heap[right] < self._heap[left]:
                    if elt > self._heap[right]:
                        self.swap(elt, self._heap[right])
                        self.bubbleDownHeapSort(self._heap[right])
        elif left < self.length():
            if elt > self._heap[left]:
                self.swap(elt, self._heap[left])
                self.bubbleDownHeapSort(self._heap[left])
        return self._heap

    def _min(self):

        return self._heap[0]._value

    def remove_min(self):

        elt = self._heap[0]
        if len(self._heap) == 1:
            self._heap.pop(0)
        else:
            self._heap[0] = self._heap[-1]
            self._heap[0]._index = 0
            self._heap.pop(-1)
            self.bubbleDownHeapSort(self._heap[0])
        return elt

    def is_empty(self):

        return self._heap == []

    def length(self):

        return len(self._heap)

    def update_key(self, element, new_key):

        element._key = new_key
        self.rebalance(element)
        
    def rebalance(self, elt):

        j = elt._index
        parent = (j-1)//2
        left = 2*j + 1
        if j <= len(self._heap)-1:
            if parent >= 0:
                if self._heap[j]._key < self._heap[parent]._key:
                    self.bubbleUpHeapSort(self._heap[j])
            elif left < len(self._heap): 
                self.bubbleDownHeapSort(self._heap[j])
        else:
            return self._heap
        
    def get_key(self, element):

        return self._heap[element._index]._key

    def remove(self, element):

        j = element._index
        last = len(self._heap)-1
        (self._heap[-1], self._heap[j]) = (self._heap[j], self._heap[-1])
        self._heap[j]._index = j
        self._heap.pop(-1)
        self.rebalance(self._heap[-1])
        
def test():

    heap = APQ()
    a = heap.add(3, 'animal')
    b = heap.add(1, 'cat')
    c = heap.add(2, 'dog')
    d = heap.add(12, 'shark')
    e = heap.add(34, 'snail')
    f = heap.add(71, 'fish')
    g = heap.add(0, 'goat')
    print(heap)
    heap.remove(a)
    heap.remove(b)
    h = heap.add(28, 'racoon')
    heap.update_key(e, 5)
    print(heap)
    print(heap.remove_min())
    print(heap)
    heap.remove(c)
    print(heap)
    print(heap._min())
