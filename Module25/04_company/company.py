class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return '{name} {surname} {age} years old.'.format(
            name=self.__name,
            surname=self.__surname,
            age=self.__age
        )

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__salary = 0

    def __str__(self):
        return super().__str__()


class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def get_salary(self):
        return self.__salary

    def set_salary(self):
        self.__salary = 13000

    def __str__(self):
        return '{}\nSalary: {}\n'.format(super().__str__(), self.__salary)


class Agent(Employee):

    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def get_salary(self):
        return self.__salary

    def set_salary(self):
        self.__salary = self.volume_of_sales * 0.05 + 5000

    def __str__(self):
        return '{}\nSalary: {}\n'.format(super().__str__(), self.__salary)


class Worker(Employee):

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def get_salary(self):
        return self.__salary

    def set_salary(self):
        self.__salary = self.hours * 100

    def __str__(self):
        return '{}\nSalary: {}\n'.format(super().__str__(), self.__salary)

