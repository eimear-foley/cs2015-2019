class DLLNode:

    ### Representation of a doubly linked list node
    def __init__(self, block, prev, nextnode):
        self._next = nextnode # pointer to next node
        self._prev = prev # pointer to previous node
        self._block = block # block object

class FreeMemory:

    ### Representation of Free Memory as a doubly linked list
    def __init__(self):
        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, self._head, None)
        self._head._next = self._tail
        self._size = 0
        self._first = None
        self._last = None

    # adds first item to linked list
    def add_first(self, item):
        node = DLLNode(item, self._head, self._tail)
        self._first = node
        self._last = node
        self._size += 1

    # adds item to end of linked list
    def add_last(self, item):
        if self._first == None:
            self.add_first(item)
        else:
            newnode = DLLNode(item, None, self._tail)
            self._last._next = newnode
            newnode._prev = self._last
            self._last = newnode
        self._size += 1

    # removes node from linked list
    def remove_node(self, node):
        before = node._prev
        after = node._next
        before._next = after
        after._prev = before
        self._size -= 1
        node = DLLNode(None, None, None)

class Block:

    ### Representation of Block
    def __init__(self, num_of_pages):
        self._pages = num_of_pages # size of block given by the number of pages
        self._free = True # if block available for allocation
        
class MainMemory:
    ### Representation of the main memory
    def __init__(self, free_memory, page_replacement):
        self._memory = free_memory
        self._queue = page_replacement
        self._processes = {} # dictionary containing (process_id, request) pairs

    def addProcessRequest(self, process_id, request):
        self._processes[process_id] = request

    def merge(self, blocks, pages, process_id):
        for block in blocks:
            self._memory.remove_node(block) # remove blocks from free memory
        new_block = Block(pages) # merge pages from deleted blocks to create new block
        new_block._free = False
        self._memory.add_last(new_block) # add to free memory
        self._processes = {k:v for k,v in self._processes.items() if k != process_id}
        # run process now that memory request satisfied
        self.runProcess(process_id, new_block)

    def runProcess(self, process_id, block):
        self._queue.addPageReplacementQueue(block)
        print("Request successful. Process %i running in main memory." % process_id)
        return

    def checkMemory(self):

        # Check for memory for each process with FIFO strategy
        for process_id in self._processes:
            print("Searching for memory for process %i" % process_id)
            block = self._memory._first
            request = self._processes[process_id]
            print("requested pages: %i" % request)
            if request > 1024:
                self._processes = {k:v for k,v in self._processes.items() if k != process_id}
                print("Process request greater than size of main memory.")
                return
            # find available memory for process request
            while block._next:
                if block._block._free:
                    if block._block._pages >= request:
                        self.runProcess(process_id, block)
                        block._block._free = False
                        self._processes = {k:v for k,v in self._processes.items() if k != process_id}
                        break
                block = block._next
                if block._next == None:
                    # if no available memory check page replacement queue
                    (blocks, pages) = self._queue.findPages(process_id, request) 
                    self.merge(blocks, pages, process_id)
                    # merge blocks found from page replacement queue

class PageReplacementQueue:

    ### Representation of Page Replacement Queue using FIFO policy
    def __init__(self):
        self.body = []
        self.head = 0    #index of first element, unless empty, and then 0 by default
        self.tail = 0    #index of free cell for next element
        self.size = 0    #number of elements in the queue

    # Queues pages/blocks to Page Replacement Queue
    def addPageReplacementQueue(self, block):
        if self.size == 0:
            self.body.append(block)      #assumes an empty queue has head at 0
            self.size = 1
            self.tail = 1
        else:
            self.body.append(block)
            self.size += 1

    # Dequeues pages from the Page Replacement Queue
    def dequeue(self):
        if self.size == 0:     #empty queue
            print("No pages to replace with.")
            return 
        block = self.body[self.head]
        self.body[self.head] = None
        if self.size == 1:                #just removed last element, so rebalance
            self.head = 0
            self.tail = 0
            self.size = 0
        elif self.head == len(self.body) - 1:  #if the head was the end of the list
            self.head = 0                 #we must have wrapped round, so point to start
            self.size = self.size - 1
        else:            
            self.head = self.head + 1          #just move the pointer on one cell
            self.size = self.size - 1
        #we haven't changed the tail, so nothing to do
        return block

    # Finds pages for process request
    def findPages(self, process_id, request):

        if self.size == 0:     #empty queue
            print("No pages to replace with.")
            return
        block = self.body[self.head]
        pages = block._block._pages
        required = [block] # list containing blocks to be merged to satisfy memory request
        i = 0
        print("Searching page replacement queue.")
        while i < len(self.body) and pages < request:
            block = self.body[i]
            required += [block] 
            pages += block._block._pages
            i += 1
        for _ in range(len(required)):
            self.dequeue() # dequeue required blocks from page replacement queue
        print("Pages replacement successful.")
        if len(required) > 1:
            return required, pages
        return

def Kernel(main):

    while len(main._processes) != 0:
        main.checkMemory()

def test():

    memory = FreeMemory()
    page_replacement = PageReplacementQueue()
    block1 = Block(2)
    memory.add_first(block1)
    block2 = Block(2)
    memory.add_last(block2)
    block3 = Block(4)
    memory.add_last(block3)
    block4 = Block(8)
    memory.add_last(block4)
    block5 = Block(16)
    memory.add_last(block5)
    block6 = Block(32)
    memory.add_last(block6)
    block7 = Block(64)
    memory.add_last(block7)
    block8 = Block(128)
    memory.add_last(block8)
    block9 = Block(256)
    memory.add_last(block9)
    block10 = Block(512)
    memory.add_last(block10)
    main = MainMemory(memory, page_replacement)
    main.addProcessRequest(1, 5)
    main.addProcessRequest(2, 102)
    main.addProcessRequest(3, 512)
    main.addProcessRequest(4, 2)
    main.addProcessRequest(5, 2)
    main.addProcessRequest(6, 301)
    main.addProcessRequest(7, 3001)
    Kernel(main)
