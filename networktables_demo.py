# https://github.com/robotpy/pynetworktables
import time
from networktables import NetworkTables

NetworkTables.initialize()
sd = NetworkTables.getTable('SmartDashboard')

i = 0
while True:
	sd.putValue('x', [i, 0])
	i += 1
	time.sleep(1)
