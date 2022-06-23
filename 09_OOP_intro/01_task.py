class Student:
    university = 'PUT'

    def __init__(self, first, last, age):#pierwsza podstawowa instancja
        self.first = first
        self.last = last
        self.age = age

    def email(self):#metoda email
        return f'{self.first}.{self.last}@university.com'.lower()

ola = Student('Anna', 'Kowalska', 23)
print(ola.last, ola.first, ola.age, ola.email())
ola.last = 'Smith'

print(ola.last, ola.first, ola.age, ola.email())

piotr = Student('Piotr', 'Kowal', 22)

print(piotr.first, piotr.last, piotr.age, piotr.email())

print(ola.university)
print(piotr.university)

print(ola.__dict__)
print(Student.__dict__)