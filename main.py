import spacenavigator
import time
import udp_client
from threading import Thread
import matplotlib.pyplot as plt
import math
sender = udp_client.Sender()

thread1 = Thread(target=sender.send_date)
thread1.start()

def value_changer(val):
    a = 1

    if math.fabs(val) <= 0.1:
      return 0
    if val < 0:
      a = -1
    if math.fabs(val) >= 0.6:
      return 1 * a
    
    return val / 0.6

# fig = plt.figure()
# arr_x = []
# arr_y = []
# arr_z = []

success = spacenavigator.open()
if success:
  while 1:
    state = spacenavigator.read()
    # print(0, value_changer(state.x), value_changer(state.y), value_changer(state.z), 
    #         value_changer(state.pitch),value_changer(state.roll), value_changer(state.yaw), state.buttons[0], state.buttons[1])
    sender.change_value(0, value_changer(state.x), value_changer(state.y), value_changer(state.z), 
            value_changer(state.pitch),value_changer(state.roll), value_changer(state.yaw), state.buttons[0], state.buttons[1])

    if state.buttons[0] == 1:
      sender.send_button('btn1')
    if state.buttons[1] == 1:
      sender.send_button('btn2')
    