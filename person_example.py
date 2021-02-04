class Person:
    def __init__(self, name, job = None , pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
       return self.name.split()[-1]

    def giveRaise(self, percent):
       self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: {} , {}]'.format(self.name, self.pay)

if __name__ == '__main__':
    arthur = Person('Arthur Wiles')
    jeanne = Person('Jeanne Miles', pay=1000)
    print(arthur.name, arthur.pay)
    print(jeanne.name, jeanne.pay)


    print(arthur.lastName(), jeanne.lastName())  #
    jeanne.giveRaise(.10)  #
    print(jeanne.pay)
    print(jeanne.job)
    print(jeanne)
