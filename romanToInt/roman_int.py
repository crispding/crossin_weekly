def romanToInt(s):

    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans = 0
    size = len(s)
    i = 0
    while i < size:
        if i > 0 and d[s[i]] > d[s[i - 1]]:
            ans += d[s[i]] - 2 * d[s[i - 1]]
        else:
            ans += d[s[i]]
        i += 1
    return ans

def intToRoman(num):
    
    a = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    b = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    ans = ''
    c = 0
    i = 0

    while num > 0:
        c = num // a[i]
        num %= a[i]
        while c > 0:
            ans += b[i]
            c -= 1
        i += 1
    return ans

assert romanToInt('III') == 3
assert romanToInt('IV') == 4
assert romanToInt('VI') == 6
assert romanToInt('XIX') == 19
assert romanToInt('XLV') == 45
assert romanToInt('MCMLXXX') == 1980
assert romanToInt('CMXCIX') == 999

print(intToRoman(12))
