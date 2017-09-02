### Eimear Foley 115352866
 
class Process:
    def __init__(self, quanta, event, state, _id):
        # Initializes process variables 
        self._quanta = quanta
        self._event = event # If I/O operation required or not
        self._state = state
        self._id = _id
  
class CPU:
    def __init__(self):
        self._currentprocess = None
        self._readyQueue = []
        self._blockedQueue = []
               
    def runProcess(self):
 
        # set current process running in CPU to top of readyQueue
        self._currentprocess = self._readyQueue[0]
        print("Running process - Process ID:%i" % self._currentprocess._id)
 
        # decrement process's number of quanta
        self._currentprocess._quanta -= 1
 
        # check if process life cycle complete
        if self._currentprocess._quanta == 0:
            self._readyQueue.pop(0) # remove from ready queue
 
        # check if process requires I/O operation
        elif self._currentprocess._event != False:
            print("Process ID:%i sent to blocked queue." % self._currentprocess._id)
            self.addBlockedProcess(self._currentprocess) # add to blockedQueue
            self._readyQueue.pop(0) # remove from readyQueue
        else:
            # return process to end of readyQueue when quanta finished 
            self.addReadyProcess(self._currentprocess)
            self._readyQueue.pop(0) # remove from top of readyQueue
 
            # check if blockedQueue is empty
            if self._blockedQueue != []: 
                self._blockedQueue[0]._state = "ready"
                # send process at top of blockedQueue to the readyQueue
                self.addReadyProcess(self._blockedQueue[0]) 
                print("Process ID:%i returned to ready queue" % self._blockedQueue[0]._id)
                self._blockedQueue.pop(0)
 
        # if readyQueue and blockedQueue are empty - processes completed
        if self._readyQueue == [] and self._blockedQueue == []:
            print("All processes comleted.")
            return
 
    def addProcess(self, process):
        if process._state == "ready":
            self.addReadyProcess(process)
        else:
            self.addBlockedProcess(process)
             
    def addReadyProcess(self, process):
        self._readyQueue.append(process)
 
    def addBlockedProcess(self, process):
        self._blockedQueue.append(process)
         
  
def Schedule(CPU):
    while CPU._readyQueue != []:
        CPU.runProcess()       
 
def test():
    cpu = CPU()
    process1 = Process(5, False, "ready",1)
    cpu.addProcess(process1)
    process2 = Process(2, False, "ready",3)
    cpu.addProcess(process2)
    process3 = Process(10, False, "ready",2)
    cpu.addProcess(process3)
    process4 = Process(2, True, "blocked", 4)
    cpu.addProcess(process4)
    Schedule(cpu)
