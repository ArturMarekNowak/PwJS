import threading
import time
import random

def printPhilosophersStates(n, philosophers, forks, exTime):

    for i in range(n):
        print("Philosopher: %s \t" % philosophers[i].getPhilosophersName(), end = "")
    
    for i in range(n - 1):
        print("Fork: %s \t" % forks[i].getForkName(), end = "")
    
    print("Fork: %s" % forks[i].getForkName())


    for i in range(exTime):
        for j in range(n):
            print("%s \t" % philosophers[j].getPhilosopherState(), end = "")
        
        for j in range(n - 1):
            print("%s \t" % forks[j].getForkStatus(), end = "")
        
        print("%s" % forks[n - 1].getForkStatus())
    
        time.sleep(1.0)
        
                
class Fork():

    def __init__(self, ID, state = "Free"):
        self.ID = ID
        self.status = "Free" 
 
    def getForkStatus(self):
        return self.status

    def getForkName(self):
        return self.ID
   
    def tryToTakeFork(self):
        if self.status != "Free":
            return 0
        else:
            self.status = "Taken"
            return 1 

    def releaseFork(self):
        self.status = "Free"
        return 1


class Philosopher(threading.Thread): 
    
    running = True

    def __init__(self, name, lFork, rFork, state = "Thinking"):
        threading.Thread.__init__(self)
        self.name = name
        self.leftFork = lFork
        self.rightFork = rFork
        self.state = state

    def getPhilosophersName(self):
        return self.name

    def getPhilosopherState(self):
        return self.state

    def run(self):        
        while self.running == True:
            time.sleep(random.uniform(3, 15))
            self.tryToEat()
    
    def tryToEat(self):
        rclf = self.leftFork.tryToTakeFork()
        rcrf = 0

        while self.running == True:
           
            
            if rclf == 0 and rcrf == 0:
                self.state = "l N/A \t" 
                rclf = self.leftFork.tryToTakeFork()

            elif rclf == 1 and rcrf == 0:
                self.state = "r N/A \t"
                rcrf = self.rightFork.tryToTakeFork()
                
            elif rclf == 1 and rcrf == 1:
                self.state = "Eating \t" 
                time.sleep(random.uniform(3, 8))
                self.rightFork.releaseFork()
                self.leftFork.releaseFork()
                self.state = "Thinking"
                break
        return 

 
def main():
    random.seed(292839)

    n = 5
    
    forks = [Fork(i) for i in range(n)]
    philosophers = [Philosopher(i, forks[i], forks[(i+1)%n]) for i in range(n)]
    
    Philosopher.running = True
    for i in range(n):
        philosophers[i].start()
 
    printPhilosophersStates(n, philosophers, forks, 150)   

    Philosopher.running = False

if __name__ == "__main__":
    main()            



