
from map_tile import MapTile

class Map:
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.map_tiles = []
        self.map_states = []
        for x in range(self.w):
            for y in range(self.h):
                mt = MapTile(PVector(x,y))
                self.map_tiles.append(mt)
                sl = StateList()
                self.map_states.append(sl)
                
               # r = noise(x*0.6, y*0.6)*0.7 +  1 - dist(self.w/2, self.h/2,x,y)/5
               # if r < 0.5:
               #     self.setWall(x,y)
        
        
        
        self.forms = []
        self.form_locs = []
    
        
        
    
    def setWall(self, x, y):
        self.map_states[floor(y + x*self.w)].addState([-1])
        
    def removeWall(self, x, y):
        self.map_states[floor(y + x*self.w)].removeForm([-1])
    
    
    
    
    def show(self, pos, w, h):
        
        pushMatrix()
        translate(pos.x, pos.y)
        tile_size_w = w/self.w
        tile_size_h = h/self.h
        i = 0
        for t in self.map_tiles:
            pushMatrix()
            t.setScale(tile_size_w, tile_size_h)
            t.show(self.map_states[i].getTotalState())
            popMatrix()
            i += 1
        
        popMatrix()
        
        # pushMatrix()
        # translate(pos.x, pos.y)

        # for f in self.forms:

        #     for n in range(len(f.tiles)):
        #         t = f.tiles[n]
        #         pos = f.posL.pos_list[n]
        #         t.showMap(pos)
        # popMatrix()
        
    
    
    
    
    def activateLocation(self, x, y):
        if x >= 0 and x < self.w and y >= 0 and y < self.h:
            i = y + x*self.w
            self.map_tiles[i].setActive(True)
            
            
            
            
            
    def deActivate(self):
        for t in self.map_tiles:
            t.setActive(False)
            
            
            
    
    def addForm(self, form, pos_list):
        posL = PosList(pos_list)
        for p in pos_list:
            if p.x >= 0 and p.x < self.w and p.y >= 0 and p.y < self.w:
                pass
            else:
                return False
        
        if not (form in self.forms):
            
            i = 0
            for p in posL.pos_list:
                ts = self.map_states[floor(p.y + p.x*self.w)].getTotalState()
                #println(ts)
                if not (7 in ts):
                    for s in form.tiles[i].state_list:
                        if (s in ts):
                            return False
                    i += 1
                    
                    if (-1 in ts):
                        return False
            
            i = 0
            #println(" ")
            for p in posL.pos_list:
                self.map_states[floor(p.y + p.x*self.w)].addState(form.tiles[i].state_list)
                i += 1
            form.posL = posL
            self.forms.append(form)
            
            
            #self.form_locs.append(posL)
            return True
        
        return False
        
        
    def getForm(self, pos):
        i = 0
        found = False
        
        
        for fo in self.forms:
            
            if found:
                break
            for p in fo.posL.pos_list:
                if found:
                    break
                if p.equals(pos):
                    
                    f = fo
                    found = True

            
        if found:
            
            i = 0
            for p in f.posL.pos_list:
                self.map_states[floor(p.y + p.x*self.w)].removeForm(f.tiles[i].state_list)
                i += 1
            
            self.forms.remove(f)
            f.posL = None
            
            return f
        
        return None
            

class PosList:
    
    def __init__(self, pos_list):
        self.pos_list = pos_list
        
    def equals(self, p):
        for p1 in self.pos_list:
            for p2 in p:
                if not(p1.equals(p2)):
                    return False
        return true
    





class StateList:
    
    def __init__(self,):
        self.state_list = []
        self.state_list.append(0)
        
    
    def removeForm(self, sl):
        #println(sl)
        for s in sl:
            nr = 0
            if s in self.state_list :
                nr += 1            
                self.state_list.remove(s)

                
        
        
    def addState(self, state):
        for s in state:
       
            self.state_list.append(s)
        
        #println(self.state_list)
            
    
# -1 = wall
# 0 = empty
# 1 = red
# 2 = green
# 3 = blue
# 4 = cyan
# 5 = yellow
# 6 = magenta
# 7 = white
    def getTotalState(self):
        temp_states = []
        for k in self.state_list:
            temp_states.append(k)
        current_states = []
        
        
        

        reduced = False
        while not reduced:

            
            if  (1 in temp_states) and (2 in temp_states) and (3 in temp_states): 
                current_states.append(7)
                current_states.append(1)
                current_states.append(2)
                current_states.append(3)
                temp_states.remove(1)
                temp_states.remove(2)
                temp_states.remove(3)
            else:
                if ((2 in temp_states) and (3 in temp_states)) or ((1 in temp_states) and (3 in temp_states)) or ((1 in temp_states) and (2 in temp_states)): 
                    if  (2 in temp_states) and (3 in temp_states):
                        current_states.append(4)
                        current_states.append(2)
                        current_states.append(3)
                        temp_states.remove(2)
                        temp_states.remove(3)
                    
                    if  (1 in temp_states) and (3 in temp_states):
                        current_states.append(6)
                        current_states.append(1)
                        current_states.append(3)
                        temp_states.remove(1)
                        temp_states.remove(3)
                        
                    if  (1 in temp_states) and (2 in temp_states):
                        current_states.append(5)
                        current_states.append(1)
                        current_states.append(2)
                        temp_states.remove(1)
                        temp_states.remove(2)
                else:
                
                    if (1 in temp_states):
                        temp_states.remove(1)
                        current_states.append(1)
                        
                    if (2 in temp_states):
                        temp_states.remove(2)
                        current_states.append(2)
                        
                    if (3 in temp_states):
                        temp_states.remove(3)
                        current_states.append(3)
                    
            if (-1 in temp_states):
                temp_states.remove(-1)
                current_states.append(-1)
                
            if (0 in temp_states):
                temp_states.remove(0)
                current_states.append(0)
                

                
            if  len(temp_states) == 0:
                
                reduced = True
            else:
                #println("double_state")
                current_states = []
            
      
        
        
        return current_states
        
        
    
    
    
    
    
    
    
    
    
    
    
    
        