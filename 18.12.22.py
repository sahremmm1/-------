from random import randint
class Camera:

    def __init__(self, name_: str):
        self.name = name_ 
        self.kolvo = 0   

    
    def kolizestvo(self, kolvo_: int):
        self.kolvo += kolvo_
  
    def info(self):
        print(f"{self.name}: {self.kolvo} фотографии")

camera = Camera("Canon 2323")

camera.kolizestvo(3)
camera.info()




