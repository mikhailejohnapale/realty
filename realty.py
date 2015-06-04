BASIC_TAX_RATE = 0.011
SEF_RATE = 0.01
SH_RATE = 0.5


def compute_discount_rate(month):
    if month == 1:
        discount_rate = 0.2
    elif month <= 3:
        discount_rate = 0.1
    else:
        discount_rate = 0
    return discount_rate


def compute_penalty_rate(curr_date, prev_date):
    penalty_rate = 0
    if curr_date.month > 3:
        for year in range(curr_date.year, prev_date.year - 1, -1):
            # current year
            if year == curr_date.year:
                if curr_date.year == prev_date.year:
                    for month in range(1, curr_date.month + 1):
                        penalty_rate += 2
                    break
                else:
                    for month in range(1, 12 + 1):
                        penalty_rate += 2
            # previous year
            elif year == prev_date.year:
                for month in range(1, prev_date.month + 1):
                    penalty_rate += 2
            # middle years
            else:
                for month in range(1, 12 + 1):
                    penalty_rate += 2
    if penalty_rate >= 72:
        penalty_rate = 72
    return penalty_rate


def compute_sh_tax(assessed_value, type, SH_RATE):
    if type == 'LOT' and assessed_value > 50000:
        sh = assessed_value * SH_RATE
    else:
        sh = 0
    return sh


def compute_discount(tax, month):
    discount_rate = compute_discount_rate(month)
    return tax * discount_rate
