class Parents:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def print_info(self):
        print('\nName: {}\nAge: {}'.format(
            self.name, self.age,
        ))
        print("Children:")
        for child in self.children:
            child.print_info()

    def calm_the_child(self, child):
        if not child.state_of_calm:
            print(self.name, 'calms', child.name, '\n')
            child.state_of_calm = True
        else:
            print(child.name, 'is calm\n')

    def feed_the_baby(self, child):
        if not child.hunger_state:
            print(self.name, 'feed', child.name, '\n')
            child.hunger_state = True
        else:
            print(child.name, 'is not hungry\n')


class Child:

    def __init__(self, name, age, state_of_calm=False, hunger_state=False):
        self.name = name
        self.age = age
        self.state_of_calm = state_of_calm
        self.hunger_state = hunger_state

    def print_info(self):
        print('\tChild name:', self.name)
        print('\tChild age:', self.age)
        print('\tState of calm', self.state_of_calm)
        print('\tHunger state:', self.hunger_state, '\n')

