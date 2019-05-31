
class Form:
    
    def __init__(self, tiles, pos):
        
        self.tiles = tiles
        self.pos = pos
        self.mid = self.midPoint()
        self.translateToMidpoint()
        self.angle = 0
        
        self.shade_offset_x = 4
        self.shade_offset_y = -4
        
        self.locked = False
        self.snapped = True
        
        self.posL = None
        
        
   
   
    # Midpoint only used for rotation and tying to mouse.
    # rotate around mousePoint?
    def midPoint(self):
        if len(self.tiles) > 0:
            x = 0
            y = 0
            for t in self.tiles:
                x += t.pos.x
                y += t.pos.y
            p = PVector(x/len(self.tiles), y/len(self.tiles))
            #p = p.sub(self.pos)
            return p
        return null
    
    
    

    def setStateAll(self, state):
        for t in self.tiles:
            t.state_list.append(state)
        
        
        
    def setScale(self,sx, sy):
        for t in self.tiles:
            t.setScale(sx, sy)
    
    
    def show(self):
        
        if not self.locked:
            pushMatrix()
            translate(self.pos.x, self.pos.y)
            
            #scale(20)
            for t in self.tiles:
                pushMatrix()
                translate(self.shade_offset_x, self.shade_offset_y)
                rotate(self.angle)
                
                t.showShadow()
                popMatrix()
                
            rotate(self.angle)
            for t in self.tiles:
                pushMatrix()
                t.show()
                popMatrix()
                
            popMatrix()
        
        
        
    def translateToMidpoint(self):
        for t in self.tiles:
            t.pos.sub(self.mid)
    
    
    
    def clickedOn(self, m, xl, yl):
        if not self.locked:
            l = dist(self.pos.x, self.pos.y, m.x, m.y)
            if l < dist(xl, yl,0,0)*1:
                return True
        return False
        
        
        
        

class Boundary:
    
    def __init__(self, parent):
        self.parent = parent
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        