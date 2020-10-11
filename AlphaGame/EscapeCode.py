# Danielle Anderson
# Version Beta
# Instructions: Use the mouse to go between rooms via arrows to collect
# and use items found in order to gather pieces of a code that will
# be inputted into the control panel to win.

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 13, 91)
GRAY = (127, 127, 127)
YELLOW = (255, 242, 0)


class Lock(pygame.sprite.Sprite):
    # Define the locking device class
    WIDTH = 150
    HEIGHT = 100
    X = 250
    Y = 100

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])

        self.rect = self.image.get_rect()
        self.rect.x = self.X
        self.rect.y = self.Y

        self.image = lk_image.convert()


class Buttons(pygame.sprite.Sprite):
    # Define the button class
    # there are 3 kinds of buttons on the locking device
    # two (up, down) change the number displayed
    # enter checks if the number displayed is right
    number = 0
    b_name = ""

    def __init__(self, name, width, height, button_x, button_y):
        super().__init__()
        self.image = pygame.Surface([width, height])

        self.rect = self.image.get_rect()
        self.rect.x = button_x
        self.rect.y = button_y

        # get the sprite for each object
        if name == "up":
            self.image = up_image.convert()
        elif name == "down":
            self.image = dn_image.convert()
        elif name == "enter":
            self.image = et_image.convert()
        self.b_name = name


class UsefulItems(pygame.sprite.Sprite):
    # Define useful items class
    # These items are for interaction and will get the
    # code pieces
    WIDTH = 50
    HEIGHT = 50
    location = 0
    lit_candle = False
    item_name = ''

    def __init__(self, name, item_x, item_y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])

        self.rect = self.image.get_rect()
        self.rect.x = item_x
        self.rect.y = item_y

        self.item_name = name

        # get the sprite for each object
        if name == 'magnifying glass':
            self.image = mg_image.convert()
        elif name == 'screwdriver':
            self.image = sc_image.convert()
        elif name == 'recipe':
            self.image = rp_image.convert()
        elif name == 'tomato':
            self.image = tm_image.convert()
        elif name == 'carrot':
            self.image = ct_image.convert()
        elif name == 'cilantro':
            self.image = cl_image.convert()
        elif name == 'herb':
            self.image = hb_image.convert()
        elif name == 'candle':
            self.image = cd_image.convert()
        elif name == 'matches':
            self.image = mt_image.convert()
        self.image.set_colorkey(PINK)

    def light(self):
        self.lit_candle = True
        new_image = pygame.image.load('lit.png')
        self.image = new_image.convert()
        self.image.set_colorkey(PINK)

    def store(self, name):
        position_x = 0
        position_y = 0
        if name == 'magnifying glass':
            position_x = 90
            position_y = 325
        elif name == 'screwdriver':
            position_x = 250
            position_y = 325
        elif name == 'recipe' or name == 'herb':
            position_x = 385
            position_y = 325
        elif name == 'matches' or name == 'candle':
            position_x = 540
            position_y = 325

        self.rect.x = position_x
        self.rect.y = position_y


class CodePieces(pygame.sprite.Sprite):
    # Define the code pieces class
    # These pieces/objects tell/give you parts of the code
    # to be inputted in the locking device
    changed = False
    location = 0

    def __init__(self, name, piece_x, piece_y, piece_width, piece_height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([piece_width, piece_height])

        self.rect = self.image.get_rect()

        self.rect.x = piece_x
        self.rect.y = piece_y

        # get the sprite of the object
        if name == 'note':
            self.image = nt_image.convert()
        elif name == 'chest' and self.changed is False:
            self.image = ch_image.convert()
        elif name == 'pot':
            self.image = pt_image.convert()
        elif name == 'book':
            self.image = bk_image.convert()
        self.image.set_colorkey(PINK)

    def on_clicked(self, name):
        # change something about the object on click
        if name == 'chest':
            new_image = pygame.image.load('chest_under.png')
            self.image = new_image.convert()
            self.changed = True

    def open(self, screw_num):
        # open the chest once screws are removed
        if screw_num == 1:
            new_image = pygame.image.load('chest_under_1.png')
            self.image = new_image.convert()
            self.changed = True
        elif screw_num == 2:
            new_image = pygame.image.load('chest_under_2.png')
            self.image = new_image.convert()
            self.changed = True
        else:
            creak_sound.play()
            new_image = pygame.image.load('chest_open.png')
            self.image = new_image.convert()
            self.changed = True


class Inventory(pygame.sprite.Sprite):
    # Define inventory class
    # This will hold up to 4 items to carry
    # between rooms
    WIDTH = 700
    HEIGHT = 100
    X = 0
    Y = 300

    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.rect.x = self.X
        self.rect.y = self.Y


class Box(pygame.sprite.Sprite):
    # Define the box class
    # These are the boxes items are held in
    # the inventory
    WIDTH = 135
    HEIGHT = 50
    SPACE = 150

    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()


def show_code(box):
    # Display the part of the code gained from a code piece
    font = pygame.font.SysFont("serif", 15)
    if box == box1:
        text = font.render("Code piece is 6138", True, BLACK)
        screen.blit(text, [60, 345])
    elif box == box2:
        text = font.render("Code piece is 492", True, BLACK)
        screen.blit(text, [205, 345])
    elif box == box3:
        if ingredients < 5 and room_num == 4:
            text = font.render("The recipe calls for: 3 Carrots, 1 Tomato, "
                               "and something else "
                               "you can't read", True, BLACK)
            screen.blit(text, [180, 100])
        elif ingredients >= 5:
            text = font.render("3 Carrots, 1 Tomato,", True, BLACK)
            text2 = font.render("4 Cilantro", True, BLACK)
            screen.blit(text, [355, 335])
            screen.blit(text2, [355, 350])
    elif box == box4:
        text = font.render("Code piece is " + str(num1.num) + str(num2.num) +
                           str(num3.num) + str(num4.num), True, BLACK)
        screen.blit(text, [510, 345])


class WallNumber(pygame.sprite.Sprite):
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, num, num_x, num_y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = num_x
        self.rect.y = num_y
        self.image.set_alpha(0)
        self.num = num


class Arrow(pygame.sprite.Sprite):
    # Define the arrow class
    # On clicking them, these objects will move
    # you from room to room
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, arrow_x, arrow_y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.rect = self.image.get_rect()
        self.rect.x = arrow_x
        self.rect.y = arrow_y

    def draw(self, direction):
        # There are 4 different arrows for each direction
        # If an 'X' is shown this means that this is not
        # a direction the player can take
        if direction == 'left':
            ar_image = pygame.image.load('arrow-left.png')
        elif direction == 'up':
            ar_image = pygame.image.load('arrow-up.png')
        elif direction == 'down':
            ar_image = pygame.image.load('arrow-down.png')
        elif direction == 'right':
            ar_image = pygame.image.load('arrow.png')
        else:
            ar_image = pygame.image.load('stop.png')
        self.image = ar_image.convert()
        self.image.set_colorkey(PINK)
# Setup


def add_to_room(item, num):
    # If an item is placed in a room
    # Remove it from all others first
    # and change location
    item.location = num
    if num == 0:
        ingredients_list.remove(item)
    inventory_list.remove(item)
    room_1_list.remove(item)
    room_2_list.remove(item)
    room_3_list.remove(item)
    room_4_list.remove(item)
    room_11_list.remove(item)
    room_12_list.remove(item)
    room_13_list.remove(item)
    room_14_list.remove(item)
    room_21_list.remove(item)
    room_22_list.remove(item)
    room_23_list.remove(item)
    room_24_list.remove(item)
    if num % 10 == 1:
        if num == 1:
            room_1_list.add(item)
        elif num == 11:
            room_11_list.add(item)
        else:
            room_21_list.add(item)
    elif num % 10 == 2:
        if num == 2:
            room_2_list.add(item)
        elif num == 12:
            room_12_list.add(item)
        else:
            room_22_list.add(item)
    elif num % 10 == 3:
        if num == 3:
            room_3_list.add(item)
        elif num == 13:
            room_13_list.add(item)
        else:
            room_23_list.add(item)
    elif num % 10 == 4:
        if num == 4:
            room_4_list.add(item)
        elif num == 14:
            room_14_list.add(item)
        else:
            room_24_list.add(item)


def draw_room(number):
    # Draw all the components in a room
    if number % 10 == 1:
        if number == 1:
            room_1_list.draw(screen)
        elif number == 11:
            room_11_list.draw(screen)
        else:
            room_21_list.draw(screen)
        arrow_right.draw('right')
        arrow_left.draw('stop')
        arrow_up.draw('stop')
        arrow_down.draw('stop')
    elif number % 10 == 2:
        if number == 2:
            room_2_list.draw(screen)
        elif number == 12:
            room_12_list.draw(screen)
        else:
            room_22_list.draw(screen)
        arrow_right.draw('right')
        arrow_left.draw('left')
        arrow_up.draw('stop')
        arrow_down.draw('stop')
    elif number % 10 == 3:
        if number == 3:
            room_3_list.draw(screen)
            arrow_up.draw('up')
            arrow_down.draw('stop')
        elif number == 13:
            room_13_list.draw(screen)
            arrow_up.draw('up')
            arrow_down.draw('down')
        else:
            room_23_list.draw(screen)
            arrow_up.draw('stop')
            arrow_down.draw('down')
        arrow_right.draw('right')
        arrow_left.draw('left')
    elif number % 10 == 4:
        if number == 4:
            room_4_list.draw(screen)
            # ingredients_list.draw(screen)
        elif number == 14:
            room_14_list.draw(screen)
        else:
            room_24_list.draw(screen)
        arrow_right.draw('stop')
        arrow_left.draw('left')
        arrow_up.draw('stop')
        arrow_down.draw('stop')


def display_text(evt):
    # Display text when prompted
    font = pygame.font.SysFont("serif", 15)
    if evt == "herb":
        text = font.render("You grabbed 4 stalks of cilantro", True, BLACK)
        screen.blit(text, [180, 100])
    elif evt == "note":
        if not magnifying_g.location == 0:
            text = font.render("This note is too small to read", True, BLACK)
        else:
            text = font.render("Remember the book upstairs", True, BLACK)
        screen.blit(text, [20, 130])
    elif evt == "recipe":
        text = font.render("This recipe is for the soup "
                           "in the pot", True, BLACK)
        screen.blit(text, [445, 180])
    elif evt == "soup":
        text = font.render("You need a recipe to make the soup", True, BLACK)
        screen.blit(text, [100, 80])
    elif evt == "locked":
        text = font.render("Input code to open the door", True, BLACK)
        screen.blit(text, [240, 70])


def config_panel(index):
    # This matches the right up/down buttons
    # with the right spot on the locking device panel
    if index == 0 or index == 1:
        return 0
    elif index == 2 or index == 3:
        return 1
    elif index == 4 or index == 5:
        return 2
    elif index == 6 or index == 7:
        return 3


def on_click(name, j):
    # This changes the number on the locking
    # device panel
    if name == "up":
        panel_list[j] += 1
    elif name == "down":
        panel_list[j] -= 1

    # allow it to loop around
    if panel_list[j] > 9:
        panel_list[j] = 0
    if panel_list[j] < 0:
        panel_list[j] = 9


def getcode():
    # Get the code that was inputted in the
    # locking device panel
    code_string = ""
    for k in range(len(panel_list)):
        code_string += str(panel_list[k])
    return code_string


pygame.init()

# Set the width and height of the screen [width,height]
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

#  locking device sprites
up_image = pygame.image.load("up_button.png")
dn_image = pygame.image.load("down_button.png")
lk_image = pygame.image.load("locked.png")
ulk_image = pygame.image.load("unlocked.png")
et_image = pygame.image.load("enter.png")

# useful items sprites
mg_image = pygame.image.load('magnifying_glass.png')
sc_image = pygame.image.load('screwdriver.png')
mt_image = pygame.image.load('matches.png')
rp_image = pygame.image.load('recipe.png')
light = pygame.image.load('light.png')
cd_image = pygame.image.load('unlit.png')

# code pieces sprites
nt_image = pygame.image.load('note.png')
ch_image = pygame.image.load('chest_front.png')

# recipe items sprites -- note some of these are also
# either useful items or code pieces
pt_image = pygame.image.load('pot.png')
ct_image = pygame.image.load('carrot.png')
tm_image = pygame.image.load('tomato.png')
cl_image = pygame.image.load('cilantro.png')
hb_image = pygame.image.load('herb.png')
bk_image = pygame.image.load('morse_book.png')

# This is a list of every sprite.
common_sprites_list = pygame.sprite.Group()

# These lists indicate what is in each room
room_1_list = pygame.sprite.Group()
room_2_list = pygame.sprite.Group()
room_3_list = pygame.sprite.Group()
room_4_list = pygame.sprite.Group()
room_11_list = pygame.sprite.Group()
room_12_list = pygame.sprite.Group()
room_13_list = pygame.sprite.Group()
room_14_list = pygame.sprite.Group()
room_21_list = pygame.sprite.Group()
room_22_list = pygame.sprite.Group()
room_23_list = pygame.sprite.Group()
room_24_list = pygame.sprite.Group()

# groups
inventory_list = pygame.sprite.Group()
item_clicked_list = pygame.sprite.Group()
item_used_list = pygame.sprite.Group()
useful_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()
arrow_list = pygame.sprite.Group()
ingredients_list = pygame.sprite.Group()

# lists
button_list = []
panel_list = []
cupboard_list = []
position_list = [(237, 194), (393, 194), (544, 194), (428, 6), (560, 6)]
book_list = []

for i in range(3):
    cupboard = pygame.image.load('cupboard.png').convert()
    cupboard_list.append(cupboard)
for i in range(4, 6):
    cupboard = pygame.image.load('cupboard_2.png').convert()
    cupboard_list.append(cupboard)

clock_door = pygame.image.load('clock_door.png').convert()
clock_door.set_colorkey(PINK)

book1 = pygame.Surface([52, 12])
book1.get_rect(topleft=(57, 87))
book1.fill(YELLOW)
book1.set_alpha(0)
book_list.append(book1)

book2 = pygame.Surface([12, 40])
book2.get_rect(topleft=(62, 110))
book2.fill(YELLOW)
book2.set_alpha(0)
book_list.append(book2)

book3 = pygame.Surface([11, 39])
book3.get_rect(topleft=(272, 160))
book3.fill(YELLOW)
book3.set_alpha(0)
book_list.append(book3)

book4 = pygame.Surface([23, 34])
book4.get_rect(topleft=(292, 257))
book4.fill(YELLOW)
book4.set_alpha(0)
book_list.append(book4)

minute_hand = pygame.image.load('minute_hand.png').convert()
minute_hand.set_colorkey(PINK)
hour_hand = pygame.image.load('hour_hand.png').convert()
hour_hand.set_colorkey(PINK)

# Create the locking device panel of numbers
for i in range(4):
    panel_list.append(0)

# if user has an item in inventory selected
selected = None

# Starting room number
room_num = -1

# create the lock and its buttons
lock = Lock()
room_1_list.add(lock)

# Create locking device buttons
up_x = 292
up_y = 129
down_x = 292
down_y = 165
for i in range(4):
    up = Buttons("up", 15, 15, up_x, up_y)
    down = Buttons("down", 15, 15, down_x, down_y)
    up_x += 15
    down_x += 15
    room_1_list.add(up)
    room_1_list.add(down)
    button_list.append(up)
    button_list.append(down)

enter = Buttons("enter", 68, 27, 290, 185)
room_1_list.add(enter)

# create an inventory
inventory = Inventory(GREEN)
common_sprites_list.add(inventory)
box_x = 50
box_y = 325

box1 = Box(WHITE)
box1.rect.x = box_x
box_x += box1.SPACE
box1.rect.y = box_y
common_sprites_list.add(box1)

box2 = Box(WHITE)
box2.rect.x = box_x
box_x += box2.SPACE
box2.rect.y = box_y
common_sprites_list.add(box2)

box3 = Box(WHITE)
box3.rect.x = box_x
box_x += box3.SPACE
box3.rect.y = box_y
common_sprites_list.add(box3)

box4 = Box(WHITE)
box4.rect.x = box_x
box_x += box4.SPACE
box4.rect.y = box_y
common_sprites_list.add(box4)

# create an arrow to go to the next room
arrow_right = Arrow(650, 250)
common_sprites_list.add(arrow_right)
arrow_list.add(arrow_right)
arrow_left = Arrow(0, 250)
common_sprites_list.add(arrow_left)
arrow_list.add(arrow_left)
arrow_up = Arrow(650, 0)
common_sprites_list.add(arrow_up)
arrow_list.add(arrow_up)
arrow_down = Arrow(0, 0)
common_sprites_list.add(arrow_down)
arrow_list.add(arrow_down)

# create code pieces
note = CodePieces('note', 100, 100, 20, 20)
room_1_list.add(note)
useful_list.add(note)
add_to_room(note, 1)

chest = CodePieces('chest', 400, 30, 100, 100)
room_21_list.add(chest)
useful_list.add(chest)
screws = 0
add_to_room(chest, 21)

pot = CodePieces('pot', 97, 108, 45, 61)
room_4_list.add(pot)
useful_list.add(pot)
ingredients = 0

book = CodePieces('book', 513, 121, 33, 8)
room_11_list.add(book)
useful_list.add(book)

# create useful items
magnifying_g = UsefulItems("magnifying glass", 275, 170)
room_14_list.add(magnifying_g)
add_to_room(magnifying_g, 14)
item_list.add(magnifying_g)

screwdriver = UsefulItems("screwdriver", 162, 248)
room_12_list.add(screwdriver)
add_to_room(screwdriver, 12)
item_list.add(screwdriver)

recipe = UsefulItems("recipe", 460, 110)
room_2_list.add(recipe)
add_to_room(recipe, 2)
item_list.add(recipe)

tomato = UsefulItems("tomato", 370, 138)
ingredients_list.add(tomato)
add_to_room(tomato, 4)

carrot = UsefulItems("carrot", 425, 154)
ingredients_list.add(carrot)
add_to_room(carrot, 4)

carrot2 = UsefulItems("carrot", 435, 154)
ingredients_list.add(carrot2)
add_to_room(carrot2, 4)

carrot3 = UsefulItems("carrot", 445, 154)
ingredients_list.add(carrot3)
add_to_room(carrot3, 4)

herb = UsefulItems("herb", 337, 115)
room_24_list.add(herb)
add_to_room(herb, 24)
item_list.add(herb)

cilantro = UsefulItems("cilantro", 330, 109)
room_24_list.add(cilantro)
add_to_room(cilantro, 24)

candle = UsefulItems("candle", 150, 185)
room_21_list.add(candle)
add_to_room(candle, 21)
item_list.add(candle)

matches = UsefulItems("matches", 440, 238)
room_4_list.add(matches)
add_to_room(matches, 4)
item_list.add(matches)

num1 = WallNumber(7, 200, 120)
room_22_list.add(num1)

num2 = WallNumber(0, 310, 140)
room_22_list.add(num2)

num3 = WallNumber(5, 430, 145)
room_22_list.add(num3)

num4 = WallNumber(8, 515, 135)
room_22_list.add(num4)

pygame.display.set_caption("Escape Code")

# loop until the user clicks the close button.
done = False

# other variables
hold = None
display_txt = None
display_box1_text = False
display_box2_text = False
display_box3_text = False
display_box4_text = False
code = ""
code_text = ""
stage = 1
timer = 0
grab = True
books_clicked = 0
show_morse = False
turns = 0
time = '12:15'
wall_num = 0

# sound effects
success_sound = pygame.mixer.Sound("beep.ogg")
button_sound = pygame.mixer.Sound("button.ogg")
splash_sound = pygame.mixer.Sound("splash.ogg")
match_sound = pygame.mixer.Sound("match.ogg")
creak_sound = pygame.mixer.Sound("creak.ogg")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mouse.set_visible(1)

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            # to start
            if room_num == -1 or room_num == 0:
                room_num += 1
            # Clicking will cause some text to disappear
            display_txt = None

            # Interactions with items and code pieces
            if magnifying_g.rect.collidepoint(pygame.mouse.get_pos()) and \
                    (magnifying_g.location == room_num or
                     inventory_list.has(magnifying_g)):
                if inventory_list.has(magnifying_g) is False:
                    magnifying_g.store('magnifying glass')
                    inventory_list.add(magnifying_g)
                else:
                    selected = magnifying_g
                    box1.image.fill(BLACK)

            if screwdriver.rect.collidepoint(pygame.mouse.get_pos()) and \
                    (screwdriver.location == room_num or
                     inventory_list.has(screwdriver)) and \
                    clock_door.get_alpha() == 0:
                if inventory_list.has(screwdriver) is False:
                    screwdriver.store('screwdriver')
                    inventory_list.add(screwdriver)
                else:
                    selected = screwdriver
                    box2.image.fill(BLACK)

            if recipe.rect.collidepoint(pygame.mouse.get_pos()) and \
                    (recipe.location == room_num or
                     inventory_list.has(recipe)):
                if room_num == 2:
                    display_txt = "recipe"
                if inventory_list.has(recipe) is False:
                    recipe.store('recipe')
                    inventory_list.add(recipe)
                else:
                    selected = recipe
                    box3.image.fill(BLACK)

            if matches.rect.collidepoint(pygame.mouse.get_pos()) and \
                    cupboard_list[1].get_alpha() == 0 and \
                    (matches.location == room_num or
                     inventory_list.has(matches)):
                if inventory_list.has(matches) is False:
                    matches.store('matches')
                    inventory_list.add(matches)
                else:
                    selected = matches
                    box4.image.fill(BLACK)

            # If you are holding an ingredient
            if hold is not None:
                if pygame.sprite.collide_rect(candle, box4):
                    candle.store('candle')
                    box4.image.fill(WHITE)
                hold = None
            elif tomato.rect.collidepoint(pygame.mouse.get_pos()) and \
                    tomato.location == 4 and tomato.location == room_num:
                hold = 'tomato'
            elif carrot.rect.collidepoint(pygame.mouse.get_pos()) and \
                    carrot.location == 4 and carrot.location == room_num:
                hold = 'carrot'
            elif carrot2.rect.collidepoint(pygame.mouse.get_pos()) and \
                    carrot2.location == 4 and carrot2.location == room_num:
                hold = 'carrot2'
            elif carrot3.rect.collidepoint(pygame.mouse.get_pos()) and \
                    carrot3.location == 4 and carrot3.location == room_num:
                hold = 'carrot3'

            if candle.rect.collidepoint(pygame.mouse.get_pos()) and \
                    candle.lit_candle is True and \
                    (candle.location == room_num or
                     inventory_list.has(candle)):
                if room_num == 22 and hold is None:
                    hold = 'candle'
                    candle.location = 22
                    box4.image.fill(BLACK)
                    inventory_list.remove(candle)
                if inventory_list.has(candle) is False:
                    candle.store('candle')
                    inventory_list.add(candle)
                else:
                    selected = candle
                    box4.image.fill(BLACK)

            if herb.rect.collidepoint(pygame.mouse.get_pos()) and \
                    (herb.location == room_num or
                     inventory_list.has(herb)) and \
                    display_box3_text is True:
                if inventory_list.has(herb) is False:
                    herb.store('herb')
                    inventory_list.add(herb)
                    if grab is True:
                        display_txt = "herb"
                        grab = False
                else:
                    selected = herb
                    box3.image.fill(BLACK)

            if pygame.sprite.collide_rect(tomato, pot) and \
                    tomato.location == 4:
                ingredients += 1
                splash_sound.play()
                add_to_room(tomato, 0)
            if pygame.sprite.collide_rect(carrot, pot) and \
                    carrot.location == 4:
                ingredients += 1
                splash_sound.play()
                add_to_room(carrot, 0)
            if pygame.sprite.collide_rect(carrot2, pot) and \
                    carrot2.location == 4:
                ingredients += 1
                splash_sound.play()
                add_to_room(carrot2, 0)
            if pygame.sprite.collide_rect(carrot3, pot) and \
                    carrot3.location == 4:
                ingredients += 1
                splash_sound.play()
                add_to_room(carrot3, 0)

            if chest.rect.collidepoint(pygame.mouse.get_pos()) and \
                    screws == 0 and \
                    selected is None and chest.location == room_num:
                chest.on_clicked('chest')
                screws = 1
            if note.rect.collidepoint(pygame.mouse.get_pos()) and \
                    note.location == room_num:
                display_txt = "note"
            if book.rect.collidepoint(pygame.mouse.get_pos()) and \
                    room_num == 11 and item_used_list.has(magnifying_g):
                show_morse = True
            if pot.rect.collidepoint(pygame.mouse.get_pos()) and \
                    room_num == 4 and recipe.location > 0:
                display_txt = "soup"
            # Panel interaction
            for i in range(len(button_list)):
                if button_list[i].rect.collidepoint(pygame.mouse.get_pos()) \
                        and room_num == 1:
                    ind = config_panel(i)
                    on_click(button_list[i].b_name, ind)

            if enter.rect.collidepoint(pygame.mouse.get_pos()) and \
                    room_num == 1:
                button_sound.play()
                code = getcode()

            # Placing an item in a room
            if selected is not None:
                if not (inventory.rect.collidepoint(pygame.mouse.get_pos())):
                    (selected.rect.x, selected.rect.y) = pygame.mouse.get_pos()
                    add_to_room(selected, room_num)
                    inventory_list.remove(selected)
                    item_clicked_list.add(selected)
                    box1.image.fill(WHITE)
                    box2.image.fill(WHITE)
                    box3.image.fill(WHITE)
                    box4.image.fill(WHITE)
                    selected = None

            if room_num == 4:
                for i in range(5):
                    if cupboard_list[i].get_rect(topleft=position_list[i])\
                            .collidepoint(pygame.mouse.get_pos()):
                        cupboard_list[i].set_alpha(0)

            if room_num == 2 and item_used_list.has(magnifying_g):
                if book1.get_rect(topleft=(57, 87))\
                        .collidepoint(pygame.mouse.get_pos()) \
                        and books_clicked == 0:
                    book1.set_alpha(100)
                    books_clicked = 1
                elif book2.get_rect(topleft=(62, 110))\
                        .collidepoint(pygame.mouse.get_pos()) \
                        and books_clicked == 1:
                    book2.set_alpha(100)
                    books_clicked = 2
                elif book3.get_rect(topleft=(272, 160))\
                        .collidepoint(pygame.mouse.get_pos()) \
                        and books_clicked == 2:
                    book3.set_alpha(100)
                    books_clicked = 3
                elif book4.get_rect(topleft=(292, 257))\
                        .collidepoint(pygame.mouse.get_pos()) \
                        and books_clicked == 3:
                    book4.set_alpha(100)
                    books_clicked = 4

            if room_num == 12:
                if minute_hand.get_rect(center=(197, 117))\
                        .collidepoint(pygame.mouse.get_pos()):
                    minute_hand = pygame.transform.rotate(minute_hand, 90)
                    turns += 1
                if turns == 4:
                    turns = 0
                if clock_door.get_rect(topleft=(138, 151))\
                        .collidepoint(pygame.mouse.get_pos()) \
                        and time == '12:45' and \
                        not (clock_door.get_alpha() == 0):
                    creak_sound.play()
                    clock_door.set_alpha(0)
            # room movement
            if arrow_right.rect.collidepoint(pygame.mouse.get_pos())\
                    and room_num % 10 < 4:
                room_num += 1
            if arrow_left.rect.collidepoint(pygame.mouse.get_pos())\
                    and room_num % 10 > 1:
                room_num -= 1
            if arrow_up.rect.collidepoint(pygame.mouse.get_pos())\
                    and room_num % 10 == 3 \
                    and room_num < 20:
                room_num += 10
            if arrow_down.rect.collidepoint(pygame.mouse.get_pos())\
                    and room_num % 10 == 3 \
                    and room_num > 10:
                room_num -= 10

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    # 'Hold' an ingredient by keeping it with the mouse
    if x < 650 and y < 250:
        if hold == 'tomato':
            tomato.rect.x = x
            tomato.rect.y = y
        elif hold == 'carrot':
            carrot.rect.x = x
            carrot.rect.y = y
        elif hold == 'carrot2':
            carrot2.rect.x = x
            carrot2.rect.y = y
        elif hold == 'carrot3':
            carrot3.rect.x = x
            carrot3.rect.y = y
        elif hold == 'candle':
            candle.rect.x = x - 10
            candle.rect.y = y - 10

    # Interactions
    if pygame.sprite.collide_rect(magnifying_g, note) and \
            note.location == room_num:
        item_used_list.add(magnifying_g)
    if pygame.sprite.collide_rect(screwdriver, chest) and \
            screws >= 1 and chest.location == room_num:
        chest.open(screws)
        screwdriver.rect.x = 250
        screwdriver.rect.y = 325
        screws += 1
    if pygame.sprite.collide_rect(recipe, pot):
        display_box3_text = True
        add_to_room(recipe, 0)
    if pygame.sprite.collide_rect(herb, pot) and \
            herb.location == 4:
        ingredients += 1
        splash_sound.play()
        add_to_room(herb, 0)
    if pygame.sprite.collide_rect(matches, candle) and \
            matches.location == room_num:
        candle.light()
        match_sound.play()
        add_to_room(matches, 0)

    if pygame.sprite.collide_rect(num1, candle) and \
            wall_num == 0:
        wall_num = 1
    if pygame.sprite.collide_rect(num2, candle) and \
            wall_num == 1:
        wall_num = 2
    if pygame.sprite.collide_rect(num3, candle) and \
            wall_num == 2:
        wall_num = 3
    if pygame.sprite.collide_rect(num4, candle) and \
            wall_num == 3:
        wall_num = 4
    if wall_num == 4:
        display_box4_text = True

    if screws > 3:
        item_used_list.add(screwdriver)

    overlap = pygame.sprite.groupcollide(item_list, arrow_list, False, False)
    for i in overlap:
        i.store(i.item_name)
        inventory_list.add(i)

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    if room_num == 22:
        screen.blit(pygame.image.load('rm_22.png'), [0, 0])
        dark = pygame.Surface((700, 300))
        dark.fill(pygame.color.Color('Grey'))
        lt_x = candle.rect.x
        lt_y = candle.rect.y
        if candle.lit_candle is True and candle.location == 22 \
                and candle.rect.y < 300:
            dark.blit(light, [lt_x, lt_y])
        screen.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    if room_num % 10 == 3:
        if room_num == 23:
            screen.fill((181, 198, 221))
        else:
            screen.blit(pygame.image.load('stairs.png'), [0, 0])

    if room_num == 4:
        screen.blit(pygame.image.load('kitchen.png'), [0, 0])
    elif room_num % 10 == 1:
        if room_num == 1:
            screen.blit(pygame.image.load('door.png'), [0, 0])
        else:
            screen.blit(pygame.image.load('storage_room.png'), [0, 0])
    elif room_num == 24:
        screen.blit(pygame.image.load('green_house.png'), [0, 0])
    elif room_num == 2:
        screen.blit(pygame.image.load('library.png'), [0, 0])
    elif room_num == 14:
        screen.blit(pygame.image.load('study.png'), [0, 0])

    # draw cupboards over items
    if room_num == 4:
        draw_room(4)
        screen.blit(cupboard_list[0], [237, 194])
        screen.blit(cupboard_list[1], [393, 194])
        screen.blit(cupboard_list[2], [544, 194])
        screen.blit(cupboard_list[3], [428, 6])
        screen.blit(cupboard_list[4], [560, 6])
        ingredients_list.draw(screen)

    if room_num == 2:
        screen.blit(book1, (57, 87))
        screen.blit(book2, (62, 110))
        screen.blit(book3, (272, 160))
        screen.blit(book4, (292, 257))

    if room_num == 12:
        screen.blit(pygame.image.load('hall.png'), (0, 0))
        screen.blit(hour_hand, (191, 97))
        if turns == 0:
            screen.blit(minute_hand, (196, 110))
            time = '12:15'
        elif turns == 1:
            screen.blit(minute_hand, (190, 97))
            time = '12:00'
        elif turns == 2:
            screen.blit(minute_hand, (172, 110))
            time = '12:45'
        elif turns == 3:
            screen.blit(minute_hand, (189, 114))
            time = '12:30'

    # Draw all the sprites
    common_sprites_list.draw(screen)
    inventory_list.draw(screen)
    if not room_num == 4:
        draw_room(room_num)
    if room_num == 12:
        screen.blit(clock_door, (142, 150))

    # Drawing the panel
    b_x = 296
    if room_num == 1:
        for i in range((len(panel_list))):
            b_font = pygame.font.SysFont("serif", 15)
            b_text = b_font.render(str(panel_list[i]), True, BLACK)
            screen.blit(b_text, [b_x, 145])
            b_x += 15

    # If code piece was taken
    if item_used_list.__contains__(magnifying_g):
        add_to_room(magnifying_g, 0)
        add_to_room(note, 0)
        if books_clicked == 4:
            display_box1_text = True
    if item_used_list.__contains__(screwdriver):
        display_box2_text = True
        add_to_room(screwdriver, 0)

    if display_box1_text is True:
        show_code(box1)
    if display_box2_text is True:
        show_code(box2)
    if display_box3_text is True:
        show_code(box3)
    if display_box4_text is True:
        show_code(box4)
        box4.image.fill(WHITE)
        add_to_room(candle, 0)

    # Interacting with the locking device
    if room_num == 1 and stage < 5:
        code_text = "locked"
    elif not room_num == 1:
        code_text = ""

    if not code == "":
        if code == "6138" and stage == 1:
            success_sound.play()
            timer = 20
            stage = 2
        elif code == "0492" and stage == 2:
            success_sound.play()
            timer = 20
            stage = 3
        elif code == "0314" and stage == 3:
            success_sound.play()
            timer = 20
            stage = 4
        elif code == "7058" and stage == 4:
            success_sound.play()
            lock.image = ulk_image.convert()
            stage = 5
            room_num = 25

    # Indicate the player is correct by showing green for a moment
    if timer > 0:
        lock.image = ulk_image.convert()
        timer -= 1
    elif timer == 0 and code_text == "locked":
        lock.image = lk_image.convert()

    display_text(code_text)
    if display_txt is not None:
        display_text(display_txt)

    if show_morse is True and room_num == 11:
        screen.blit(pygame.image.load('morse.png'), (270, 0))

    if room_num == -1:
        screen.blit(pygame.image.load('title_screen.png'), (0, 0))
    elif room_num == 0:
        screen.blit(pygame.image.load('instructions.png'), (0, 0))
    elif room_num == 25:
        screen.blit(pygame.image.load('end_screen.png'), (0, 0))

    pygame.display.update()
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
