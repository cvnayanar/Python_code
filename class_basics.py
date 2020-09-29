class employee():
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.email_id = first + '.' + last + '@gmail.com'
        self.pay = pay

    def full_name(self):
        print('{} {}'.format(self.first_name, self.last_name))


emp1 = employee('chinmai', 'nayanar', '50000')
emp2 = employee('test', 'test', '60000')

emp1.full_name()
employee.full_name(emp1)
