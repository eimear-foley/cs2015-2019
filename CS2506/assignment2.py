### Eimear Foley 115352866

class Process:
    def __init__(self, quanta, event, state, _id, priority):
        # Initializes process variables 
        self._quanta = quanta
        self._event = event # If I/O operation required or not
        self._state = state
        self._id = _id
        self._priority = priority
        
class CPU:
    def __init__(self):
        self._curprocess = None
        self._activequeue = None
        self._queues = [[],[],[],[],[],[],[],[]] # multilevel feedback queues
        self._blockedqueue = []

    def addProcess(self, process):

        # calculate which queue process is added to according to priority
        base = 4
        index = (process._priority - base) // 2
        self._queues[index].append(process)

    def addBlockedProcess(self, process):
        self._blockedqueue.append(process)

    def completeIO(self, process):
        process = self._blockedqueue[0]
        process._state = 'ready'
        process._event = False
        if process._priority != 4:
            process._priority -= 2
        self.addProcess(process)

    def addReadyProcess(self, process):
        self.completeIO(process)

    def checkQueues(self):
        # check if all process complete or not
        terminated = True
        for queue in self._queues:
            if queue != []:
                terminated = False
        return terminated

    def runProcess(self):

        index = 0
        while index < 8:
            # reset the active queue after each time slice is completed
            self._activequeue = self._queues[index]
            # check if current active queue has a process
            while self._activequeue == []:
                if index == 7:
                    index = 0
                else:
                    index += 1
                self._activequeue = self._queues[index]
                
            # set current process to top of active queue
            self._curprocess = self._activequeue[0]
            print("Running process - Process ID:%i, priority: %i, quanta: %i" %
                  (self._curprocess._id, self._curprocess._priority, self._curprocess._quanta))
            
            # check if process life cycle complete
            if self._curprocess._quanta == 0:
                print("Process ID:%i completed" % self._curprocess._id)
                self._activequeue.pop(0) # remove from ready queue

            # check if process requires I/O operation
            elif self._curprocess._event != False:
                print("Process ID:%i sent to blocked queue." % self._curprocess._id)
                # decrement process's number of quanta
                self._curprocess._quanta -= 1
                self.addBlockedProcess(self._curprocess) # add to blockedQueue
                self._activequeue.pop(0) # remove from readyQueue
            else:
                # decrement process's number of quanta
                self._curprocess._quanta -= 1
                # return process to end of readyQueue when quanta finished 
                self.addProcess(self._curprocess)
                self._activequeue.pop(0) # remove from top of readyQueue
     
                # check if blockedQueue is empty
                if self._blockedqueue != []: 
                    self._blockedqueue[0]._state = "ready"
                    # send process at top of blockedQueue to the readyQueue
                    self.addReadyProcess(self._blockedqueue[0]) 
                    print("Process ID:%i returned to ready state" % self._blockedqueue[0]._id)
                    self._blockedqueue.pop(0)
     
            # if all queues are empty - processes completed
            terminated = self.checkQueues()
            if terminated:
                print("All processes comleted. CPU now idle.")
                return

            if index == 7:
                index = 0
            else:
                index += 1
                
def Schedule(CPU):

    CPU.runProcess() # CPU runs processes while all queues are not empty

def test():

    cpu = CPU()
    p1 = Process(2, False, 'ready', 1, 4)
    cpu.addProcess(p1)
    p2 = Process(7, True, 'ready', 2, 6)
    cpu.addProcess(p2)
    p3 = Process(3, False, 'ready', 3, 16)
    cpu.addProcess(p3)
    p4 = Process(1, True, 'ready', 4, 10)
    cpu.addProcess(p4)
    p5 = Process(2, False, 'ready', 5, 18)
    cpu.addProcess(p5)
    p6 = Process(5, False, 'ready', 6, 8)
    cpu.addProcess(p6)
    Schedule(cpu)
    
