class Wheels(): ## wheels ## rotation grid ## input = rotation (q, d)

    def rotate_left(self):
        self.direction += 1 

    def rotate_right(self):
        self.direction += 3 ## -=1

class Head():
    def __init__(self, speed=0): ## engine ## input = speed (z, s)
        self.speed = speed ## on peut remplacer speed par 0 et enlever speed=0 de l'init
        self.position = [0,0]
        self.direction = 1 # ["positif_y", "negatif_x", "negatif_y", "positif_x"]

    def move(self):
        if self.direction %4 == 1: # positif_y
            self.position[1] += self.speed
             
        elif self.direction %4 == 2: # negatif_x
            self.position[0] -= self.speed

        elif self.direction %4 == 3: # negatif_y
            self.position[1] -= self.speed

        elif self.direction %4 == 0: # positif_x
            self.position[0] += self.speed

    def faster(self):
        if self.speed < 9:
            self.speed += 1

    def slower(self):
        if self.speed > 1:    
            self.speed -= 1

class Tail():
    ## next week
    pass

class Snake(Head,Wheels,Tail): ## main class
    def __init__(self,name,color): ## can add speed=0
        Wheels.__init__(self) ## Car exercice oop-06 legacy
        Head.__init__(self) ## need to add speed if we add speed=0
        Tail.__init__(self)
        self.name = name
        self.color = color

## app ## snake ##
## app ## snake ##
## app ## snake ##

snake_food = [7,2] ## add random.randint(), random X, random Y, add new food ## snake
color = "blue" # input("choose a color for your car: ")
name = "test" # input("choose a name for your car: ") 
user_car = Snake(name,color)

print(f"you're goal is to reach: {snake_food}")
print("--- use 'z' to accelerate -----")
print("--- use 's' to decelerate -----")
print("--- use 'q' to rotate left ----")
print("--- use 'd' to rotate right ---")

while user_car.position != snake_food: ## add time(), auto move each second
    print(f"you're goal is to reach: {snake_food}")
    print(f"Current position: {user_car.position}")

    command = input("Enter command: ").strip()
    if command == "z": user_car.faster()
    elif command == "s": user_car.slower()
    elif command == "q": user_car.rotate_left()
    elif command == "d": user_car.rotate_right()
    user_car.move()

print(f"Reached the target grid position {snake_food}!")