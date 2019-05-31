

# -1 = wall
# 0 = empty
# 1 = red
# 2 = green
# 3 = blue
# 4 = cyan
# 5 = yellow
# 6 = magenta
# 7 = white


from tile import Tile
from form import Form
from mapper import Map
from loader import MapLoader
from level import Level




forms = []

loader = MapLoader()

levels = []

current_level_index = 0

def setup():
    size(700,500)
    
   # createForms()
    
    global levels, key_timer, mouse_timer
    #game_map = Map(nr_tiles_x, nr_tiles_y)
    #click_timer = 0
    
    level = loader.loadLevel("/data/01/01")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The first Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/02")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The second Level")
    level.forms[0].angle = PI
    levels.append(level)
    
    level = loader.loadLevel("/data/01/03")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The third Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/04")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The fourth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/05")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The fifth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/06")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The sixth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/07")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The seventh Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/08")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The eighth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/09")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The nineth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/10")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The tenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/11")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The eleventh Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/12")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The twelveth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/13")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The thirteenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/14")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The fourteenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/15")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The fifteenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/16")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The sixteenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/17")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The seventeenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/18")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The eighteenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/19")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The nineteenth Level")
    levels.append(level)
    
    level = loader.loadLevel("/data/01/20")
    tile_size_w = (height-20)/(level.game_map.w)
    tile_size_h = (height-20)/(level.game_map.h)
    level.setScale(tile_size_w, tile_size_h)
    level.setID("The twentieth Level")
    levels.append(level)

    key_timer = 0
    mouse_timer = 0



def draw():

    background(234)

    global levels, current_level_index, key_timer, mouse_timer
    levels[current_level_index].interact()
    levels[current_level_index].show()
    
    if levels[current_level_index].isComplete():
        next_level_active = True
    else:
        next_level_active = False
        

    if current_level_index == 0:
        prev_level_active = False
    else:
        prev_level_active = True
        
    if next_level_active:
        fill(100,200,50)
    else:
        fill(50,100,25)
    rectMode(CORNER)
    rect(width-100, height-50, 80, 30)
    fill(0)
    text("NEXT", width-90, height-25)
    
    if prev_level_active:
        fill(100,200,50)
    else:
        fill(50,100,25)
    rectMode(CORNER)
    rect(width-190, height-50, 80, 30)
    fill(0)
    text("PREV", width-180, height-25)

    
    if mousePressed and millis() - mouse_timer > 200:
        mouse_timer = millis()
        x = mouseX
        y = mouseY
        # prev
        if x < width - 110 and x > width-190 and y < height-20 and y > height-50:
            current_level_index -= 1
        
        # next     
        if x < width - 20 and x > width-100 and y < height-20 and y > height-50:
            current_level_index += 1
    
    if keyPressed and millis() - key_timer > 300:
        key_timer = millis()
        if keyCode == LEFT:
            current_level_index -= 1
        if keyCode == RIGHT:
            current_level_index += 1
    current_level_index = (current_level_index+len(levels))%len(levels)
            
      

def mouseDragged():
    pass

def mouseReleased():
    
    levels[current_level_index].mouseDropForm()



def mouseWheel(event):
    levels[current_level_index].mouseRotate(event)
    














           
        
        

            
    
    
    
    
    
    
    
    