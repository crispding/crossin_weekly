# -*- coding: utf-8 -*-

# 计算旧税率下的个人所得税
# pretaxIncome : 税前工资
# insuranceFund : 五险一金
# taxableIncome : 应纳税所得额
# tax : 应纳税额


def taxByOldRate(pretaxIncome, insuranceFund):
    taxableIncome = pretaxIncome - insuranceFund - 3500
    tax = 0
    if taxableIncome <= 0:
        tax = 0
    elif taxableIncome <= 1500:
        tax = taxableIncome * 0.03
    elif taxableIncome <= 4500:
        tax = taxableIncome * 0.1 - 105
    elif taxableIncome <= 9000:
        tax = taxableIncome * 0.2 - 555
    elif taxableIncome <= 35000:
        tax = taxableIncome * 0.25 - 1005
    elif taxableIncome <= 55000:
        tax = taxableIncome * 0.3 - 2755
    elif taxableIncome <= 80000:
        tax = taxableIncome * 0.35 - 5505
    else:
        tax = taxableIncome * 0.45 - 13505
    return tax


# 计算新税率下的个人所得税
# pretaxIncome : 税前工资
# insuranceFund : 五险一金
# taxableIncome : 应纳税所得额
# tax : 应纳税额


def taxByNewRate(pretaxIncome, insuranceFund):
    taxableIncome = pretaxIncome - insuranceFund - 5000
    tax = 0
    if taxableIncome <= 0:
        tax = 0
    elif taxableIncome <= 3000:
        tax = taxableIncome * 0.03
    elif taxableIncome <= 12000:
        tax = taxableIncome * 0.1 - 210
    elif taxableIncome <= 25000:
        tax = taxableIncome * 0.2 - 1410
    elif taxableIncome <= 35000:
        tax = taxableIncome * 0.25 - 2660
    elif taxableIncome <= 55000:
        tax = taxableIncome * 0.3 - 4410
    elif taxableIncome <= 80000:
        tax = taxableIncome * 0.35 - 7160
    else:
        tax = taxableIncome * 0.45 - 15160
    return tax


if __name__ == '__main__':
    try:
        pretaxIncome = float(input("税前月收入："))
        insuranceFund = float(input("五险一金："))
    except ValueError as e:
        print(e, "请输入正确数字。")
    else:
        oldTax = taxByOldRate(pretaxIncome, insuranceFund)
        oldIncome = pretaxIncome - oldTax - insuranceFund
        newTax = taxByNewRate(pretaxIncome, insuranceFund)
        newIncome = pretaxIncome - newTax - insuranceFund

        print("旧税率应纳税：{:.2f} 元，税后收入：{:.2f} 元".format(oldTax, oldIncome))
        print("新税率应纳税：{:.2f} 元，税后收入：{:.2f} 元".format(newTax, newIncome))
