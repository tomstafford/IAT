#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.00), March 21, 2014, at 14:01
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Store info about the experiment session
expName = 'IAT-1.3'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'', u'order': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\tom\\Dropbox\\university\\Leverhulme Project Grant\\expts\\IAT-1.3\\IAT-1.3.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1680, 1050), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "SetupCode"
SetupCodeClock = core.Clock()
#Order is specified by experimenter at start of experiment via dialogue box
order=int(expInfo['order']) #convert to integer

#Now counterbalance pro-stereotype vs anti-stereotype IAT blocks

#Default is pro-stereotypical - "Congruent" first
trainfiles=['cong_train.xlsx','incong_train.xlsx']
testfiles=['cong_test.xlsx','incong_test.xlsx']
trainlabelsL=['A = \nWhite','A = \nBlack']
trainlabelsR=['L = \nBlack','L = \nWhite']
testlabelsL=['A = \nWhite or \nPositive','A = \nBlack or \nPositive']
testlabelsR=['L = \nBlack or \nNegative','L = \nWhite or \nNegative']

if order==2:
    #Anti-stereotypical - "Incongruent" first
    trainfiles.reverse()
    testfiles.reverse()
    trainlabelsL.reverse()
    trainlabelsR.reverse()
    testlabelsL.reverse()
    testlabelsR.reverse()

if order is not (1 or 2):
    print "UNRECOGNISED ORDER CODE - please use 1 or 2 only"





#print "UNRECOGNISED ORDER CODE - please use 1 or 2 only"

#CREDITS

'''
Developed by Robin Scaife on the Leverhulme Trust "Bias and Blame" project 2014
Additional coding by Tom Stafford with thanks to Lily Fitzgibbon for advice
'''



# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text="You will be presented with words or images to classify into catogories using either the 'A' or 'L' key.\r\n\r\nTry to go as fast as possible while making as few mistakes as possible.\r\n\r\nPress the space bar to continue",    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Keep_in_mind"
Keep_in_mindClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='Keep in mind:\r\n\r\n1) Labels at the top of the screen indicate which catogory goes with which key.\r\n\r\n2) Each word or image has a correct catogory classification\r\n\r\n3) Keep your index fingers on the A and L keys to enable a rapid response.\r\n\r\n4) The test gives no results if you go slow- please try to go as fast as possible\r\n\r\nPress the space bar to continue',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Ready1"
Ready1Clock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text='Take note of the catogories\r\n\r\nPosition your index fingers\r\n\r\nPress the space bar to begin',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='A=Positive',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='L=Negative',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Training1"
Training1Clock = core.Clock()
Positive_label = visual.TextStim(win=win, ori=0, name='Positive_label',
    text='A=Positive',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
Negative_label = visual.TextStim(win=win, ori=0, name='Negative_label',
    text='L=Negative',    font='Arial',
    pos=[0.8,0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_3 = visual.ImageStim(win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)

# Initialize components for Routine "Feedback1"
Feedback1Clock = core.Clock()
msg=""

text_27 = visual.TextStim(win=win, ori=0, name='text_27',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_29 = visual.TextStim(win=win, ori=0, name='text_29',
    text='A=Positive',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_30 = visual.TextStim(win=win, ori=0, name='text_30',
    text='L=Negative',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Superloop_code"
Superloop_codeClock = core.Clock()


# Initialize components for Routine "Ready2"
Ready2Clock = core.Clock()
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='Take note of the catogories\r\n\r\nPosition your index fingers\r\n\r\nPress the space bar to begin',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='default text',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='default text',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Training2"
Training2Clock = core.Clock()
text_9 = visual.TextStim(win=win, ori=0, name='text_9',
    text='default text',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_10 = visual.TextStim(win=win, ori=0, name='text_10',
    text='default text',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.3, 0.3],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)

# Initialize components for Routine "Feedback2"
Feedback2Clock = core.Clock()
msg=""

text_28 = visual.TextStim(win=win, ori=0, name='text_28',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_31 = visual.TextStim(win=win, ori=0, name='text_31',
    text='default text',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_32 = visual.TextStim(win=win, ori=0, name='text_32',
    text='default text',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Ready3"
Ready3Clock = core.Clock()
text_11 = visual.TextStim(win=win, ori=0, name='text_11',
    text='Take note of the catogories\r\n\r\nPosition your index fingers\r\n\r\nPress the space bar to begin',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_12 = visual.TextStim(win=win, ori=0, name='text_12',
    text='default text',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_13 = visual.TextStim(win=win, ori=0, name='text_13',
    text='default text',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Non_congruent"
Non_congruentClock = core.Clock()
text_14 = visual.TextStim(win=win, ori=0, name='text_14',
    text='default text',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
text_15 = visual.TextStim(win=win, ori=0, name='text_15',
    text='default text',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)

# Initialize components for Routine "Feedback3"
Feedback3Clock = core.Clock()
msg=""
text_33 = visual.TextStim(win=win, ori=0, name='text_33',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_34 = visual.TextStim(win=win, ori=0, name='text_34',
    text='default text',    font='Arial',
    pos=[-0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text_35 = visual.TextStim(win=win, ori=0, name='text_35',
    text='default text',    font='Arial',
    pos=[0.8, 0.8], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "End_Thanks"
End_ThanksClock = core.Clock()
text_26 = visual.TextStim(win=win, ori=0, name='text_26',
    text='The End.\r\n\r\nThank you for your participation.',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "SetupCode"-------
t = 0
SetupCodeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

# keep track of which components have finished
SetupCodeComponents = []
for thisComponent in SetupCodeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "SetupCode"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = SetupCodeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SetupCodeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "SetupCode"-------
for thisComponent in SetupCodeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(text_2)
InstructionsComponents.append(key_resp_3)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Keep_in_mind"-------
t = 0
Keep_in_mindClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
Keep_in_mindComponents = []
Keep_in_mindComponents.append(text_3)
Keep_in_mindComponents.append(key_resp_4)
for thisComponent in Keep_in_mindComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Keep_in_mind"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Keep_in_mindClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # underestimates by a little under one frame
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Keep_in_mindComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Keep_in_mind"-------
for thisComponent in Keep_in_mindComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Ready1"-------
t = 0
Ready1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
Ready1Components = []
Ready1Components.append(text)
Ready1Components.append(key_resp_5)
Ready1Components.append(text_4)
Ready1Components.append(text_5)
for thisComponent in Ready1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Ready1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Ready1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Ready1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Ready1"-------
for thisComponent in Ready1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
Train_pos_neg = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\tom\\Dropbox\\university\\Leverhulme Project Grant\\expts\\IAT-1.3\\IAT-1.3.psyexp',
    trialList=data.importConditions('pos_neg_train.xlsx'),
    seed=None, name='Train_pos_neg')
thisExp.addLoop(Train_pos_neg)  # add the loop to the experiment
thisTrain_pos_neg = Train_pos_neg.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrain_pos_neg.rgb)
if thisTrain_pos_neg != None:
    for paramName in thisTrain_pos_neg.keys():
        exec(paramName + '= thisTrain_pos_neg.' + paramName)

for thisTrain_pos_neg in Train_pos_neg:
    currentLoop = Train_pos_neg
    # abbreviate parameter names if possible (e.g. rgb = thisTrain_pos_neg.rgb)
    if thisTrain_pos_neg != None:
        for paramName in thisTrain_pos_neg.keys():
            exec(paramName + '= thisTrain_pos_neg.' + paramName)
    
    #------Prepare to start Routine "Training1"-------
    t = 0
    Training1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image_3.setImage(os.path.join('stimuli',StimuliImages))
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    Training1Components = []
    Training1Components.append(Positive_label)
    Training1Components.append(Negative_label)
    Training1Components.append(image_3)
    Training1Components.append(key_resp_2)
    for thisComponent in Training1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Training1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Training1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Positive_label* updates
        if t >= 0.0 and Positive_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            Positive_label.tStart = t  # underestimates by a little under one frame
            Positive_label.frameNStart = frameN  # exact frame index
            Positive_label.setAutoDraw(True)
        
        # *Negative_label* updates
        if t >= 0.0 and Negative_label.status == NOT_STARTED:
            # keep track of start time/frame for later
            Negative_label.tStart = t  # underestimates by a little under one frame
            Negative_label.frameNStart = frameN  # exact frame index
            Negative_label.setAutoDraw(True)
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'l'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(CorrAns1)) or (key_resp_2.keys == CorrAns1):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Training1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Training1"-------
    for thisComponent in Training1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
       # was no response the correct answer?!
       if str(CorrAns1).lower() == 'none': key_resp_2.corr = 1  # correct non-response
       else: key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for Train_pos_neg (TrialHandler)
    Train_pos_neg.addData('key_resp_2.keys',key_resp_2.keys)
    Train_pos_neg.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        Train_pos_neg.addData('key_resp_2.rt', key_resp_2.rt)
    
    #------Prepare to start Routine "Feedback1"-------
    t = 0
    Feedback1Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if key_resp_2.corr==0:
        msg="oops"
    elif key_resp_2.corr==1:
        msg=""
    
    text_27.setText(msg)
    # keep track of which components have finished
    Feedback1Components = []
    Feedback1Components.append(text_27)
    Feedback1Components.append(text_29)
    Feedback1Components.append(text_30)
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Feedback1"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_27* updates
        if t >= 0.0 and text_27.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_27.tStart = t  # underestimates by a little under one frame
            text_27.frameNStart = frameN  # exact frame index
            text_27.setAutoDraw(True)
        elif text_27.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_27.setAutoDraw(False)
        
        # *text_29* updates
        if t >= 0.0 and text_29.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_29.tStart = t  # underestimates by a little under one frame
            text_29.frameNStart = frameN  # exact frame index
            text_29.setAutoDraw(True)
        elif text_29.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_29.setAutoDraw(False)
        
        # *text_30* updates
        if t >= 0.0 and text_30.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_30.tStart = t  # underestimates by a little under one frame
            text_30.frameNStart = frameN  # exact frame index
            text_30.setAutoDraw(True)
        elif text_30.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_30.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Feedback1"-------
    for thisComponent in Feedback1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'Train_pos_neg'


# set up handler to look after randomisation of conditions etc
superloop = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath='C:\\Users\\tom\\Dropbox\\university\\Leverhulme Project Grant\\expts\\IAT-1.3\\IAT-1.3.psyexp',
    trialList=[None],
    seed=None, name='superloop')
thisExp.addLoop(superloop)  # add the loop to the experiment
thisSuperloop = superloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisSuperloop.rgb)
if thisSuperloop != None:
    for paramName in thisSuperloop.keys():
        exec(paramName + '= thisSuperloop.' + paramName)

for thisSuperloop in superloop:
    currentLoop = superloop
    # abbreviate parameter names if possible (e.g. rgb = thisSuperloop.rgb)
    if thisSuperloop != None:
        for paramName in thisSuperloop.keys():
            exec(paramName + '= thisSuperloop.' + paramName)
    
    #------Prepare to start Routine "Superloop_code"-------
    t = 0
    Superloop_codeClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    #Set stimuli files and labels according to this is the 1st or 2nd time we are here
    testblockfile=testfiles[superloop.thisRepN]
    trainblockfile=trainfiles[superloop.thisRepN]
    trainlabelL=trainlabelsL[superloop.thisRepN]
    trainlabelR=trainlabelsR[superloop.thisRepN]
    testlabelL=testlabelsL[superloop.thisRepN]
    testlabelR=testlabelsR[superloop.thisRepN]
    
    # keep track of which components have finished
    Superloop_codeComponents = []
    for thisComponent in Superloop_codeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Superloop_code"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Superloop_codeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Superloop_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Superloop_code"-------
    for thisComponent in Superloop_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "Ready2"-------
    t = 0
    Ready2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    text_7.setText(trainlabelL)
    text_8.setText(trainlabelR)
    # keep track of which components have finished
    Ready2Components = []
    Ready2Components.append(text_6)
    Ready2Components.append(key_resp_6)
    Ready2Components.append(text_7)
    Ready2Components.append(text_8)
    for thisComponent in Ready2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Ready2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Ready2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # underestimates by a little under one frame
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t  # underestimates by a little under one frame
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Ready2"-------
    for thisComponent in Ready2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    Train_target_stimuli = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath='C:\\Users\\tom\\Dropbox\\university\\Leverhulme Project Grant\\expts\\IAT-1.3\\IAT-1.3.psyexp',
        trialList=data.importConditions(trainblockfile),
        seed=None, name='Train_target_stimuli')
    thisExp.addLoop(Train_target_stimuli)  # add the loop to the experiment
    thisTrain_target_stimulu = Train_target_stimuli.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrain_target_stimulu.rgb)
    if thisTrain_target_stimulu != None:
        for paramName in thisTrain_target_stimulu.keys():
            exec(paramName + '= thisTrain_target_stimulu.' + paramName)
    
    for thisTrain_target_stimulu in Train_target_stimuli:
        currentLoop = Train_target_stimuli
        # abbreviate parameter names if possible (e.g. rgb = thisTrain_target_stimulu.rgb)
        if thisTrain_target_stimulu != None:
            for paramName in thisTrain_target_stimulu.keys():
                exec(paramName + '= thisTrain_target_stimulu.' + paramName)
        
        #------Prepare to start Routine "Training2"-------
        t = 0
        Training2Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        text_9.setText(trainlabelL)
        text_10.setText(trainlabelR)
        image.setImage(os.path.join('stimuli',TrialImages))
        key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_7.status = NOT_STARTED
        # keep track of which components have finished
        Training2Components = []
        Training2Components.append(text_9)
        Training2Components.append(text_10)
        Training2Components.append(image)
        Training2Components.append(key_resp_7)
        for thisComponent in Training2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Training2"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = Training2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_9* updates
            if t >= 0.0 and text_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_9.tStart = t  # underestimates by a little under one frame
                text_9.frameNStart = frameN  # exact frame index
                text_9.setAutoDraw(True)
            
            # *text_10* updates
            if t >= 0.0 and text_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_10.tStart = t  # underestimates by a little under one frame
                text_10.frameNStart = frameN  # exact frame index
                text_10.setAutoDraw(True)
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # underestimates by a little under one frame
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            
            # *key_resp_7* updates
            if t >= 0.0 and key_resp_7.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_7.tStart = t  # underestimates by a little under one frame
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                key_resp_7.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_7.status == STARTED:
                theseKeys = event.getKeys(keyList=['a', 'l'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_7.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_7.rt = key_resp_7.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_7.keys == str(CorrAns)) or (key_resp_7.keys == CorrAns):
                        key_resp_7.corr = 1
                    else:
                        key_resp_7.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Training2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Training2"-------
        for thisComponent in Training2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
           key_resp_7.keys=None
           # was no response the correct answer?!
           if str(CorrAns).lower() == 'none': key_resp_7.corr = 1  # correct non-response
           else: key_resp_7.corr = 0  # failed to respond (incorrectly)
        # store data for Train_target_stimuli (TrialHandler)
        Train_target_stimuli.addData('key_resp_7.keys',key_resp_7.keys)
        Train_target_stimuli.addData('key_resp_7.corr', key_resp_7.corr)
        if key_resp_7.keys != None:  # we had a response
            Train_target_stimuli.addData('key_resp_7.rt', key_resp_7.rt)
        
        #------Prepare to start Routine "Feedback2"-------
        t = 0
        Feedback2Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if key_resp_7.corr==0:
            msg="oops"
        elif key_resp_7.corr==1:
            msg=""
        
        text_28.setText(msg)
        text_31.setText(trainlabelL)
        text_32.setText(trainlabelR)
        # keep track of which components have finished
        Feedback2Components = []
        Feedback2Components.append(text_28)
        Feedback2Components.append(text_31)
        Feedback2Components.append(text_32)
        for thisComponent in Feedback2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback2"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Feedback2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_28* updates
            if t >= 0.0 and text_28.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_28.tStart = t  # underestimates by a little under one frame
                text_28.frameNStart = frameN  # exact frame index
                text_28.setAutoDraw(True)
            elif text_28.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_28.setAutoDraw(False)
            
            # *text_31* updates
            if t >= 0.0 and text_31.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_31.tStart = t  # underestimates by a little under one frame
                text_31.frameNStart = frameN  # exact frame index
                text_31.setAutoDraw(True)
            elif text_31.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_31.setAutoDraw(False)
            
            # *text_32* updates
            if t >= 0.0 and text_32.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_32.tStart = t  # underestimates by a little under one frame
                text_32.frameNStart = frameN  # exact frame index
                text_32.setAutoDraw(True)
            elif text_32.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_32.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback2"-------
        for thisComponent in Feedback2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Train_target_stimuli'
    
    
    #------Prepare to start Routine "Ready3"-------
    t = 0
    Ready3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_8 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_8.status = NOT_STARTED
    text_12.setText(testlabelL)
    text_13.setText(testlabelR)
    # keep track of which components have finished
    Ready3Components = []
    Ready3Components.append(text_11)
    Ready3Components.append(key_resp_8)
    Ready3Components.append(text_12)
    Ready3Components.append(text_13)
    for thisComponent in Ready3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Ready3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Ready3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t  # underestimates by a little under one frame
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t  # underestimates by a little under one frame
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t  # underestimates by a little under one frame
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t  # underestimates by a little under one frame
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ready3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Ready3"-------
    for thisComponent in Ready3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    Test_associations = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath='C:\\Users\\tom\\Dropbox\\university\\Leverhulme Project Grant\\expts\\IAT-1.3\\IAT-1.3.psyexp',
        trialList=data.importConditions(testblockfile),
        seed=None, name='Test_associations')
    thisExp.addLoop(Test_associations)  # add the loop to the experiment
    thisTest_association = Test_associations.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTest_association.rgb)
    if thisTest_association != None:
        for paramName in thisTest_association.keys():
            exec(paramName + '= thisTest_association.' + paramName)
    
    for thisTest_association in Test_associations:
        currentLoop = Test_associations
        # abbreviate parameter names if possible (e.g. rgb = thisTest_association.rgb)
        if thisTest_association != None:
            for paramName in thisTest_association.keys():
                exec(paramName + '= thisTest_association.' + paramName)
        
        #------Prepare to start Routine "Non_congruent"-------
        t = 0
        Non_congruentClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        text_14.setText(testlabelL)
        text_15.setText(testlabelR)
        image_2.setImage(os.path.join('stimuli',TrialImages))
        key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_9.status = NOT_STARTED
        # keep track of which components have finished
        Non_congruentComponents = []
        Non_congruentComponents.append(text_14)
        Non_congruentComponents.append(text_15)
        Non_congruentComponents.append(image_2)
        Non_congruentComponents.append(key_resp_9)
        for thisComponent in Non_congruentComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Non_congruent"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = Non_congruentClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_14* updates
            if t >= 0.0 and text_14.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_14.tStart = t  # underestimates by a little under one frame
                text_14.frameNStart = frameN  # exact frame index
                text_14.setAutoDraw(True)
            
            # *text_15* updates
            if t >= 0.0 and text_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_15.tStart = t  # underestimates by a little under one frame
                text_15.frameNStart = frameN  # exact frame index
                text_15.setAutoDraw(True)
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # underestimates by a little under one frame
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            
            # *key_resp_9* updates
            if t >= 0.0 and key_resp_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_9.tStart = t  # underestimates by a little under one frame
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                key_resp_9.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_9.status == STARTED:
                theseKeys = event.getKeys(keyList=['a', 'l'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_9.rt = key_resp_9.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_9.keys == str(CorrAns)) or (key_resp_9.keys == CorrAns):
                        key_resp_9.corr = 1
                    else:
                        key_resp_9.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Non_congruentComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Non_congruent"-------
        for thisComponent in Non_congruentComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
           key_resp_9.keys=None
           # was no response the correct answer?!
           if str(CorrAns).lower() == 'none': key_resp_9.corr = 1  # correct non-response
           else: key_resp_9.corr = 0  # failed to respond (incorrectly)
        # store data for Test_associations (TrialHandler)
        Test_associations.addData('key_resp_9.keys',key_resp_9.keys)
        Test_associations.addData('key_resp_9.corr', key_resp_9.corr)
        if key_resp_9.keys != None:  # we had a response
            Test_associations.addData('key_resp_9.rt', key_resp_9.rt)
        
        #------Prepare to start Routine "Feedback3"-------
        t = 0
        Feedback3Clock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if key_resp_9.corr==0:
            msg="oops"
        elif key_resp_9.corr==1:
            msg=""
        
        text_33.setText(msg)
        text_34.setText(testlabelL)
        text_35.setText(testlabelR)
        # keep track of which components have finished
        Feedback3Components = []
        Feedback3Components.append(text_33)
        Feedback3Components.append(text_34)
        Feedback3Components.append(text_35)
        for thisComponent in Feedback3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback3"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Feedback3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text_33* updates
            if t >= 0.0 and text_33.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_33.tStart = t  # underestimates by a little under one frame
                text_33.frameNStart = frameN  # exact frame index
                text_33.setAutoDraw(True)
            elif text_33.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_33.setAutoDraw(False)
            
            # *text_34* updates
            if t >= 0.0 and text_34.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_34.tStart = t  # underestimates by a little under one frame
                text_34.frameNStart = frameN  # exact frame index
                text_34.setAutoDraw(True)
            elif text_34.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_34.setAutoDraw(False)
            
            # *text_35* updates
            if t >= 0.0 and text_35.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_35.tStart = t  # underestimates by a little under one frame
                text_35.frameNStart = frameN  # exact frame index
                text_35.setAutoDraw(True)
            elif text_35.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_35.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Feedback3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback3"-------
        for thisComponent in Feedback3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'Test_associations'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'superloop'


#------Prepare to start Routine "End_Thanks"-------
t = 0
End_ThanksClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
# keep track of which components have finished
End_ThanksComponents = []
End_ThanksComponents.append(text_26)
for thisComponent in End_ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End_Thanks"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = End_ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    if t >= 0.0 and text_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_26.tStart = t  # underestimates by a little under one frame
        text_26.frameNStart = frameN  # exact frame index
        text_26.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "End_Thanks"-------
for thisComponent in End_ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)





win.close()
core.quit()
