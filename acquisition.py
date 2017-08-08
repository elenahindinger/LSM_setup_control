import zmq
import time
from zmq_class import ZmqLightsheetTrigger

zmq = ZmqLightsheetTrigger(pause=0, tcp_address='tcp://192.168.233.184:5555')

imaging_duration = 1200
# enter your duration of imaging per time point in seconds
pause_duration = 1
no_sesh = 1
total = (imaging_duration + pause_duration) * (no_sesh - 1) + imaging_duration
print ('Total Time is ' + str(total) + ' seconds.')
time.sleep(5)
# calculates total number of frames to be entered in hokawo
# total = (imaging_duration * 60) + 57
# print ('Total number of frames is ' + str(total))
# time.sleep(20)

def imaging_sesh(seshlength, pauselength, trial):
    if trial != 0:
        print ('Imaging time point ' + str(trial))
    else:
        pass
    zmq.start_command()
    time.sleep(seshlength)
    zmq.prepare()
    print('break time')
    # break in between imaging sessions
    time.sleep(pauselength)

zmq.prepare()
print('TURN ON CAMERA NOW')
time.sleep(10)
# imaging_sesh(1, 5, 0) # this is essential, do not delete

''' last session, has to always be pauselength 1sec, but do not count this in hokawo '''

#imaging_sesh(imaging_duration, pause_duration, 1)

imaging_sesh(imaging_duration, 1, 1)


# end of protocol
zmq.start_command()
zmq.stop()
print('Acquisition finished.')



"PyQT for stimulus, use version 4"