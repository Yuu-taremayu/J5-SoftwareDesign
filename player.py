import random

class PLAYER():
    # init player status
    def __init__(self):
        # player's position
        self.x = 0
        self.y = 0

        # some status
        self.money = 0
        self.muscle = 0
        self.stress = 0
        self.dexterity = 0
        self.job = None
        self.condition = False

        self.decide_job()

    # decide player's job
    def decide_job(self):
        r = random.randrange(4)
        if r == 0:
            self.job = 'Teacher'
        elif r == 1:
            self.job = 'Engineer'
        elif r == 2:
            self.job = 'SportsMan'
        else:
            self.job = 'NoJob'
