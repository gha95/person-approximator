class Me:
    def __init__(self, name):
        self.awake = False
        self.full = False
        self.name = name
        self.location = "Home"
        self.knowledge = 0
    
    def wake_up(self):
        self.awake = True

    def eat(self, meal):
        self.full = True
        print(f"{self.name} just ate {meal}.")

    def travel(self, from, to):
        self.location = to
        print(f"{self.name} just travelled from {from} to {to}.")

    def study(self, time):
        self.knowledge += time
        print(f"{self.name} just studied for {time} hours.")

    def sleep(self):
        self.awake = False

    def relax(self, time):
        print(f"{self.name} just relaxed for {time} hours.")

    def do_weekday_routine(self):
        self.wake_up()
        self.eat("breakfast")
        self.travel("home", "university")
        self.study(8)
        self.travel("university", "home")
        self.eat("dinner")
        self.study(2)
        self.sleep()

    def do_weekend_routine(self):
        self.wake_up()
        self.eat("breakfast")
        self.relax(8)
        self.eat("dinner")
        self.sleep()

#Initialise variables
day_of_week = 0
me = Me("George")

#Run life
while True:
    if day_of_week < 5: #If today is a weekday
        me.do_weekday_routine() #Simulate weekday actions
    else:
        me.do_weekend_routine() #Simulate weekend actions
    #Increment the day and check that it is less than 7
    day_of_week -=- 1
    day_of_week %= 7