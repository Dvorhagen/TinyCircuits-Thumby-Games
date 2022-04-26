## By Aaron Feinstein, University of Connecticut dept. of Molecular and Cell Biology 




import time
import math
import thumby
import builtins
import gc

gc.enable()

#init display
thumby.DISPLAY_W = 72
thumby.DISPLAY_H = 40


#splash image: width: 32, height: 32
# BITMAP: width: 32, height: 32
bitmap0 = bytearray([0,0,0,64,128,0,0,64,128,0,0,128,64,64,192,32,0,128,64,64,192,32,0,0,0,0,0,0,0,0,0,0,
           0,0,16,240,227,180,50,164,195,0,128,67,69,5,133,64,128,3,5,133,197,32,128,64,64,0,64,192,64,128,0,0,
           0,0,0,31,15,1,3,31,48,32,99,69,196,64,199,193,71,72,67,68,71,96,163,181,148,128,128,135,193,102,48,0,
           0,0,0,0,0,0,0,0,12,12,4,2,1,2,6,13,9,1,1,1,1,1,2,12,24,0,0,0,0,3,0,0])
           
# Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
SplashScreen = thumby.Sprite(32, 32, bitmap0)

# Set the FPS (without this call, the default fps is 30)
thumby.display.setFPS(60)

def show_title():
    while(1):
        t0 = time.ticks_ms()   # Get time (ms)
        thumby.display.fill(0) # Fill canvas to black
    # As time goes on create a vertical offset using the sin function. The offset will move the sprite up and down 5px.
        bobRate = 250 # Set arbitrary bob rate (higher is slower)
        bobRange = 8  # How many pixels to move the sprite up/down (-5px ~ 5px)
    # Calculate number of pixels to offset sprite for bob animation
        bobOffset = math.sin(t0 / bobRate) * bobRange
    # Center the sprite using screen and bitmap dimensions and apply bob offset
        SplashScreen.x = int((thumby.display.width/2) - (32/2))
        SplashScreen.y = int(round((thumby.display.height/2) - (32/2) + bobOffset))
    # Display the bitmap using bitmap data, position, and bitmap dimensions
        thumby.display.drawSprite(SplashScreen)
        thumby.display.update()
        if(thumby.buttonA.justPressed()):
            break
        
def read_chunks(filename, chunk_size):
#"local" globals
    pages=0
    bookmark=0
    index=0
    index2=0
    count_lines=0
    maxlines=100
    lines=[]
    chunk=[]
    cur_line=[]
    words=[]
    indiv_words=[]
    enumerated=[]
    lines=[]
    save_count=0
 
 #Flip to a desired location....  
    thumby.display.setFPS(60)
    thumby.display.fill(0)
    thumby.display.update()
    thumby.display.drawText('Bookmark?\n', 0, 0, 1)
    thumby.display.drawText("A to skip", 0, 9, 1)
    thumby.display.drawText("U, D -10s", 0, 18, 1)
    thumby.display.drawText("L, R -100s", 0, 27, 1)
    thumby.display.update()
    
    while(1):
        if thumby.buttonU.pressed():
            bookmark += 10
            thumby.display.fill(0)
            thumby.display.update()
            thumby.display.drawText(str(bookmark), 0, 9, 1)
            thumby.display.update()
        if thumby.buttonR.pressed():
            bookmark += 100
            thumby.display.fill(0)
            thumby.display.update()
            thumby.display.drawText(str(bookmark), 0, 9, 1)
            thumby.display.update()
        if thumby.buttonD.pressed() and bookmark > 0:
            thumby.display.fill(0)
            thumby.display.update()
            bookmark -= 10
            thumby.display.drawText(str(bookmark), 0, 0, 1)
            thumby.display.update()
        if thumby.buttonL.pressed():
            bookmark -= 100
            thumby.display.fill(0)
            thumby.display.update()
            thumby.display.drawText(str(bookmark), 0, 9, 1)
            thumby.display.update()
        if thumby.buttonA.justPressed():
            break

#Read finite, small chunks of text so that your memory doesn't scream at you    
    with open(filename) as f:
        
        if bookmark == 0:
            while count_lines <= maxlines:
                chunk.append(f.readline())
                count_lines += 1
        else:
            while count_lines <= maxlines:
                if save_count < bookmark:
                    save_count += 1
                    chunk=[]
                    chunk.append(f.readline())
                if save_count == bookmark:
                    chunk.append(f.readline())
                    count_lines += 1
          
                
  
        index = 0
        while index <= maxlines:
            lines.append(chunk[index].split())
            index += 1
        
        index=0
        index2=0
        for x in lines:
            cur_line = x
            for i in cur_line:
                indiv_words.append(i)
        pages += 1
    
        thumby.display.setFPS(5)
        wc = 0
        screen_count = 0
        word = str(indiv_words[wc])
        thumby.display.fill(0)
        thumby.display.update()
        thumby.display.drawText(word, 0, 0, 1)
        thumby.display.update()
        
       
        while(1): #main loop
            screen_count=1
            while screen_count <= 4:
                if thumby.buttonR.justPressed() or thumby.buttonD.pressed():
                    wc += 1
                    
                    if wc >= len(indiv_words):
                        indiv_words=[]
                        chunk=[]
                        lines=[]
                        wc=0
                        count_lines=0
                        while count_lines <= maxlines:
                            chunk.append(f.readline())
                            count_lines += 1
                            #print(chunk)    
                        index = 0
                        while index <= maxlines:
                            lines.append(chunk[index].split())
                            index += 1
                        index=0
                        index2=0
                        for x in lines:
                            cur_line = x
                            for i in cur_line:
                                indiv_words.append(i)
                        bookmark += 1
                        
                    word = str(indiv_words[wc])
                    if indiv_words.index(word) == -1:
                        return
                
                    thumby.display.drawText(word, 0, 9*(screen_count), 1)
                    thumby.display.update()
                    screen_count += 1
                    if screen_count == 4:
                        screen_count = 0
                        thumby.display.fill(0)
    
                if(thumby.buttonB.justPressed()):
                    location = 'Loc:\n {}'.format(bookmark)
                    thumby.display.fill(0)
                    thumby.display.update()
                    thumby.display.drawText(location, 0, 0, 1)
                    thumby.display.update()
                
                if(thumby.buttonU.pressed()):    
                    return
        
                if(thumby.buttonL.pressed()) and wc >= 0:
                    screen_count = 0
                    thumby.display.fill(0)
                    wc -= 1
                    word = str(indiv_words[wc])
                    thumby.display.drawText(word, 0, 0, 1)
                    thumby.display.update() 
    return 
        
            
            
show_title()
read_chunks("/Games/wee-read/alice_gut.txt", 3)
