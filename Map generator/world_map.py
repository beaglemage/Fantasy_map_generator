from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time

"""
Created by Jay Collins 2020
Licensed under Creative Commons 0. Anyone is free to modify or use for any legal purpose.
"""

im_width = 4000


names_used = [""]

def name_taken(place_name):
        # See if a place was already given the same name.
        taken = False
        for i in names_used:
            if i == place_name:
                taken = True
        return taken

def place_city_name(colors, x,y):
    def get_city_name():
        name = ""
        while name_taken(name):
            start = ""
            n = np.random.randint(26)
            if n < 1:
                start = "Bone"
            elif n < 2:
                start = "Ham"
            elif n < 3:
                start = "Ale"
            elif n < 4:
                start = "Black"
            elif n < 5:
                start = "Gray"
            elif n < 6:
                start = "Marth"
            elif n < 7:
                start = "Lyn"
            elif n < 8:
                start = "Bellow"
            elif n < 9:
                start = "Gresh"
            elif n < 10:
                start = "Slips"
            elif n < 11:
                start = "Sun"
            elif n < 12:
                start = "Bith"
            elif n < 13:
                start = "Deep"
            elif n < 14:
                start = "Mead"
            elif n < 15:
                start = "Del"
            elif n < 16:
                start = "Gold"
            elif n < 17:
                start = "Ost"
            elif n < 18:
                start = "Shadow"
            elif n < 19:
                start = "Way"
            elif n < 20:
                start = "Marrow"
            elif n < 21:
                start = "Ice"
            elif n < 22:
                start = "Swin"
            elif n < 23:
                start = "Squal"
            elif n < 24:
                start = "Wolf"
            elif n < 25:
                start = "Lesh"
            elif n < 26:
                start = "Rust"
            end = ""
            n = np.random.randint(25)
            if n < 1:
                end = "hold"
            elif n < 2:
                end = "helm"
            elif n < 3:
                end = "spire"
            elif n < 4:
                end = "gar"
            elif n < 5:
                end = "den"
            elif n < 6:
                end = "fall"
            elif n < 7:
                end = "dor"
            elif n < 8:
                end = "dragon"
            elif n < 9:
                end = "haven"
            elif n < 10:
                end = "ridge"
            elif n < 11:
                end = "hall"
            elif n < 12:
                end = "keep"
            elif n < 13:
                end = "ston"
            elif n < 14:
                end = "gate"
            elif n < 15:
                end = "thorpe"
            elif n < 16:
                end = "shield"
            elif n < 17:
                end = "well"
            elif n < 18:
                end = "wright"
            elif n < 19:
                end = "crest"
            elif n < 20:
                end = "var"
            elif n < 21:
                end = "por"
            elif n < 22:
                end = "smog"
            elif n < 23:
                end = "blade"
            elif n < 24:
                end = "blaze"
            elif n < 25:
                end = "cheese"
            name = start + end
        names_used.append(name)
        img = Image.new('RGB', (200, 30), color = (0,0,0))
        fnt = ImageFont.truetype('akaPotsley.ttf', 28)
        d = ImageDraw.Draw(img)
        d.text((0,0), name, font=fnt, fill=(255,255,255))
        img.save('town_name.png')
        name_im = Image.open("town_name.png")
        return name_im.load()
    name = get_city_name()
    for i in range(x-70, x+130):
        for j in range(y+10, y+40):
            if name[i-x+70, j-y-10][0] > 10:
                colors[i,j] = name[i-x+70, j-y-10]
    return colors

def place_town_name(colors, x,y):
    def get_town_name():
        name = ""
        while name_taken(name):
            start = ""
            n = np.random.randint(25)
            if n < 1:
                start = "Blort"
            elif n < 2:
                start = "Oak"
            elif n < 3:
                start = "Fiz"
            elif n < 4:
                start = "Horn"
            elif n < 5:
                start = "Dun"
            elif n < 6:
                start = "Om"
            elif n < 7:
                start = "Sil"
            elif n < 8:
                start = "Iron"
            elif n < 9:
                start = "Leaf"
            elif n < 10:
                start = "Silver"
            elif n < 11:
                start = "Rork"
            elif n < 12:
                start = "Salt"
            elif n < 12:
                start = "Bell"
            elif n < 13:
                start = "Cir"
            elif n < 14:
                start = "Jar"
            elif n < 15:
                start = "Wim"
            elif n < 16:
                start = "Roth"
            elif n < 17:
                start = "Moose"
            elif n < 18:
                start = "Moss"
            elif n < 19:
                start = "Nan"
            elif n < 20:
                start = "Turn"
            elif n < 21:
                start = "Skar"
            elif n < 22:
                start = "Brae"
            elif n < 23:
                start = "Wind"
            elif n < 24:
                start = "Fin"
            elif n < 25:
                start = "Ost"
            end = ""
            n = np.random.randint(26)
            if n < 1:
                end = "shire"
            elif n < 2:
                end = "grove"
            elif n < 3:
                end = "moor"
            elif n < 4:
                end = "lun"
            elif n < 5:
                end = "town"
            elif n < 6:
                end = "moon"
            elif n < 7:
                end = "took"
            elif n < 8:
                end = "firth"
            elif n < 9:
                end = "vale"
            elif n < 10:
                end = "hope"
            elif n < 11:
                end = "field"
            elif n < 12:
                end = "raden"
            elif n < 13:
                end = "fork"
            elif n < 14:
                end = "mist"
            elif n < 15:
                end = "fur"
            elif n < 16:
                end = "wrath"
            elif n < 17:
                end = "burn"
            elif n < 18:
                end = "garth"
            elif n < 19:
                end = "ham"
            elif n < 20:
                end = "stead"
            elif n < 21:
                end = "spore"
            elif n < 22:
                end = "fang"
            elif n < 23:
                end = "tooth"
            elif n < 24:
                end = "bon"
            elif n < 25:
                end = "mush"
            elif n < 26:
                end = "spur"
            
            name = start + end
        names_used.append(name)
        img = Image.new('RGB', (200, 30), color = (0,0,0))
        fnt = ImageFont.truetype('akaPotsley.ttf', 24)
        d = ImageDraw.Draw(img)
        d.text((0,0), name, font=fnt, fill=(255,255,255))
        img.save('town_name.png')
        name_im = Image.open("town_name.png")
        return name_im.load()
    name = get_town_name()
    for i in range(x-45, x+155):
        for j in range(y, y+30):
            if name[i-x+45, j-y][0] > 10:
                colors[i,j] = name[i-x+45, j-y]
    return colors

def place_ruin_name(colors, x,y):
    def get_ruin_name():
        name = ""
        while name_taken(name):
            start = ""
            n = np.random.randint(11)
            if n < 1:
                start = "Eldritch"
            elif n < 2:
                start = "Giant Scorpion"
            elif n < 3:
                start = "Skeleton"
            elif n < 4:
                start = "Zombie"
            elif n < 5:
                start = "Warlock's"
            elif n < 6:
                start = "Necromancer's"
            elif n < 7:
                start = "Demon"
            elif n < 8:
                start = "Argoth's"
            elif n < 9:
                start = "Zagmar's"
            elif n < 10:
                start = "Ordin's"
            elif n < 11:
                start = "Dwarven"
                
            
            end = ""
            n = np.random.randint(5)
            if n < 2:
                end = " Ruins"
            elif n < 3:
                end = " Temple"
            elif n < 4:
                end = " Labyrinth"
            elif n < 5:
                end = " Dungeons"
            
            name = start + end
        names_used.append(name)
        img = Image.new('RGB', (220, 30), color = (0,0,0))
        fnt = ImageFont.truetype('akaPotsley.ttf', 24)
        d = ImageDraw.Draw(img)
        d.text((0,0), name, font=fnt, fill=(255,255,255))
        img.save('town_name.png')
        name_im = Image.open("town_name.png")
        return name_im.load()
    name = get_ruin_name()
    for i in range(x-65, x+155):
        for j in range(y, y+30):
            if name[i-x+65, j-y][0] > 10:
                colors[i,j] = name[i-x+65, j-y]
    return colors

def place_cave_name(colors, x,y):
    def get_cave_name():
        name = ""
        while name_taken(name):
            start = ""
            n = np.random.randint(15)
            if n < 1:
                start = "Wolf"
            elif n < 2:
                start = "Troll"
            elif n < 3:
                start = "Dragon's"
            elif n < 4:
                start = "Slime"
            elif n < 5:
                start = "Goblin"
            elif n < 6:
                start = "Bugbear's"
            elif n < 7:
                start = "Stigmar's"
            elif n < 8:
                start = "Lundmar's"
            elif n < 9:
                start = "Cursed"
            elif n < 10:
                start = "Rork's"
            elif n < 11:
                start = "Foul"
            elif n < 12:
                start = "Murmog's"
            elif n < 13:
                start = "Endless"
            elif n < 14:
                start = "Stygian"
            elif n < 15:
                start = "Ogre's"
                
            
            end = ""
            n = np.random.randint(8)
            if n < 1:
                end = " Cave"
            if n < 2:
                end = " Cavern"
            elif n < 3:
                end = " Den"
            elif n < 4:
                end = " Crevice"
            elif n < 5:
                end = " Depths"
            elif n < 6:
                end = " Grotto"
            elif n < 7:
                end = " Alcove"
            elif n < 8:
                end = " Lair"
            
            name = start + end
        names_used.append(name)
        img = Image.new('RGB', (220, 30), color = (0,0,0))
        fnt = ImageFont.truetype('akaPotsley.ttf', 24)
        d = ImageDraw.Draw(img)
        d.text((0,0), name, font=fnt, fill=(255,255,255))
        img.save('town_name.png')
        name_im = Image.open("town_name.png")
        return name_im.load()
    name = get_cave_name()
    for i in range(x-65, x+155):
        for j in range(y, y+30):
            if name[i-x+65, j-y][0] > 10:
                colors[i,j] = name[i-x+65, j-y]
    return colors

def place_camp_name(colors, x,y):
    def get_camp_name():
        name = ""
        while name_taken(name):
            start = ""
            n = np.random.randint(15)
            if n < 1:
                start = "Orc"
            elif n < 2:
                start = "Goblin"
            elif n < 3:
                start = "Giant Badger"
            elif n < 4:
                start = "Gnoll"
            elif n < 5:
                start = "Imp"
            elif n < 6:
                start = "Lizardfolk"
            elif n < 7:
                start = "Skeleton"
            elif n < 8:
                start = "Bandit"
            elif n < 9:
                start = "Outlaw"
            elif n < 10:
                start = "Brigand"
            elif n < 11:
                start = "Barbarian"
            elif n < 12:
                start = "Cultist"
            elif n < 13:
                start = "Crabfolk"
            elif n < 14:
                start = "Cyclops"
            elif n < 15:
                start = "Dryad"
                
            
            end = ""
            n = np.random.randint(4)
            if n < 1:
                end = " Camp"
            if n < 2:
                end = " Outpost"
            elif n < 3:
                end = " Fort"
            elif n < 4:
                end = " Encampment"
            
            name = start + end
        names_used.append(name)
        img = Image.new('RGB', (220, 30), color = (0,0,0))
        fnt = ImageFont.truetype('akaPotsley.ttf', 24)
        d = ImageDraw.Draw(img)
        d.text((0,0), name, font=fnt, fill=(255,255,255))
        img.save('town_name.png')
        name_im = Image.open("town_name.png")
        return name_im.load()
    name = get_camp_name()
    for i in range(x-65, x+155):
        for j in range(y, y+30):
            if name[i-x+65, j-y][0] > 10:
                colors[i,j] = name[i-x+65, j-y]
    return colors



water_back = Image.open("water_back.png")
water_back = water_back.resize((im_width,im_width))
w_back = water_back.load()

hill_back = Image.open("hill_text.png")
hill_back = hill_back.resize((im_width,im_width))
h_back = hill_back.load()

tree_im1 = Image.open("tree1.png")
tree1 = tree_im1.load()
tree_im2 = Image.open("tree2.png")
tree2 = tree_im2.load()
tree_im3 = Image.open("tree3.png")
tree3 = tree_im3.load()
tree_im4 = Image.open("tree4.png")
tree4 = tree_im4.load()
tree_im5 = Image.open("tree5.png")
tree5 = tree_im5.load()

city_im = Image.open("city.png")
city = city_im.load()

town_im = Image.open("town.png")
town= town_im.load()

ruin_im = Image.open("ruins.png")
ruins = ruin_im.load()

cave_im = Image.open("cave.png")
cave = cave_im.load()

camp_im = Image.open("camp.png")
camp = camp_im.load()



mount_img1 = Image.open("mount1.png")
mount1= mount_img1.load()
mount_img2 = Image.open("mount2.png")
mount2= mount_img2.load()
mount_img3 = Image.open("mount3.png")
mount3= mount_img3.load()

mount_img4 = Image.open("mount1.png")
mount_img4 = mount_img4.resize((14,14))
mount4= mount_img4.load()
mount_img5 = Image.open("mount2.png")
mount_img5 = mount_img5.resize((14,14))
mount5= mount_img5.load()
mount_img6 = Image.open("mount3.png")
mount_img6 = mount_img6.resize((14,14))
mount6= mount_img6.load()

swamp_im = Image.open("swamp.png")
swamp_im = swamp_im.resize((im_width,im_width))
swamp = swamp_im.load()

t0 = time.time()
def gaussian_filter(size):
    #Generate 2-D Gaussian bump filter to add to heightmaps
    sigma = size*.5
    def g(x,y):
        x0 = size*1.5
        y0 = size*1.5
        factor = 1/(sigma*np.sqrt(2*np.pi))
        return factor*np.exp(-.5*(np.square(x-x0)+np.square(y-y0))/np.square(sigma))
    filter_points = np.zeros((size*3,size*3))
    for i in range(size*3):
        for j in range(size*3):
            filter_points[i][j] = g(i,j)
    return filter_points

def normalize_points(points):
    Max = np.amax(points)
    for i in range(im_width):
        for j in range(im_width):
            if points[i,j] != -500:
                points[i,j] = points[i,j]*255.0/Max
    return points

def get_heightmap(width,start_iteration):
    """
    Generate a 2-D array of height points representing the topography of a map. This is accomplished by adding a fractal series of bumps and indents to random locations.
    """
    h_map = np.zeros((width,width))
    iterations = 6
    size = int(width/(6.0*np.power(2,start_iteration-1)))
    for i in range(start_iteration,iterations):
        f = gaussian_filter(size)
        for j in range(np.power(4,i+1)):
            xx_0 = np.random.randint(int(1.5*size),width-int(1.5*size))
            yy_0 = np.random.randint(int(1.5*size),width-int(1.5*size))
            s = f.shape[0]
            h_map[xx_0-int(size*1.5)-width:xx_0-int(size*1.5)+s, yy_0-int(size*1.5)-width:yy_0-int(size*1.5)+s] += f*np.power(size,1.8)
        size = int(size*.5)
    size = int(width/4.0)
    for i in range(iterations):
        f = gaussian_filter(size)
        for j in range(np.power(4,i+1)):
            xx_0 = np.random.randint(int(size*1.5),width-int(size*1.5))
            yy_0 = np.random.randint(int(size*1.5),width-int(size*1.5))
            s = f.shape[0]
            h_map[xx_0-int(size*1.5)-width:xx_0-int(size*1.5)+s, yy_0-int(size*1.5)-width:yy_0-int(size*1.5)+s] -= .5*f*np.power(size,1.8)
        size = int(size*.5)
    for i in range(width):
        for j in range(width):
            if h_map[i][j] <= -1000:
                h_map[i][j] = -500
    return h_map

def get_forest_mask(width):
    f_map = get_heightmap(width,3)
    Max = np.amax(f_map)
    for i in range(width):
        for j in range(width):
            if f_map[i,j] < Max*.01:
                f_map[i,j] = 0
            else:
                f_map[i,j] = 1
    return f_map

def get_hill_mask(width, forest_mask):
    f_map = get_heightmap(width,3)
    Max = np.amax(f_map)
    #print(Max)
    for i in range(width):
        for j in range(width):
            if forest_mask[i,j] != 1:
                if f_map[i,j] < -.5*Max:#*.00000001,    --, -.01
                    f_map[i,j] = 0
                else:
                    f_map[i,j] = 1
            else:
                f_map[i,j] = 0
    return f_map

def get_brick_map(width, forest_mask, hill_mask):
    f_map = get_heightmap(width,3)
    Max = np.amax(f_map)
    for i in range(width):
        for j in range(width):
            if forest_mask[i,j] != 1 and hill_mask[i,j] != 1:
                if f_map[i,j] < -.75*Max:#*.00015:
                    f_map[i,j] = 0
                else:
                    f_map[i,j] = 1
            else:
                f_map[i,j] = 0
    return f_map

def add_river(hmap):
    Max = np.amax(hmap)
    i = np.random.randint(im_width)
    j = np.random.randint(im_width)
    while hmap[i][j] < Max*.66 or hmap[i][j] > Max*.75:
        i = np.random.randint(im_width)
        j = np.random.randint(im_width)
    x = i
    y = j
    angle = np.random.randint(200)*np.pi/100
    while hmap[int(x+3*np.cos(angle))][int(y+3*np.sin(angle))] > Max/7.5 or hmap[int(x+3*np.cos(angle))][int(y+3*np.sin(angle))]== -1000:
        if hmap[int(x+4*np.cos(angle))][int(y+4*np.sin(angle))] > Max*.75:
            angle += np.pi/4
        hmap[x][y] = -1000
        hmap[x+1,y] = -1000
        hmap[x,y+1] = -1000
        hmap[x+1,y+1] = -1000
        x+=2*np.cos(angle)
        y+=2*np.sin(angle)
        x = int(x)
        y = int(y)
        angle += .15*(np.random.randint(200)*np.pi/100 -np.pi)
    for n in range(3):
        hmap[x][y] = Max/7.6
        hmap[x+1,y] = Max/7.6
        hmap[x,y+1] = Max/7.6
        hmap[x+1,y+1] = Max/7.6
        x+=2*np.cos(angle)
        y+=2*np.sin(angle)
        x = int(x)
        y = int(y)
    return hmap
        




def blend_colors(c1, c2, amount):
    red = int(c1[0]*(1-amount)+c2[0]*amount)
    green = int(c1[1]*(1-amount)+c2[1]*amount)
    blue = int(c1[2]*(1-amount)+c2[2]*amount)
    return (red, green, blue)



def get_colors(heightmap, forest_map, hill_mask, brick_mask):
    Max = np.amax(heightmap)
    temp = np.zeros((im_width, im_width))
    for i in range(im_width):
        for j in range(im_width):
            if heightmap[i,j] > -1000:
                temp[i,j] = heightmap[i,j]
    Min = np.amin(temp)
    water_level = Max/7.5
    im2 = Image.new('RGB', (im_width,im_width), 0)
    colors = im2.load()
    for j in range(heightmap.shape[1]):
        r_factor = np.random.randint(12)
        for i in range(heightmap.shape[0]):
            if heightmap[i,j] == -1000:
                colors[i,j] = (41, 50, 154)
            elif heightmap[i][j] < water_level:
                alpha = np.power((heightmap[i][j] - Min)/(water_level-Min),4)
                colors[i,j] = blend_colors(w_back[i,j], (41, 50, 154), alpha)
            elif heightmap[i,j] <Max*.5:
                d_x = 0
                if i >1 and i < heightmap.shape[0]-2:
                    d_x = (heightmap[i+2,j] -heightmap[i-2,j])*.25*(im_width/600.0)/(Max*.025)
                    if heightmap[i+1,j]== -1 or heightmap[i,j] == -1:
                        d_x = 0
                    if d_x < -1:
                        d_x = -1
                    if d_x > 1:
                        d_x = 1
                if forest_map[i,j] == 1:
                    colors[i,j] = (85-int(80*d_x),181-int(80*d_x),74-int(70*d_x))
                elif hill_mask[i,j] == 1:
                    hill_color = h_back[i,j]
                    r = hill_color[0]
                    g = hill_color[1]
                    b = hill_color[2]
                    #colors[i,j] = h_back[i,j]
                    colors[i,j] = (r-int(d_x*80), g-int(d_x*80), b)
                elif brick_mask[i,j] == 1:
                    colors[i,j]= (175-int(80*d_x),111-int(80*d_x),99-int(70*d_x))
                elif i < heightmap.shape[0]-1:
                    ###
                    d_x = 0
                    if i >0 and i < heightmap.shape[0]-1:
                        d_x = (heightmap[i+1,j] -heightmap[i-1,j])*.5*(im_width/600.0)/(Max*.025)
                    if heightmap[i+1,j]== -1 or heightmap[i,j] == -1:
                        d_x = 0
                    if d_x < -1:
                        d_x = -1
                    if d_x > 1:
                        d_x = 1
                    ###
                    colors[i,j] = (152-int(50*d_x),138-int(50*d_x),120-int(50*d_x))
                """
                elif heightmap[i,j] <Max*.85:
                    d_x = 0
                    if i >0 and i < heightmap.shape[0]-1:
                        d_x = (heightmap[i+1,j] -heightmap[i,j])/(Max*.025)
                    if heightmap[i+1,j]== -1 or heightmap[i,j] == -1:
                        d_x = 0
                    colors[i,j] = swamp[i,j]
                    im_type = 1
                """
            elif heightmap[i,j] <Max*.75:
                d_x = 0
                if i >1 and i < heightmap.shape[0]-2:
                    d_x = (heightmap[i+2,j] -heightmap[i-2,j])*.25*(im_width/600.0)/(Max*.025)
                if i < heightmap.shape[0]-1:
                    if heightmap[i+1,j]== -1 or heightmap[i,j] == -1:
                        d_x = 0
                ###
                if d_x < -1:
                    d_x = -1
                if d_x > 1:
                    d_x = 1
                ###
                colors[i,j] = (115-int(50*d_x),109-int(50*d_x),96-int(50*d_x))
                if np.random.randint(500) <2:
                    r = np.random.randint(7)
                    if r < 1:
                        for u in range(i-14,i+14):
                            for v in range(j-14, j+14):
                                if mount1[u-i+14,v-j+14][0] > 5:
                                    if v > j-7:
                                        colors[u,v] = blend_colors(mount1[u-i+14,v-j+14], colors[u,v], (v-(j-7))/7  )
                                    else:
                                        colors[u,v] = mount1[u-i+14,v-j+14]
                    elif r < 2:
                        for u in range(i-14,i+14):
                            for v in range(j-14, j+14):
                                if mount2[u-i+14,v-j+14][0] > 5:
                                    if v > j-7:
                                        colors[u,v] = blend_colors(mount2[u-i+14,v-j+14], colors[u,v], (v-(j-7))/7  )
                                    else:
                                        colors[u,v] = mount2[u-i+14,v-j+14]
                    elif r < 3:
                        for u in range(i-14,i+14):
                            for v in range(j-14, j+14):
                                if mount3[u-i+14,v-j+14][0] > 5:
                                    if v > j-7:
                                        colors[u,v] = blend_colors(mount3[u-i+14,v-j+14], colors[u,v], (v-(j-7))/7  )
                                    else:
                                        colors[u,v] = mount3[u-i+14,v-j+14]
                    elif r < 4:
                        for u in range(i-7,i+7):
                                for v in range(j-7, j+7):
                                    if mount4[u-i+7,v-j+7][0] > 5:
                                        colors[u,v] = mount4[u-i+7,v-j+7]
                    elif r < 5:
                        for u in range(i-7,i+7):
                                for v in range(j-7, j+7):
                                    if mount5[u-i+7,v-j+7][0] > 5:
                                        colors[u,v] = mount5[u-i+7,v-j+7]
                    else:
                        for u in range(i-7,i+7):
                                for v in range(j-7, j+7):
                                    if mount6[u-i+7,v-j+7][0] > 5:
                                        colors[u,v] = mount6[u-i+7,v-j+7]
                
            else:
                d_x = 0
                if i >0 and i < heightmap.shape[0]-1:
                    d_x = max((heightmap[i+1,j] -heightmap[i-1,j])*.5*(im_width/600.0)/(Max*.025),0)
                if i < heightmap.shape[0]-1:
                    if heightmap[i+1,j]== -1 or heightmap[i,j] == -1:
                        d_x = 0
                ###
                if d_x < -.25:
                     d_x = -.25
                if d_x > .25:
                    d_x = .25
                ###
                colors[i,j] = (255-int(100*d_x),255-int(100*d_x),255)

                    
    return colors

def add_trees(heightmap, forest_map, colors):
    Max = np.amax(heightmap)
    temp = np.zeros((im_width, im_width))
    for i in range(im_width):
        for j in range(im_width):
            if heightmap[i,j] > -1000:
                temp[i,j] = heightmap[i,j]
    Min = np.amin(temp)
    water_level = Max/7.5
    for j in range(heightmap.shape[1]):
        for i in range(heightmap.shape[0]):
            if heightmap[i,j] <Max*.5 and heightmap[i,j] > water_level and forest_map[i,j] == 1 and np.random.randint(350)<1:
                r = np.random.randint(5)
                if r < 1:
                    for u in range(i-7,i+6):
                        for v in range(j-4, j+9):
                            if tree1[u-i+7, v-j+4][1] >30:
                                colors[u,v] = tree1[u-i+7, v-j+4]
                elif r < 2:
                    for u in range(i-7,i+6):
                        for v in range(j-4, j+9):
                            if tree2[u-i+7, v-j+4][1] >30:
                                colors[u,v] = tree2[u-i+7, v-j+4]
                elif r < 3:
                    for u in range(i-7,i+6):
                        for v in range(j-4, j+9):
                            if tree3[u-i+7, v-j+4][1] >30:
                                colors[u,v] = tree3[u-i+7, v-j+4]
                elif r < 4:
                    for u in range(i-9,i+9):
                        for v in range(j-40, j+35):
                            if v > 0 and v < im_width and u > 0 and u < im_width:
                                    if tree4[u-i+9, v-j+40][1] >15:
                                        colors[u,v] = tree4[u-i+9, v-j+40]
                else:
                    for u in range(i-16,i+16):
                        for v in range(j-35, j+100):
                                if v > 0 and v < im_width and u > 0 and u < im_width:
                                    if tree5[u-i+16, v-j+35][1] >15:
                                        colors[u,v] = tree5[u-i+16, v-j+35]

                    
    return colors

def blend_colormap(colors, hmap):
    def get_hue(color):
        R = color[0]
        G = color[1]
        B = color[2]
        hue = np.arctan2(np.sqrt(3)*(G-B),2*R-G-B)*180/np.pi+180
        return hue
    def get_hue_difference(color1, color2):
        hue1 = get_hue(color1)
        hue2 = get_hue(color2)
        diff1 = abs(hue1-hue2)
        diff2 = abs(hue1 + 360 - hue2)
        diff3 = abs(hue1 -(hue2+360))
        return min(diff1, diff2, diff3)

    Max = np.amax(hmap)
    im2 = Image.new('RGB', (im_width,im_width), 0)
    c_out = im2.load()
    for i in range(im_width):
        for j in range(im_width):
            c_out[i,j] = colors[i,j]
    ave_width = 12

    def blur(i,j):
        norm = 0
        red = 0
        green = 0
        blue = 0
        for k in range(i -int(ave_width/2), i +int(ave_width/2) ):
            for l in range(j -int(ave_width/2), j +int(ave_width/2) ):
                if k > -1 and k < im_width and l > -1 and l < im_width:
                    if hmap[k,l] > Max/7.5:
                        red += colors[k,l][0]
                        green += colors[k,l][1]
                        blue += colors[k,l][2]
                        norm += 1
        red = int(red*1.0/norm)
        green = int(green*1.0/norm)
        blue = int(blue*1.0/norm)
        return (red, green, blue)
                
    def check_hue_contrast(i,j):
        c0 = colors[i,j]
        c1 = c0
        dist = 8
        if i - dist > -1:
            if hmap[i-dist, j] > Max/7.5:
                c1 = colors[i-dist, j]
        c2 = c0
        if i +dist < im_width:
            if hmap[i+dist, j] > Max/7.5:
                c2 = colors[i+dist, j]
        c3 = c0
        if j-dist > -1:
            if hmap[i, j-dist] > Max/7.5:
                c3 = colors[i,j-dist]
        c4 = c0
        if j+dist < im_width:
            if hmap[i, j+dist] > Max/7.5:
                c4 = colors[i,j+dist]
        max_hue_diff = max(get_hue_difference(c1, c2), get_hue_difference(c3, c4))
        if max_hue_diff > 15:
            return True
        else:
            return False
    
    for i in range(im_width):
        for j in range(im_width):
            if hmap[i,j] > Max/7.5 and check_hue_contrast(i,j):
                c_out[i,j] = blur(i,j)
    return c_out

def place_settlements(hmap, colors):
    Max = np.amax(hmap)
    def ok_for_city(x,y):
        ok = True
        for i in range(x-20, x+20):
            for j in range(y-20, y+20):
                if hmap[i][j] < Max/7.5 or hmap[i][j] > Max*.5:
                    ok = False
        return ok
    def ok_for_town(x,y):
        ok = True
        for i in range(x-10, x+10):
            for j in range(y-10, y+10):
                if hmap[i][j] < Max/7.5 or hmap[i][j] > Max*.5:
                    ok = False
        return ok
    locations = []
    M = 0
    def dist_ok(x,y):
        ok = True
        for m in range(M):
            r = np.sqrt(np.square(x-locations[m][0])+np.square(y-locations[m][1]))
            if r < 150:
                ok = False
        return ok
    def place_city(colors, x,y):
        W = 100
        H = 143
        for i in range(x - int(W/2), x+ int(W/2)):
            for j in range(y-int(H/2)+30, y+ int(H/2)+30):
                if city[i-x+int(W/2), j-y+int(H/2)-30][0] > 0:
                    colors[i,j] = city[i-x+int(W/2), j-y+int(H/2)-30]
        return colors

    def place_town(colors, x,y):
        W = 58
        H = 102
        for i in range(x - int(W/2), x+ int(W/2)):
            for j in range(y-int(H/2)+25, y+ int(H/2)+25):
                if town[i-x+int(W/2), j-y+int(H/2)-25][0] > 20:
                    colors[i,j] = town[i-x+int(W/2), j-y+int(H/2)-25]
        return colors
        
    def place_ruins(colors, x,y):
        W = 60
        H = 119
        for i in range(x - int(W/2), x+ int(W/2)):
            for j in range(y-int(H/2)+40, y+ int(H/2)+40):
                if ruins[i-x+int(W/2), j-y+int(H/2)-40][0] > 10:
                    colors[i,j] = ruins[i-x+int(W/2), j-y+int(H/2)-40]
        return colors

    def place_cave(colors, x,y):
        W = 60
        H = 120
        for i in range(x - int(W/2), x+ int(W/2)):
            for j in range(y-int(H/2)+40, y+ int(H/2)+40):
                if cave[i-x+int(W/2), j-y+int(H/2)-40][0] > 10:
                    colors[i,j] = cave[i-x+int(W/2), j-y+int(H/2)-40]
        return colors

    def place_camp(colors, x,y):
        W = 120
        H = 240
        for i in range(x - int(W/2), x+ int(W/2)):
            for j in range(y-int(H/2)+40, y+ int(H/2)+40):
                if camp[i-x+int(W/2), j-y+int(H/2)-40][0] > 5:
                    colors[i,j] = camp[i-x+int(W/2), j-y+int(H/2)-40]
        return colors
    
    for n in range(3):
        x = np.random.randint(im_width-102)+51
        y = np.random.randint(im_width-288)+144
        while (not ok_for_city(x,y)) or not dist_ok(x,y):
            x = np.random.randint(im_width-102)+51
            y = np.random.randint(im_width-288)+144
        place_city(colors, x,y)
        place_city_name(colors, x,y+30)
        M += 1
        locations.append([x,y])

    for n in range(9):
        x = np.random.randint(im_width-102)+51
        y = np.random.randint(im_width-288)+144
        while (not ok_for_town(x,y)) or not dist_ok(x,y):
            x = np.random.randint(im_width-102)+51
            y = np.random.randint(im_width-288)+144
        place_town(colors, x,y)
        place_town_name(colors, x,y+25)
        M += 1
        locations.append([x,y])

    N = 2 + np.random.randint(3)
    for n in range(N):
        x = np.random.randint(im_width-160)+80
        y = np.random.randint(im_width-400)+400
        while (not ok_for_town(x,y)) or not dist_ok(x,y):
            x = np.random.randint(im_width-160)+80
            y = np.random.randint(im_width-400)+400
        place_ruins(colors, x,y)
        place_ruin_name(colors, x-8,y+30)
        M += 1
        locations.append([x,y])

    N = 2 + np.random.randint(3)
    for n in range(N):
        x = np.random.randint(im_width-160)+80
        y = np.random.randint(im_width-400)+400
        while (not ok_for_town(x,y)) or not dist_ok(x,y):
            x = np.random.randint(im_width-160)+80
            y = np.random.randint(im_width-400)+400
        place_cave(colors, x,y-15)
        place_cave_name(colors, x-8,y+30)
        M += 1
        locations.append([x,y])

    N = 2 + np.random.randint(3)
    for n in range(N):
        x = np.random.randint(im_width-240)+120
        y = np.random.randint(im_width-400)+400
        while (not ok_for_town(x,y)) or not dist_ok(x,y):
            x = np.random.randint(im_width-240)+120
            y = np.random.randint(im_width-400)+400
        place_camp(colors, x,y+15)
        place_camp_name(colors, x-8,y+10)
        M += 1
        locations.append([x,y])

    return colors

hmap = get_heightmap(im_width,2)
print("Heightmap generated")
hmap = normalize_points(hmap)
forest_map = get_forest_mask(im_width)
print("Forests generated")
hill_mask = get_hill_mask(im_width, forest_map)
print("Hills generated")
brick_mask = get_brick_map(im_width, forest_map, hill_mask)
print("Brick lands generated")
"""
for i in range(10):
    hmap = add_river(hmap)
print("Rivers generated")
"""
colors = get_colors(hmap, forest_map, hill_mask, brick_mask)
print("Map colors generated")
colors = blend_colormap(colors, hmap)
print("Color borders smoothed")
colors = add_trees(hmap, forest_map, colors)
print("Trees placed")
colors = place_settlements(hmap, colors)
print("Settlements placed")
print ("Time elapsed: "+str(time.time()-t0)+" s")


def show_image():
    im = Image.new('RGB', (im_width,im_width), 0)
    pixels = im.load()
    for i in range(im_width):
        for j in range(im_width):
            #color = (0, int(hmap[i][j]),0)
            pixels[i,j] = colors[i,j]
    im.show()
    im.save("map.png")


show_image()

