# -*- coding: gbk -*-
class Salary(object):
    TAX_DATA = {
        36000:0.03,
        144000:0.10,
        300000:0.20,
        420000:0.25,
        660000:0.30,
        960000:0.35,
        999999999999999999:0.45
    }
    NO_TAX_SALARY = 5000	

    def __init__(self):
        self.salary = 0
        self.tax = 0

    def clacAllTax(self, AllSalary):
        tax = 0
        lastLevel = 0
        for k in sorted(self.TAX_DATA.keys()):
            if AllSalary < k:
                tax += self.TAX_DATA[k] * (AllSalary - lastLevel)
                break
            
            tax += self.TAX_DATA[k] * (k - lastLevel)
            lastLevel = k
        return tax
	
    def clacBonusTax(self, AllBonus):
        for k in sorted(self.TAX_DATA.keys()):
            if AllBonus < k:
                return self.TAX_DATA[k] * AllBonus
        return 0
    

    def addSalary(self, currentSalary):
        self.salary += (currentSalary - self.NO_TAX_SALARY)
        tax = self.clacAllTax(self.salary)
        ret = tax - self.tax
        self.tax = tax
        return ret


s = Salary()

#输入月薪
monthSalary = 10000
for i in xrange(1, 13):
    print 'month %d tax %d' % (i, s.addSalary(monthSalary))

#年终奖
print 'bonus tax %d' % (s.clacBonusTax(120000))
