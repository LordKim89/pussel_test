

class Tile:
    
    def __init__(self, pos):
        self.pos = pos
        self.tile_size_w = 20
        self.tile_size_h = 20
        self.state_list = []
        #self.state_list.append(floor(random(3)+1))
        
        
        
    
    def show(self):
        translate(self.pos.x*self.tile_size_w , self.pos.y*self.tile_size_h)
 
        rectMode(CENTER)
        strokeWeight(2)
        stroke(0, 200)
        if (1 in self.state_list):
            fill(230, 50, 50, 200)
        if (2 in self.state_list):
            fill(50, 230, 50, 200)
        if (3 in self.state_list):
            fill(50, 50, 230, 200)
        rect( 0, 0, self.tile_size_w, self.tile_size_h)
        
        
        
    def showShadow(self):
       
        translate(self.pos.x*self.tile_size_w , self.pos.y*self.tile_size_h )

        rectMode(CENTER)    
        noStroke()
        fill(0, 80)
        rect( 0, 0, self.tile_size_w, self.tile_size_h)
        
    
    def showMap(self, pos):
        pushMatrix()
        translate(pos.x*self.tile_size_w , pos.y*self.tile_size_h )

        rectMode(CORNER)  
        stroke(0, 200)  
        fill(200,100,50, 250)
        rect( 0, 0, self.tile_size_w, self.tile_size_h)
        popMatrix()
        
    
    
    def setScale(self, sx, sy):
        self.tile_size_w = sx
        self.tile_size_h = sy
        
    def setState(self, nr):
        self.state = nr
        
    def nextState(self, nr):
        self.next_state = nr
        
    def update(self):
        self.state = self.next_state
        
        
        