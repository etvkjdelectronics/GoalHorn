import hardware_interface
import subprocess

"""
GPIO Summary:
GPIO 17: Goal light (Active Low) 
"""
GPIO_GOAL_LIGHT = 17

def goal(path):
    hardware_interface.write_gpio(GPIO_GOAL_LIGHT, 0) #Turn on goal light
    print("GOAL!!!")
    time.sleep(0.25)
    subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
    time.sleep(11.75)
    hardware_interface.write_gpio(GPIO_GOAL_LIGHT, 1) #Turn off goal light
    print(READY_STRING)

def penalty(path):
	print("Penalty! B-O-X!")
	hardware_interface.write_gpio(GPIO_GOAL_LIGHT, 0) #Turn on goal light
	subprocess.Popen("aplay -D plughw:0,1 " + path, shell=True)
	time.sleep(6)
	hardware_interface.write_gpio(GPIO_GOAL_LIGHT, 1) #Turn off goal light
	print(READY_STRING)