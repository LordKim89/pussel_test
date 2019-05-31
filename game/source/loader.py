

from mapper import Map
from tile import Tile
from map_tile import MapTile
from form import Form
from level import Level

# load a map plus a tile-set
# 1 file for the map, 1 tile for the forms.


class MapLoader:
    
    def __init__(self):
        pass
        
    
    def loadLevel(self, src):
        map_src = src + "/map.png"
        tiles_src = src + "/tiles.png"
        
        game_map = self.loadMap(map_src)
        forms = self.loadForms(tiles_src)
        
        level = Level(game_map, forms)
        
        return level
        
        
        
    def loadMap(self, src):
        #println(src)
        mi = loadImage(src)
        game_map = Map(mi.width, mi.height)
        for x in range(mi.width):
            for y in range(mi.height):
                if mi.get(x,y) == color(0):
                    game_map.setWall(x,y)
        return game_map
        
    
    def loadForms(self, src):
        mi = loadImage(src)
        
        start_pos = []
        start_c = []
        forms = []
        
        #start_c = color(0)
        #start_p = PVector(0,0)
        for x in range(mi.width):
            for y in range(mi.height):
                if not (mi.get(x,y) == color(0) or mi.get(x,y) == color(255)):
                    start_pos.append(PVector(x,y))
                    start_c.append(mi.get(x,y))

        
        
        for k in range(len(start_pos)):
            tiles = []
            self.floodFill(mi, tiles, floor(start_pos[k].x), floor(start_pos[k].y), start_c[k])
            form = Form(tiles, PVector(575 + random(-50, 25),height/2 + height/(len(start_pos)+3)*(k - len(start_pos)/2 )))
            if start_c[k] == color(255,0,0):
                form.setStateAll(1)
            if start_c[k] == color(0,255,0):
                form.setStateAll(2)
            if start_c[k] == color(0,0,255):
                form.setStateAll(3)
                
            form.angle = floor(random(4)+1)*HALF_PI
            forms.append(form)
        return forms
                    
        
        
    def floodFill(self,img, tiles, x, y, c):
    
        if x < 0 or x >= img.width or y < 0 or y >= img.height:
            pass
        else:
    
            t = Tile(PVector(x,y))
            for tl in tiles:
                if tl.pos.equals(t.pos):
                    return None
            
            if img.get(x,y) == color(255) or img.get(x,y) == c:
                tiles.append(t)
                        
                self.floodFill(img, tiles, x+1, y, c)
                self.floodFill(img, tiles, x-1, y, c)
                self.floodFill(img, tiles, x, y+1, c)
                self.floodFill(img, tiles, x, y-1, c)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
       