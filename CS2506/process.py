class Process:
    def __init__(self, quanta, event, state, _id):
        self._quanta = quanta
        self._event = event
        self._state = state
        self._id = _id

    if self._state == 'ready':
        addReadyProcess(self)
    elif self._state == 'blocked':
        addBlockedProcess(self)
        
    def __str__(self):

        return("Process- quanta: %i, event: %s, state: %s, ID: %i" % (self._quanta, self._event, self._state, self._id))

class BlockedQueue:
    def __init__(self):
        self._body = []

    def addBlockedProcess(self, process):
        self._body += [process]

    def dequeueBlockedProcess(self):
        if len(self._body) == 0:
            print("No process in blocked queue")
        else:
            self.completeIO()
            
    def completeIO(self):
        self._body[0]._event = False
        self._body[0]._state = 'ready'
        print("Process %i completed I/O event; added to readyQueue" % self._body[0]._id)
        process = self._body[0]
        self._body.pop(0)
        addReadyProcess(process)

class ReadyQueue:
    def __init__(self):
        self._body = []

    def addReadyProcess(self, process):
        if process._state == 'ready':
            self._body += [process]

    def sendProcess(self):
        process = self._body[0]
        if process._state == 'ready':
            # send to CPU

class CPU:
    def __init__(self):
        self._currentprocess = None

    def checkProcess():
        if self._currentprocess._event:
            self._currentprocess._state = 'blocked'
            return addBlockedProcess(self._currentprocess)
            
    def runProcess(self):
        self.checkProcess()
        self._currentprocess._quanta -= 1
        dequeueBlockedProcess()
        if self._currentprocess._quanta == 0:
            # remove process from cycle
        sendProcess()

class Schedule:
    def __init__(self):
