class Owner:
    def __init__(self, owner):
        self.owner = owner

Dog = Owner("Woman")
Cat = Owner("Woman")
Fish = Owner("Woman")

print(Dog.owner)
