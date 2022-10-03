"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    monthlyPay = 0
    bonusCommission = 0
    hoursNo = 0
    payPerHour = 0
    contractNo = 0
    payPerContract = 0

    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return self.get_wage() + self.get_commission()

    def __str__(self):
        return self.name

    def get_wage(self):
        return self.hoursNo * self.payPerHour + self.monthlyPay

    def get_commission(self):
        return self.contractNo * self.payPerContract + self.bonusCommission

    def get_contract_details(self):
        if self.bonusCommission:
            return f" and receives a bonus commission of {self.bonusCommission}"
        elif self.contractNo and self.payPerContract:
            return f" and receives a commission for {self.contractNo} contract(s) at {self.payPerContract}/contract"
        else:
            return ""

class MonthlyContractor(Employee):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.get_wage()}{self.get_contract_details()}. Their total pay is {self.get_pay()}."

class SalaryContractor(Employee):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{self.name} works on a contract of {self.hoursNo} hours at {self.payPerHour}/hour{self.get_contract_details()}. Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyContractor('Billie')
billie.monthlyPay = 4000

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = SalaryContractor('Charlie')
charlie.hoursNo = 100
charlie.payPerHour = 25

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyContractor('Renee')
renee.monthlyPay = 3000
renee.contractNo = 4
renee.payPerContract = 200

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = SalaryContractor('Jan')
jan.hoursNo = 150
jan.payPerHour = 25
jan.contractNo = 3
jan.payPerContract = 220

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyContractor('Robbie')
robbie.monthlyPay = 2000
robbie.bonusCommission = 1500

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = SalaryContractor('Ariel')
ariel.hoursNo = 120
ariel.payPerHour = 30
ariel.bonusCommission = 600
