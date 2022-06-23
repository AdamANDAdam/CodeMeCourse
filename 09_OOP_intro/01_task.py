# student_anna = {
#   'name': 'Anna',
#   'lastname': 'Kowalska',
#   'age': '23',
#   'subject': 'Computing Science',
#   'email': 'anna.kowalska@university.com'
# }
#
# student_peter = {
#     'name': 'Piotr',
#     'lastname': 'Kowalski',
#     'age': '22',
#     'subject': 'art',
#     'email': 'piotr.kowalski@university.com'
# }

class Student():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = f'{first}.{last}@university.com'.lower()


ola = Student('Anna', 'Kowalska', 23)


print(ola.last, ola.first, ola.age, ola.email)

piotr = Student('Piotr', 'Kowal', 22)

print(piotr.first,piotr.last,piotr.age,piotr.email)