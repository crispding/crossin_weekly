# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import random

num = random.randint(1, 100)

root = tk.Tk()
root.title("个税计算器")
window_left = ttk.Frame(root)
window_left.pack(ipadx=10, ipady=10, fill='y', side=tk.LEFT)

label1 = ttk.Label(window_left, text="税前月收入：")
label1.pack(padx=20, pady=10)
pretax_income = tk.DoubleVar()
entry1 = ttk.Entry(window_left, width=20, textvariable=pretax_income)
entry1.pack()

label2 = ttk.Label(window_left, text="五险一金：")
label2.pack(padx=20, pady=10)
insurance_fund = tk.DoubleVar()
entry2 = ttk.Entry(window_left, width=20, textvariable=insurance_fund)
entry2.pack()

window_right = ttk.Frame(root)
window_right.pack(ipadx=10, ipady=10, fill='y', side=tk.RIGHT)
output = scrolledtext.ScrolledText(
    window_right,
    height=10,
    width=25,
    highlightbackground='black',
    highlightthickness=1)
output.pack(pady=40)

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


def getResult():
    try:
        pretaxIncome = pretax_income.get()
        insuranceFund = insurance_fund.get()
    except ValueError as e:
        print(e, "请输入正确数字。")
    else:
        oldTax = taxByOldRate(pretaxIncome, insuranceFund)
        oldIncome = pretaxIncome - oldTax - insuranceFund
        newTax = taxByNewRate(pretaxIncome, insuranceFund)
        newIncome = pretaxIncome - newTax - insuranceFund

        output.insert(tk.INSERT, "旧税率应纳税：{:.2f} 元，税后收入：{:.2f} 元\n".format(
            oldTax, oldIncome))
        output.insert(tk.INSERT, "新税率应纳税：{:.2f} 元，税后收入：{:.2f} 元\n    ".format(
            newTax, newIncome))


btn = ttk.Button(window_left, text="确定", command=getResult)
btn.pack(pady=20)

root.mainloop()
