#Work in Progress

#Hier stehen in einem Outline die main-functions eines Roboters

class robot:
    robot_rotation = 0 #Wie Himmelsrichtungen: 1=N, 2=O, 3=S, 4=W
    robot_position = [0, 0] #Koordinatensystem mit x,y

    def turn_right(): #Roboter dreht sich nach rechts
        robot_rotation += 1 #siehe oben, Rechtskurve = +1 (von N nach O etc.)
        if robot_rotation > 4: 
            robot_rotation == 0
        screen.update() #zeichnet den Screen neu

    def turn_left(): #Roboter dreht sich nach links
        robot_rotation -= 1 #siehe oben, Rechtskurve = +1 (von N nach O etc.)
        if robot_rotation < 1:
            robot_rotation==4
        screen.update() #zeichnet den Screen neu

    def move_forward(): #NEEDS CHECK IF THE RESULTING FIELD IS PASSABLE!
        rotation = self.get_robot_rotation()
        position = self.get_robot_position()
        x = position[0]
        y= position[1]
        if rotation == 0:
            y += 1
        elif rotation == 1:
            x += 1
        elif rotation == 2:
            y -= 1
        elif rotation == 3:
            x -= 1
        robot_position = [x, y]
        screen.update()

    def move_back(): #NEEDS CHECK IF THE RESULTING FIELD IS PASSABLE!
        rotation = self.get_robot_rotation()
        position = self.get_robot_position()
        x = position[0]
        y = position[1]
        if rotation == 0:
            y -= 1
        elif rotation == 1:
            x -= 1
        elif rotation == 2:
            y += 1
        elif rotation == 3:
            x += 1
        robot_position = [x, y]
        screen.update()
        
    def attack():
        rotation = self.get_robot_rotation()
        position = self.get_robot_position()
        x = position[0]
        y = position[1]
        if rotation == 0:
            y -= 1
        elif rotation == 1:
            x -= 1
        elif rotation == 2:
            y += 1
        elif rotation == 3:
            x += 1
        if lookAtField(x, y).type == opponent:
            damage()
        else:
            pass

#missing classes:
class field:
    
#missing functions:
screen.update()
damage()
lookAtField()
