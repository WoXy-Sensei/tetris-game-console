import time
import displayio

class App:
    def __init__(self,name):
        self.screen = displayio.Group()
        self.name = name
        self.started = False
        self.closed = True
        
    def init(self):
        print(f"{self.name} inited")
    
    def start(self):
        self.init()
        self.started = True
        self.closed = False
        print(f"{self.name} started")
        time.sleep(1)
        while True:
            if self.closed == True:
                break
            self.update()
            time.sleep(0.1)
   
    def update(self):
        pass
    
    def close(self):
        self.started = False
        self.closed = True
        print(f"{self.name} closed")