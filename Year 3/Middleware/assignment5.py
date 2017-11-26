#!/usr/bin/python

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self._threadID = threadID
        self._name = name
        self._q = q

    def run(self):
        print("Starting " + self._name)
        self._q._lock = True # lock mechanism set
        doWork(self._name, self._q) # thread has sole access to queue
        print("Exiting " + self._name)

def doWork(threadName, queue):
    while queue._lock != False:
        if not queue.is_empty():
            data = queue.dequeue()
            queue._lock = False # lock mechanism unset
            print("%s received data: '%s'" % (threadName, data))
        else:
            print("Queue is empty")
            queue._lock = False # lock mechanism unset
        time.sleep(1) # delay

class FIFOQueue:
    def __init__(self):
        self._body = [] # queue body
        self._head = 0 # queue head
        self._empty = True
        self._lock = False # lock set to True when queue in use

    def is_empty(self):
        # returns True or False
        if self.length() != 0:
            self._empty = False
        return self._empty

    def enqueue(self, message):
        # client can add message to queue
        print("Adding message '%s'" % (message))
        self._body.append(message)

    def dequeue(self):
        # client can remove message from queue
        if self.length == 0:
            return None
        message = self._body[self._head]
        self._body[self._head] = None
        self._head += 1
        return message

    def length(self):
        # returns length of queue
        print("Length: %i" % (len(self._body) - self._head))
        return len(self._body) - self._head

    def first(self):
        # returns top of queue
        if self.length == 0:
            return None
        return ("First: %s" % (self._body[self._head]))

def main():
    queue = FIFOQueue()
    queue.enqueue("Service failing")
    queue.enqueue("Disk error")
    queue.enqueue("load overbalanced")
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    threads = []
    threadID = 1
    # Intialises three threads with unique IDs and names
    for tName in threadList:
        thread = myThread(threadID, tName, queue)
        thread.start()
        threads.append(thread)
        threadID += 1

if __name__ == "__main__":
    main()