import pygame 
from pygame.locals import * 
pygame.init()
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# WINDOW 
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
displayScreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Digit Classifier")

# CONSTANTS 
SQUARE_SIDE = 40

# FONTS 
RIGHTEOUS = pygame.font.Font("Righteous-Regular.ttf", 400)

# FUNCTIONS 
def drawWin():
    displayScreen.fill(WHITE)
    
def paintWin():
    mos_x, mos_y = pygame.mouse.get_pos()
    pygame.draw.rect(displayScreen, BLACK, (mos_x, mos_y, SQUARE_SIDE, SQUARE_SIDE))

def getWindowScrshot():
    screenshot = displayScreen.copy()
    pygame.image.save(screenshot, "last.png")

def showText(n):
    text = RIGHTEOUS.render(f"{n}", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
    displayScreen.blit(text, text_rect)

def makePrediction():
    # Load the model
    model = load_model('keras_model.h5')
    # Create the array to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Getting saved image
    image = Image.open('last.png')
    # Resizing image and cropping 
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    # Turning image to numpy array
    image_array = np.asarray(image)
    # Normalizing image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array
    # Run inference
    prediction = model.predict(data)
    # Getting maximum confidence label
    label = np.argmax(prediction[0])
    # Returning label
    return label

# PROGRAM LOOP 
running = True 
pressed = False
TICK = 25
drawWin()
while running:
    pygame.time.delay(TICK)

    # EVENT VARIABLES
    for event in pygame.event.get():
        if (event.type==QUIT): # QUIT WINDOW
            running = False
        if (event.type==pygame.MOUSEBUTTONDOWN): 
            pressed = True 
        if (event.type==pygame.MOUSEBUTTONUP):
            pressed = False
    
    # IF MOUSE BUTTON IS DOWN 
    if pressed:
        paintWin()

    # KEYBOARD DRIVEN SCREEN COMMANDS 
    keys = pygame.key.get_pressed()
    if keys[K_1]: # CLEAR SCREEN 
        drawWin()
    if keys[K_2]: # RUN MODEL 
        getWindowScrshot() # GETTING SCREENSHOT
        drawWin() # CLEAR SCREEN
        label = makePrediction() # GETTING DIGIT
        showText(label) # BLITTING PREDICTION
    
    pygame.display.update()