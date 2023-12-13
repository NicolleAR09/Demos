from psychopy import visual, core, event, clock
from psychopy.hardware import keyboard
import random
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import visual, core, event, sound
from psychopy.hardware import keyboard





#create a window
mywin = visual.Window(fullscr=True, color=(-1,-1,-1), colorSpace='rgb', allowGUI=True, monitor="testMonitor", units="pix")

#Create message
text = visual.TextBox2(win=mywin, text='Mire el cuadro blanco en pantalla', font='Arial', pos=[0,0], color=(1,1,1), letterHeight=50, units='pix', anchor='center')

#Create message
text2 = visual.TextBox2(win=mywin, text='Presione el botón cuando escuche un beep', font='Arial', pos=[0,0], color=(1,1,1), letterHeight=50, units='pix', anchor='center')


#create visual stimuli
#square = visual.GratingStim(win=mywin, size=100, pos=[-633,334], sf=1) #Fix for every kind of window
square = visual.Rect(win=mywin, width=200, height=200, pos=[-633,334], fillColor=(1,1,1))

square2 = visual.Rect(win=mywin, width=400, height=400, pos=[0,0], fillColor=(1,1,1))



#Create sound stimuli
theSound = sound.backend_ptb.SoundPTB('A', loops=-1)


#create a keyboard component
kb = keyboard.Keyboard()



#draw the stimuli and update the window
while True: #this creates a never-ending loop
    text.setAutoDraw(False)  # Do not draw automatically
    text.draw() #Place text Visual
    mywin.flip() 
    core.wait(3.0) #show text for 3 seconds

    #20Hz -> 20 impulses per second, 0.025 seconds each black and white 
    #1: 0.025 seconds

    rand = random.randint(5, 10) #Wait random seconds

    for x in range(0,10): #repeat 10 times

        for j in range(0,5): #for 5 seconds 
        
            for i in range(0,20):
                square.draw() #draw square
                square2.draw()
                mywin.flip()
                core.wait(0.025) #show square for 0.025 second
                mywin.flip()  # flip without drawing
                core.wait(0.025) #Wait 0.025 seconds 

        core.wait(rand) #Wait random seconds 

    text2.setAutoDraw(False)  # Do not draw automatically
    text2.draw() #Place text Audio 
    mywin.flip() 
    core.wait(3.0) #show text for 3 seconds


    for y in range(0,10):
        theSound.play() 
        mywin.flip() 
        core.wait(random.randint(5, 10))
        theSound.stop()


    
    #Start again  
        



    if len(kb.getKeys()) > 0:
        break
    event.clearEvents()

#cleanup
mywin.close()
core.quit()


