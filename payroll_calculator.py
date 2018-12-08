class Payrollcalculator:
    gross_salary=0
    nhif=0
    nssf=0
    payee=0

    def __init__(self, basic, over, house, other):
        self.gross_salary = int(basic)+int(over)+int(house)+int(other)
        self.calculate_nhif(self.gross_salary)
        self.calculate_nssf(self.gross_salary)
        self.calculate_payee(self.gross_salary)


    def calculate_nhif(self, gross_salary):
        x = self.gross_salary
        if x > 0 and x <= 5999:
            nhif = 150
        if x >= 6000 and x <= 7999:
            nhif = 300
        elif x >= 8000 and x <= 11999:
            nhif = 400
        elif x >= 12000 and x <= 14999:
            nhif = 500
        elif x >= 15000 and x <= 19999:
            nhif = 600
        elif x >= 20000 and x <= 24999:
            nhif = 750
        elif x >= 25000 and x <= 29999:
            nhif = 850
        elif x >= 30000 and x <= 34999:
            nhif = 900
        elif x >= 35000 and x <= 39999:
            nhif = 950
        elif x >= 40000 and x <= 44999:
            nhif = 1000
        elif x >= 45000 and x <= 49999:
            nhif = 1100
        elif x >= 50000 and x <= 59999:
            nhif = 1300
        elif x >= 70000 and x <= 79999:
            nhif = 1400
        elif x >= 80000 and x <= 89999:
            nhif = 1500
        elif x >= 90000 and x <= 99999:
            nhif = 1600
        elif x >= 100000:
            nhif = 1700
        self.nhif = int(nhif)

    def calculate_nssf(self, x):
        nssf = x * 0.06
        self.nssf =int(nssf)

    def calculate_payee(self, x):
        if x >= 12298:
            payee = 0.1 * x
        elif x >= 12299 and x <= 28885:
            payee = 0.15 * x
        elif x >= 28886 and x <= 35472:
            payee = 0.2 * x
        elif x >= 35473 and x <= 47059:
            payee = 0.25 * x
        elif x > 47059:
            payee = 0.3 * x
        self.payee = int(payee)



