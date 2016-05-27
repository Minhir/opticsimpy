from opticsim import *


data_file = open('data.dat', 'w')
laser_light = light.LinearlyPolarizedHorizontal()
for i in range(180):
    pokkels = elements.LinearRetarder(i)
    for j in range(0, 360, 3):
        linear_polarizer = elements.LinearPolarizer(j)
        s = system.System()
        s.add_elements(pokkels, linear_polarizer)
        changed_light = s.count(laser_light)
        data_file.write(str(i) + '  ' + str(changed_light.I) + '    ' + str(j) + '\n')
data_file.close()
