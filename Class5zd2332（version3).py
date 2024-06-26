import numpy as np
def WhoAmI():
    return('zd2332')

# getBondprice
def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    discount_factors = np.array([(1 + y/ppy)**(-t) for t in range(1, n + 1)])
    pv_coupons = c * discount_factors
    pv_face = face * discount_factors[-1]
    bond_price = np.sum(pv_coupons) + pv_face
    return bond_price

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 2
bond_price = getBondPrice(y, face, couponRate, m, ppy)
print(f"The bond price is: ${bond_price:.2f}")

#getBondduration

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    c = face * couponRate / ppy
    t = np.arange(1, n + 1)
    discount_factors = (1 + y/ppy) ** -t
    cash_flows = np.full(n, c)
    cash_flows[-1] += face
    pv_cf = cash_flows * discount_factors
    w = pv_cf / np.sum(pv_cf)
    weighted_times = w * t
    duration = np.sum(weighted_times)
    return duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 2

# Calculate bond duration
duration = getBondDuration(y, face, couponRate, m, ppy)
print(f"The bond duration is: {duration:.2f}")
#getFizzbuzz
def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = "fizzbuzz"
    objvec[(numvec % 3 == 0) & (numvec % 5 != 0)] = "fizz"
    objvec[(numvec % 5 == 0) & (numvec % 3 != 0)] = "buzz"
    
    return objvec

# Test values
start = 16
finish = 30

# Calculate FizzBuzz
result = FizzBuzz(start, finish)
print(result)
