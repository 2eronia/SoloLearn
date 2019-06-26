
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

@file: calculate.py
@author: xiaoxiao
@date: 2018-07-07 17:30:32

"""


class Calculate(object):

    def __init__(self, base_limit, tax_base, tax_3, tax_10, tax_20, tax_25, tax_30, tax_35):
        self.base_limit = base_limit
        self.tax_base = tax_base
        self.tax_3 = tax_3
        self.tax_10 = tax_10
        self.tax_20 = tax_20
        self.tax_25 = tax_25
        self.tax_30 = tax_30
        self.tax_35 = tax_35

    # **********  公积金  ********** #
    # 计算公积金个人缴纳：12%
    def calculate_personal_accumulation_fund(self, n):
        if n < self.base_limit:
            return n * 0.12
        else:
            return self.base_limit * 0.12

    # 计算公积金单位缴纳：12%
    def calculate_unit_accumulation_fund(self, n):
        if n < self.base_limit:
            return n * 0.12
        else:
            return self.base_limit * 0.12

    # **********  养老保险  ********** #
    # 计算养老保险个人缴纳：8%
    def calculate_personal_endowment_insurance(self, n):
        if n < self.base_limit:
            return n * 0.08
        else:
            return self.base_limit * 0.08

    # 计算养老保险单位缴纳：19%
    def calculate_unit_endowment_insurance(self, n):
        if n < self.base_limit:
            return n * 0.19
        else:
            return self.base_limit * 0.19

    # **********  失业保险  ********** #
    # 计算失业保险个人缴纳：0.0%
    def calculate_personal_unemployment_insurance(self, n):
        if n < self.base_limit:
            return n * 0.00
        else:
            return self.base_limit * 0.00

    # 计算失业保险单位缴纳：0.8%
    def calculate_unit_unemployment_insurance(self, n):
        if n < self.base_limit:
            return n * 0.008
        else:
            return self.base_limit * 0.008

    # **********  工伤保险  ********** #
    # 计算工伤保险个人缴纳：0.0%
    def calculate_personal_injury_insurance(self, n):
        if n < self.base_limit:
            return n * 0.00
        else:
            return self.base_limit * 0.00

    # 计算工伤保险单位缴纳：0.4%
    def calculate_unit_injury_insurance(self, n):
        if n < self.base_limit:
            return n * 0.004
        else:
            return self.base_limit * 0.004

    # **********  生育保险  ********** #
    # 计算生育保险个人缴纳：0.0%
    def calculate_personal_maternity_insurance(self, n):
        if n < self.base_limit:
            return n * 0.00
        else:
            return self.base_limit * 0.

    # 计算生育保险单位缴纳：0.4%
    def calculate_unit_maternity_insurance(self, n):
        if n < self.base_limit:
            return n * 0.004
        else:
            return self.base_limit * 0.004

    # **********  医疗保险  ********** #
    # 计算医疗保险个人缴纳：2%+3
    def calculate_personal_medical_insurance(self, n):
        if n < self.base_limit and n >= 3:
            return n * 0.02 + 3
        elif n > self.base_limit:
            return self.base_limit * 0.02 + 3
        else:
            return 0.00

    # 计算医疗保险单位缴纳：10%
    def calculate_unit_medical_insurance(self, n):
        if n < self.base_limit:
            return n * 0.10
        else:
            return self.base_limit * 0.10

    # **********  个人所得税  ********** #
    def calculate_personal_income_tax(self, m):
        m = m - self.tax_base
        if m <= 0:
            return 0
        elif m < self.tax_3:
            return m * 0.03
        elif m < self.tax_10:
            return m * 0.10 - self.tax_3 * 0.07
        elif m < self.tax_20:
            return m * 0.20 - self.tax_10 * 0.1 - self.tax_3 * 0.07
        elif m < self.tax_25:
            return m * 0.25 - self.tax_20 * 0.05 - self.tax_10 * 0.1 - self.tax_3 * 0.07
        elif m < self.tax_30:
            return m * 0.30 - self.tax_25 * 0.05 - self.tax_20 * 0.05 - self.tax_10 * 0.1 - self.tax_3 * 0.07
        elif m < self.tax_35:
            return m * 0.35 - self.tax_30 * 0.05 - self.tax_25 * 0.05 - self.tax_20 * 0.05 - self.tax_10 * 0.1 - self.tax_3 * 0.07
        else:
            return m * 0.45 - self.tax_35 * 0.1 - self.tax_30 * 0.05 - self.tax_25 * 0.05 - self.tax_20 * 0.05 - self.tax_10 * 0.1 - self.tax_3 * 0.07

# 计算旧版年终奖扣税
    def calculate_year_award_tax_old(self, salary, year_award):
        tax = 0.0
        base_salary = 3500
        # 如果年终奖减去最低扣税基数与基本工资的差额小于0，则不用扣税
        if year_award - base_salary + salary <= 0:
            return tax
        if salary > base_salary:
            if year_award / 12 < 1500:
                tax = year_award * 0.03 - 0
            elif year_award / 12 < 4500:
                tax = year_award * 0.10 - 105
            elif year_award /12 < 9000:
                tax = year_award * 0.20 - 555
            elif year_award / 12 < 35000:
                tax = year_award * 0.25 - 1005
            elif year_award / 12 < 55000:
                tax = year_award * 0.30 - 2755
            elif year_award / 12 < 80000:
                tax = year_award * 0.35 - 5505
            elif year_award > 80000:
                tax = year_award * .045 - 80000
            else:
                print ("Input year_award = %s" % year_award)
        else:
            if year_award / 12 < 1500:
                tax = (year_award - base_salary + salary) * 0.03 - 0
            elif year_award / 12 < 4500:
                tax = (year_award - base_salary + salary) * 0.10 - 105
            elif year_award /12 < 9000:
                tax = (year_award - base_salary + salary) * 0.20 - 555
            elif year_award / 12 < 35000:
                tax = (year_award - base_salary + salary) * 0.25 - 1005
            elif year_award / 12 < 55000:
                tax = (year_award - base_salary + salary) * 0.30 - 2755
            elif year_award / 12 < 80000:
                tax = (year_award - base_salary + salary) * 0.35 - 5505
            elif year_award > 80000:
                tax = (year_award - base_salary + salary) * .045 - 13505
            else:
                print ("Input year_award = %s" % year_award)
        return tax

# 计算新版年终奖扣税
    def calculate_year_award_tax_new(self, salary, year_award):
        tax = 0.0
        base_salary = 5000
        # 如果年终奖减去最低扣税基数与基本工资的差额小于0，则不用扣税
        if year_award - base_salary + salary <= 0:
            return tax
        if salary > base_salary:
            if year_award / 12 < 3000:
                tax = year_award * 0.03 - 0
            elif year_award / 12 < 12000:
                tax = year_award * 0.10 - 210
            elif year_award /12 < 25000:
                tax = year_award * 0.20 - 1410
            elif year_award / 12 < 35000:
                tax = year_award * 0.25 - 2660
            elif year_award / 12 < 55000:
                tax = year_award * 0.30 - 4410
            elif year_award / 12 < 80000:
                tax = year_award * 0.35 - 7160
            elif year_award > 80000:
                tax = year_award * .045 - 15160
            else:
                print ("Input year_award = %s" % year_award)
        else:
            if year_award / 12 < 1500:
                tax = (year_award - base_salary + salary) * 0.03 - 0
            elif year_award / 12 < 4500:
                tax = (year_award - base_salary + salary) * 0.10 - 105
            elif year_award /12 < 9000:
                tax = (year_award - base_salary + salary) * 0.20 - 555
            elif year_award / 12 < 35000:
                tax = (year_award - base_salary + salary) * 0.25 - 1005
            elif year_award / 12 < 55000:
                tax = (year_award - base_salary + salary) * 0.30 - 2755
            elif year_award / 12 < 80000:
                tax = (year_award - base_salary + salary) * 0.35 - 5505
            elif year_award > 80000:
                tax = (year_award - base_salary + salary) * .045 - 80000
            else:
                print ("Input year_award = %s" % year_award)
        return tax

salary = input('请输入工资数：')
if salary:
    salary = int(salary)
else:
    salary = 0

# 其它补贴
allowance = input('其它补贴：')
if allowance:
    allowance = int(allowance)
else:
    allowance = 0

year_award = input('请输入年终奖：')
if year_award:
    year_award = int(year_award)
else:
    year_award = 0

calculation = Calculate(25401, 3500, 1500, 4500, 9000, 35000, 55000, 80000)
calculation_new = Calculate(25401, 5000, 3000, 12000, 25000, 35000, 55000, 80000)

# *****  公积金  ****** #
calculate_personal_accumulation_fund = calculation.calculate_personal_accumulation_fund(salary)
calculate_unit_accumulation_fund = calculation.calculate_unit_accumulation_fund(salary)
# print '缴纳的公积金为：' + str(calculate_personal_accumulation_fund + calculate_unit_accumulation_fund)

# *****  养老保险  ***** #
calculate_personal_endowment_insurance = calculation.calculate_personal_endowment_insurance(salary)
calculate_unit_endowment_insurance = calculation.calculate_unit_endowment_insurance(salary)

# *****  失业保险  ***** #
calculate_personal_unemployment_insurance = calculation.calculate_personal_unemployment_insurance(salary)
calculate_unit_unemployment_insurance = calculation.calculate_unit_unemployment_insurance(salary)

# *****  工伤保险  ***** #
calculate_personal_injury_insurance = calculation.calculate_personal_injury_insurance(salary)
calculate_unit_injury_insurance = calculation.calculate_unit_injury_insurance(salary)

# *****  生育保险  ***** #
calculate_personal_maternity_insurance = calculation.calculate_personal_maternity_insurance(salary)
calculate_unit_maternity_insurance = calculation.calculate_unit_maternity_insurance(salary)

# *****  医疗保险  ***** #
calculate_personal_medical_insurance = calculation.calculate_personal_medical_insurance(salary)
calculate_unit_medical_insurance = calculation.calculate_unit_medical_insurance(salary)

print('\n公积金：【个人：%.2f】【单位：%.2f】' % (calculate_personal_accumulation_fund, calculate_unit_accumulation_fund))
print('养老保险：【个人：%.2f】【单位：%.2f】' % (calculate_personal_endowment_insurance, calculate_unit_endowment_insurance))
print('失业保险：【个人：%.2f】【单位：%.2f】' % (calculate_personal_unemployment_insurance, calculate_unit_unemployment_insurance))
print('工伤保险：【个人：%.2f】【单位：%.2f】' % (calculate_personal_injury_insurance, calculate_unit_injury_insurance))
print('生育保险：【个人：%.2f】【单位：%.2f】' % (calculate_personal_maternity_insurance, calculate_unit_maternity_insurance))
print('医疗保险：【个人：%.2f】【单位：%.2f】' % (calculate_personal_medical_insurance, calculate_unit_medical_insurance))
personal_all = calculate_personal_accumulation_fund + calculate_personal_endowment_insurance + calculate_personal_unemployment_insurance + calculate_personal_injury_insurance + calculate_personal_maternity_insurance + calculate_personal_medical_insurance
unit_all = calculate_unit_accumulation_fund + calculate_unit_endowment_insurance + calculate_unit_endowment_insurance + calculate_unit_injury_insurance + calculate_unit_maternity_insurance + calculate_unit_medical_insurance
print('总共缴纳：【个人：%.2f】【单位：%.2f】\n' % (personal_all, unit_all))

# *****  税前应发工资  ***** #
total_pay_amount = salary - personal_all + allowance

print("1.老版纳税税级距：3500[base]-1500[3%]-4500[10%]-9000[20%]-35000[25%]-55000[30%]-80000[35%]-above[45%]")
print("2.新版纳税税级距：5000[base]-3000[3%]-12000[10%]-25000[20%]-35000[25%]-55000[30%]-80000[35%]-above[45%]")

# *****  缴纳的个人所得税  ***** #
personal_tax_old = calculation.calculate_personal_income_tax(total_pay_amount)
personal_tax_new = calculation_new.calculate_personal_income_tax(total_pay_amount)

print('\n应发工资：【%.2f】\n' % total_pay_amount)

print('老版个人所得税：【%.2f】' % personal_tax_old)
final_paying_amount_old = total_pay_amount - personal_tax_old
print('老版实发工资：【%.2f】\n' % final_paying_amount_old)

print('新版个人所得税：【%.2f】' % personal_tax_new)
final_paying_amount_new = total_pay_amount - personal_tax_new
print('新版实发工资：【%.2f】' % final_paying_amount_new)

print('\n新版比老版少缴纳个人所得税：【%.2f】' % (personal_tax_old - personal_tax_new))
if personal_tax_old > 0:
    print('少缴纳比例：【%.1f%%】' % ((personal_tax_old - personal_tax_new) / personal_tax_old * 100))

print ('\n')
year_award_tax_old = calculation.calculate_year_award_tax_old(salary, year_award)
year_award_tax_new = calculation.calculate_year_award_tax_new(salary, year_award)
print('老版年终奖所得扣税如下：')
print('年终奖金额       旧版扣税       新版扣税       旧版年终奖最终所得       新版年终奖最终所得')
print('  ' + str(year_award) + '         ' + str(year_award_tax_old) + '         ' + str(year_award_tax_new) + '          ' +
      str(year_award - year_award_tax_old) + '           ' + str(year_award - year_award_tax_new))
year_salary_old = final_paying_amount_old + year_award - year_award_tax_old
year_salary_new = final_paying_amount_new + year_award - year_award_tax_new
print('\n年终奖新版比老版少缴纳所得税：【%.2f】' % (year_award_tax_old - year_award_tax_new))
if year_award_tax_old > 0:
    print('少缴纳比例：【%.1f%%】' % ((year_award_tax_old - year_award_tax_new) / year_award_tax_old * 100))

print('旧版年终那个月最终工资所得：' + str(year_salary_old))
print('新版年终那个月最终工资所得：' + str(year_salary_new))
print('\n年终奖那个月新版比老版总共少缴纳所得税：【%.2f】' % (personal_tax_old - personal_tax_new + year_award_tax_old - year_award_tax_new))
if year_award_tax_old > 0:
    print('少缴纳比例：【%.1f%%】' % ((personal_tax_old - personal_tax_new + year_award_tax_old - year_award_tax_new) / (personal_tax_old + year_award_tax_old) * 100))