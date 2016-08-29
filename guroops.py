import random
import time


# Class to define the entity know as Guroops
# So far they are based off of humans and human ideals but that may be changed later once
# the program is more advanced
class Guroop:
    def __init__(self, motherData=None, fatherData=None, yearLength=0.01):
        # Parents
        self.momData = motherData  # Data strcure containing minum informaiton needed to synthesize
        self.dadData = fatherData
        # Biological Variables:
        self.time_of_birth = time.time()  # time of birth to be used for calculations for age
        self.age = 0  # will be se to zero unless otherwise specified
        self.gender = random.randint(0, 1)  # 0 is female 1 is male
        self.weight = random.randint(-2,
                                     2)  # negative values indicate being underweight, positive values indicate being overweight
        self.height = None  # Will implement later
        # Mental/Physiological Variables:
        self.iq = self.generateIQ()
        self.caring = random.uniform(0, 50)
        self.aggression = random.uniform(0, 50)
        self.greed = random.uniform(0, 50)
        self.willpower = random.uniform(0, 50)
        # Misc Variables
        self.year_length = yearLength
        self.luck = random.uniform(-30, 30)

    def age_up(self):
        current_time = time.time()
        self.age = (current_time - self.time_of_birth) / self.year_length
        if self.age >= 120:
            del self.momData
            del self.dadData
            del self.time_of_birth
            del self.age
            del self.gender
            del self.weight
            del self.height
            del self.iq
            del self.caring
            del self.aggression
            del self.greed
            del self.willpower
            del self.married
            del self.wealth
            del self.year_length

    @staticmethod
    def percentDiff(val1, val2):
        return (abs(val1 - val2) / ((val1 + val2) / 2)) * 100

    def mate_and_marry(self, possible_mate):
        # This checks to see if they are old enough and they are both opposite genders
        if (self.age < 18) or (self.gender + possible_mate.gender != 1):
            return
        if (self.percentDiff(self.age, possible_mate.age) - self.luck) <= 10:
            age_ok = True
        if self.percentDiff(self.height, possible_mate.height) - self.luck <= 50:
            height_ok = True
        if self.percentDiff(self.iq, possible_mate.iq) - self.luck <= 30:
            iq_ok = True


            # Randomly generate an IQ based on a bell curve for human intelligence or based on parent's data

    def generateIQ(self):
        # Determining what IQ will probably be around
        if (self.momData is None) or (self.dadData is None):  # No parent data available
            r = random.random() * 100
        else:
            r = (self.Data['iq'] + self.dadData['iq']) / 2
            # Using average of parent's iq this will determine the range child's iq will be in
            if r <= 54:  # questionable if they are alive
                r = random.random() * 0.13
            elif r <= 69:
                r = random.uniform(0.13, 2.28)
            elif r <= 84:
                r = random.uniform(2.28, 15.87)
            elif r <= 99:  # About lower end of average intelligence
                r = random.uniform() * 50
            elif r <= 114:  # Higher end of average intelligence
                r = random.uniform(50, 84.13)
            elif r <= 129:
                r = random.uniform(84.13, 97.92)
            elif r <= 144:
                r = random.uniform(97.92, 99.87)
            else:  # They may be too smart
                r = random.uniform(99.87, 100)
        # Actual generation of IQ
        if r < 0.13:  # questionable if they are alive
            r = random.randint(0, 54)
        elif r < 2.28:
            r = random.randint(55, 69)
        elif r < 15.87:
            r = random.randint(70, 84)
        elif r < 50:  # About lower end of average intelligence
            r = random.randint(85, 99)
        elif r < 84.13:  # Higher end of average intelligence
            r = random.randint(100, 114)
        elif r < 97.92:
            r = random.randint(115, 129)
        elif r < 99.87:
            r = random.randint(130, 144)
        else:  # They may be too smart
            r = random.randint(145, 200)
        return r

    def make_Dictionary(self):
        d = dict()
        d['momData'] = self.momData
        d['dadData'] = self.dadData
        d['time_of_birth'] = self.time_of_birth
        d['age'] = self.age
        d['gender'] = self.gender
        d['weight'] = self.weight
        d['height'] = self.height
        d['iq'] = self.iq
        d['caring'] = self.caring
        d['aggression'] = self.aggression
        d['greed'] = self.greed
        d['willpower'] = self.willpower
        d['year_length'] = self.year_length
        d['luck'] = self.luck
        return d
