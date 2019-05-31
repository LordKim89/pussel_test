

class Level:
    
    def __init__(self, game_map, forms):
        self.game_map = game_map
        self.forms = forms
        self.active_form = None
        self.click_timer = 0
        self.map_x = 10
        self.map_y = 10
        self.id = -1

        self.map_width = 480
        self.map_height = 480
        
    def setID(self, id):
        self.id = id 
        
    def show(self):
        
        self.game_map.show(PVector(self.map_x,self.map_y), self.map_width, self.map_height)
        for f in self.forms:
            f.show()
        if not(self.active_form is None):
            self.active_form.show()  
            
        stroke(255)
        fill(255)
        textSize(24)
        text(self.id, 30, 40)     
        
            
    def setScale(self, tile_size_w, tile_size_h):
        self.tile_size_w = tile_size_w
        self.tile_size_h = tile_size_h
            
            
            
    def interact(self):
        
        self.game_map.deActivate()
        
        for f in self.forms:
            f.setScale(self.tile_size_w, self.tile_size_h)
        
        if mousePressed:
            if mouseButton == LEFT:
                if not (self.active_form is None):
                    if not self.active_form.locked:
        
                        self.active_form.pos = PVector(mouseX, mouseY)
                else:
                    for f in self.forms:
                        if f.clickedOn(PVector(mouseX, mouseY), self.tile_size_h, self.tile_size_w):
                            self.active_form = f
                    if self.active_form is None:
                        self.active_form = self.game_map.getForm(self.mouseToMapLocation(PVector(mouseX, mouseY)))
                        if not (self.active_form is None):
                            self.active_form.locked = False
            
            # if mouseButton == RIGHT and millis() - self.click_timer > 100:
            #     p = mouseToMapLocation(PVector(mouseX, mouseY))
            #     self.click_timer = millis()
            #     if not(p is None):
            #         if -1 in self.game_map.map_states[floor(p.y + p.x*self.game_map.w)].state_list:
            #             self.game_map.removeWall(p.x, p.y)            
            #         else:
            #             self.game_map.setWall(p.x, p.y)
        

    def mouseRotate(self, event):
        e = event.getCount()
    

    
        if not (self.active_form is None) and mousePressed:
            self.active_form.angle += PI/19.0*self.sign(e)
            self.active_form.angle = (self.active_form.angle+TWO_PI)%TWO_PI
            self.active_form.snapped = False
            if self.active_form.angle%HALF_PI < 0.12:
                
                if self.active_form.angle < HALF_PI*1.1 and self.active_form.angle > HALF_PI*0.9:
                    self.active_form.angle = HALF_PI
                    self.active_form.snapped = True
                if self.active_form.angle < PI*1.1 and self.active_form.angle > PI*0.9:
                    self.active_form.angle = PI
                    self.active_form.snapped = True
                if self.active_form.angle < 3*HALF_PI*1.1 and self.active_form.angle > 3*HALF_PI*0.9:
                    self.active_form.angle = 3*HALF_PI
                    self.active_form.snapped = True
                if self.active_form.angle < 0.3 and self.active_form.angle > -0.3:
                    self.active_form.angle = 0
                    self.active_form.snapped = True
            
    def sign(self, nr):
        if nr < 0:
            return -1
        else:
            return 1
        
        
    def mouseDropForm(self):

        if not (self.active_form is None):
            
            if self.active_form.snapped:
                map_locs = self.formToMapLocation(self.active_form)
                
                if self.game_map.addForm(self.active_form, map_locs):
                    self.active_form.locked = True
                    self.active_form = None
                    #pass
        self.active_form = None
        
        
        
    def formToMapLocation(self, form):
        map_locs = []
        global tile_size_x, tile_size_y
        
        if form.snapped:
            for t in form.tiles:
                pk = form.pos.copy()
                pk.add(PVector(form.shade_offset_x, form.shade_offset_y))
                p2 = t.pos.copy()
                p2.x *= self.tile_size_w
                p2.y *= self.tile_size_h
                p2.rotate(form.angle)
                pk = pk.add(p2)
                p = self.mouseToMapLocation(pk)
                map_locs.append(p)
        
        for k in map_locs:
            self.game_map.activateLocation(floor(k.x), floor(k.y))
        
        return map_locs
        
    
    def mouseToMapLocation(self, p1):
        mx = p1.x - self.map_x
        my = p1.y - self.map_y
        mxi = floor(map(mx, 0, self.map_width, 0, self.game_map.w))
        myi = floor(map(my, 0, self.map_height, 0, self.game_map.h)) 
        return PVector(mxi, myi)
    
    
    
    def isComplete(self):
        for f in self.forms:
            if not f.locked:
                return False
                
        any_empty = False    
        for x in range(self.game_map.w):
            for y in range(self.game_map.h):
                state = self.game_map.map_states[y + x*self.game_map.w].getTotalState()
                
                if len(state) == 1 and (0 in state):
                    return False
                
                if (7 in state):
                    return False

        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        