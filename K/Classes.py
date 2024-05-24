class Employee:
    count = 0
    def __init__ (self, Empid, firstName, lastName, age, salary, post=None):
        self.Empid = Empid
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.post = post
        self.salary = salary
        Employee.count += 1


    def display_employee(self):
        return ('Фамилия: {}. Зарплата: {}'.format(self.lastName, self.salary))

    def annual_salary(self):
        return ('Годовая зарплата: {}'. format(self.salary * 12))

class Administration(Employee):
    def __init__(self, Empid, firstName, lastName, age, salary, countEmpl, post=None):
        super().__init__(Empid, firstName, lastName, age, salary, post=post)
        self._countEmpl = countEmpl

    @property
    def countEmpl(self):
        return self._countEmpl

    @countEmpl.setter
    def countEmpl(self, num):
        if num < 1:
            raise ValueError('Число сотрудников не может быть равняться 0.')
        self._countEmpl = num


empl1 = Employee(1 ,'Сергей', 'Сидоров', 19, 5, 'designer')
print(f'{empl1.lastName} зарабатывает {empl1.salary} серебрянников')
print(f'В год {empl1.lastName} зарабатывает {empl1.annual_salary()}')

admin1 = Administration(2, 'Анатолий', 'Котов', 20, 300, 2)
print(f'Администратор {admin1.lastName} имеет в подчинении сотрудников: {admin1._countEmpl}')