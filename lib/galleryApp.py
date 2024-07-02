from application import App
from bitmap import Bitmap
from keyInput import KeyInput

class Gallery(App):
    def __init__(self):
        super().__init__("Gallery")
        
        self.imagePath = "images/"
        self.images = ['main.bmp']
        self.index = 0
        
        self.bmp = Bitmap()
        self.keyInput = KeyInput()
    
    def init(self):
        image = self.bmp.get_bitmap(self.imagePath+self.images[self.index])
        self.screen.append(image)
        
    
    def update(self):
        if self.keyInput.isPressedKey("B"):
            self.screen.pop()
            self.index += 1
            if(self.index >= len(self.images)):
                self.index = 0
            
            image = self.bmp.get_bitmap(self.imagePath+self.images[self.index])
            self.screen.append(image)
            
        if self.keyInput.isPressedKey("A"):
            self.screen.pop()
            self.index -= 1
            if(self.index < 0):
                self.index = len(self.images) - 1
    
            image = self.bmp.get_bitmap(self.imagePath+self.images[self.index])
            self.screen.append(image)
        
        if self.keyInput.isPressedKey("X"):
            self.close()
