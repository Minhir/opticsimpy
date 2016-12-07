from opticsim import *


data_file = open('data.dat', 'w')
laser_light = light.LinearlyPolarizedM45()

for i in range(180):
    pokkels = elements.LinearRetarder(0, i)
    for j in range(0, 180):
        linear_polarizer = elements.LinearPolarizer(j)
        s = system.System()
        s.add_elements(pokkels, linear_polarizer)
        changed_light = s.count(laser_light)
        data_file.write(str(180 * i + j) + '    ' + str(changed_light.I) + '    ' + str(i / 180) + '\n')

data_file.close()
