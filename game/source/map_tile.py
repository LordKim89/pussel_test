


class MapTile:
    
    def __init__(self, pos):
        self.pos = pos
        self.tile_size_w = 20
        self.tile_size_h = 20
        self.active = False
        
        self.forms = []
        
        
        
    
    def show(self, sl):
        translate(self.pos.x*self.tile_size_w, self.pos.y*self.tile_size_h)
        rectMode(CORNER)
        strokeWeight(1)
        
        # if self.active:
        #     stroke(0, 150)
        #     fill(200, 150, 100, 100)
        # else:
        stroke(0, 30)
        
        if -1 in sl:
            fill(20, 20, 20, 255)
        else:
            if 7 in sl:
                fill(200, 200)
            else:
                if (6 in sl) or (5 in sl) or (4 in sl):
                    if 6 in sl:
                        fill(200,30,200,200)
                    if 5 in sl:
                        fill(200,200,30,200)
                    if 4 in sl:
                        fill(30,200,200,200)
                else:
                    if (1 in sl) or (2 in sl) or (3 in sl):
                        if 1 in sl:
                            fill(200,30,30,200)
                        if 2 in sl:
                            fill(30,200,30,200)
                        if 3 in sl:
                            fill(30,30,200,200)
                    else:
                        if 0 in sl:
                            fill(200,200,200,200)
                        
        
        
        rect( 0, 0, self.tile_size_w, self.tile_size_h)
        
        
        
    
    def setScale(self, sx, sy):
        self.tile_size_w = sx
        self.tile_size_h = sy
        
         
    
    
    def setActive(self, b):
        self.active = b
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        