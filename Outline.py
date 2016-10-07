#Work in Progress

#Hier stehen in einem Outline die main-functions eines Roboters

class Field():
    passable = True
    kind = "" #type is a key word ;(
    team = "zero"
    occupied = "zero"
    
    
class Robot():
    health = 100
    rotation = 3 #Wie Himmelsrichtungen: 1=N, 2=O, 3=S, 4=W
    position = [0, 0] #Koordinatensystem mit x,y
    
    def get_robot_position(self):
        robot_position = self.position #just be sure so that we are not changing important values
        return robot_position
    
    def get_robot_rotation(self):
        robot_rotation = self.rotation
        return robot_rotation
    
    def turn_right(self): #Roboter dreht sich nach rechts
        self.rotation += 1 #siehe oben, Rechtskurve = +1 (von N nach O etc.)
        if self.rotation > 4: 
            self.rotation == 0
        screen.update() #zeichnet den Screen neu

    def turn_left(self): #Roboter dreht sich nach links
        self.rotation -= 1 #siehe oben, Rechtskurve = +1 (von N nach O etc.)
        if self.rotation < 1:
            self.rotation==4
        screen.update() #zeichnet den Screen neu

    def move_forward(self):
        robot_rotation = self.get_robot_rotation()
        robot_position = self.get_robot_position()
        x = robot_position[0]
        y = robot_position[1]
        if robot_rotation == 0:
            if lookAtField(x, y+1).passable == True:
                y += 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        elif robot_rotation == 1:
            if lookAtField(x+1, y).passable == True:
                x += 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        elif robot_rotation == 2:
            if lookAtField(x, y-1).passable == True:
                y -= 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        elif robot_rotation == 3:
            if lookAtField(x-1, y).passable == True:
                x -= 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        self.position = [x, y]
        screen.update()

    def move_back(self): #NEEDS CHECK IF THE RESULTING FIELD IS PASSABLE!
        robot_rotation = self.get_robot_rotation()
        robot_position = self.get_robot_position()
        x = robot_position[0]
        y = robot_position[1]
        if robot_rotation == 0:
            if lookAtField(x, y-1).passable == True:
                y -= 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        elif robot_rotation == 1:
            if lookAtField(x-1, y).passable == True:
                x -= 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        elif robot_rotation == 2:
            if lookAtField(x, y+1).passable == True:
                y += 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        elif robot_rotation == 3:
            if lookAtField(x+1, y).passable == True:
                x += 1
            else:
                print("Hindernis im Weg, Roboter kann sich nicht bewegen")
        self.position = [x, y]
        screen.update()
        
    def attack(self):
        robot_rotation = self.get_robot_rotation()
        robot_position = self.get_robot_position()
        x = robot_position[0]
        y = robot_position[1]
        if robot_rotation == 0:
            y -= 1
        elif robot_rotation == 1:
            x -= 1
        elif robot_rotation == 2:
            y += 1
        elif robot_rotation == 3:
            x += 1
        if lookAtField(x, y).occupied == opponent: #need to define opponent
            damage()
        else:
            pass
        
#Fehlende functions:
def update():
    pass
#Was bei screen.update alles passieren muss:
#- die Roboter werden geupdated
#   - Drehungen werden ausgeführt
#   - Bewegungen werden ausgeführt
#   - Lebensleiste wird neu angezeigt
#- jedes Feld wird geupdated:
#   -Wenn ein Roboter darauf steht: passable => False, team => robot_team, occupied => robot
#   -Wenn ein Roboter nicht darauf steht:passable => False, team=> NICHT AENDERN, occupied => "zero"

def damage():
    


def lookAtField(x, y):
    field = Field[x, y] #oder so ähnlich, siehe unten.
    #Wie machen wir das mit den Feldern? Wo wird die ganze Information abgespeichert?? In einer Liste, oder ist jedes Feld ein
    #Objekt mit den dazugehörigen x und y Werten?
    def passable(self):
        #if object can not be found (je nach Variante andere Syntax) or object can be found and is unpassable:
            return False
        #if object can be found and is passable:
            return True
    
    def kind(self):
        #if object can not be found (je nach Variante andere Syntax):
            return "wall"
        #if object can be found and is a normal field:
            return "field"
        #if object can be found and is a obstacle
            return "obstacle"
    
    def occupied(self):
        #if red_robot occupies this field
            return "red_robot"
        #if blue/robot occupies this field
            return "blue_robot"
        #if object can not be found (je nach Variante andere Syntax):
            return "zero"
        
