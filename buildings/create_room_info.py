import os
import sys

args = sys.argv

if len(args) != 2:
	print('usage: python3 create_room_info.py <Building>')

building = args[1]

for floor in os.listdir(building):
	for room in os.listdir(building + '/' + floor):
		if room == 'floor_plan.jpg':
			continue
		os.system('touch "' + building + '/' + floor + '/' + room + '/info.json"')