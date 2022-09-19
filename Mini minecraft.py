from pygments import highlight
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#punch_sound = Audio('ani/sfx-punch',loop = True,autoplay = False)

class Voxel(Button):
    def __init__(self,position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = "green",
            color = color.white           
            )

        
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':                                                    
                voxel = Voxel(position = self.position + mouse.normal)
            
            if key == 'right mouse down':
                destroy(self)
'''class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = 'white_sphere',
            color = color.black,
            scale = 150,
            double_sided = True     

        )'''
app = Ursina()        
for z in range(40):
    for x in range(40):
        voxel = Voxel(position = ((x,0,z)))

player = FirstPersonController()  
Sky()
app.run()