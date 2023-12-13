from psychopy import visual, core, event, clock
from psychopy.hardware import keyboard
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import visual, core, event, sound
from psychopy.hardware import keyboard
import psychtoolbox as ptb
import random 



#create a window
mywin = visual.Window(fullscr=True, color=(-1,-1,-1), colorSpace='rgb', allowGUI=True, monitor="testMonitor", units="pix")

#Create message
text = visual.TextBox2(win=mywin, text='Presione el botón cuando escuche un beep', font='Arial', pos=[0,0], color=(1,1,1), letterHeight=50, units='pix', anchor='center')



#Create sound stimuli
theSound = sound.backend_ptb.SoundPTB('A', loops=-1)


#create a keyboard component
kb = keyboard.Keyboard()

rand = random.randint(5, 10) #Wait random seconds

#draw the stimuli and update the window
while True: #this creates a never-ending loop
    text.setAutoDraw(False)  # Do not draw automatically
    text.draw() #Place text
    mywin.flip() 
    core.wait(3.0) #show text for 3 seconds


    for y in range(0,10):
        theSound.play() 
        mywin.flip() 
        core.wait(rand)
        theSound.stop()
        
   
    
    #Start again  


    if len(kb.getKeys()) > 0:
        break
    event.clearEvents()

#cleanup
mywin.close()
core.quit()


