# It's first version if this program. In this version i have only definite
# array. And can't correct work with walls.

import numpy as np

area = np.array([[0, 0, 0, 0],
                 [0, 0, 0, 2],
                 [1, 0, 0, 0],
                 [0, 0, 0, 0]])

print(area, "\n")

hero = np.where(area == 1)  #get coordinates of hero
point = np.where(area == 2) #get coordintes of point

while hero[0] != point[0]:

    if hero[0] > point[0]:
        area[hero[0] - 1, hero[1]] = 1
        area[hero[0], hero[1]] = 0
        print(area, "\n")                   
                                    # make one step up or down
    elif hero[0] < point[0]:
        area[hero[0] + 1, hero[1]] = 1
        area[hero[0], hero[1]] = 0
        print(area, "\n")

    hero = np.where(area == 1)  #get coordinates of hero

while hero[1] != point[1]:

    if hero[1] > point[1]:
        area[hero[0], hero[1] - 1] = 1
        area[hero[0], hero[1]] = 0
        print(area, "\n")                   
                                    # make one step right or left 
    elif hero[1] < point[1]:
        area[hero[0], hero[1] + 1] = 1
        area[hero[0], hero[1]] = 0
        print(area, "\n")

    hero = np.where(area == 1)  #get coordinates of hero



