# -*- coding: utf-8 -*-


def cal_equality_corpus_interest(loan_amount, loan_months, monthly_rate):
    '''等额本息计算法'''
    monthly_payment = loan_amount * (monthly_rate *
                                     ((1 + monthly_rate)**loan_months)) / ((
                                         (1 + monthly_rate)**loan_months) - 1)
    gross_interest = loan_months * monthly_payment - loan_amount

    return monthly_payment, gross_interest


def cal_equality_corpus(loan_amount, loan_months, monthly_rate):
    '''等额本金计算法'''
    fst_month_payment = loan_amount / loan_months + loan_amount * monthly_rate
    decrease_monthly = loan_amount / loan_months * monthly_rate
    gross_interest = loan_months * ((loan_amount * monthly_rate) -
                                    (monthly_rate *
                                     (loan_amount / loan_months) *
                                     (loan_months - 1) / 2) +
                                    (loan_amount / loan_months)) - loan_amount

    return fst_month_payment, decrease_monthly, gross_interest


if __name__ == "__main__":
    """
    输入：
    1.贷款金额
    2.贷款期限
    3.标准年利率
    4.利率浮动倍数
    """
    loan_amount = float(input('贷款金额（万）：'))
    Loan_period = int(input('贷款期限（年）：'))
    anaual_rate = float(input('标准年利率（%）：'))
    rate_floating_multiple = float(input('利率浮动倍数：'))

    loan_amount = loan_amount * 10000
    anaual_rate = anaual_rate * rate_floating_multiple
    loan_months = Loan_period * 12
    monthly_rate = anaual_rate / 12 / 100

    # 等额本息法计算
    monthly_payment, gross_interest = cal_equality_corpus_interest(
        loan_amount, loan_months, monthly_rate)
    print('等额本息：')
    print('每月还款', monthly_payment)
    print('总利息', gross_interest)

    # 等额本金计算
    fst_month_payment, decrease_monthly, gross_interest2 = cal_equality_corpus(
        loan_amount, loan_months, monthly_rate)
    print('等额本金:')
    print('首月还款', fst_month_payment)
    print('每月递减额', decrease_monthly)
    print('总利息', gross_interest2)
