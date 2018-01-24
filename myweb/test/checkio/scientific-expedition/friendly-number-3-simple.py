#coding:utf8


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    str_power = powers[0]
    for i in range(len(powers)-1):
        if number/base>=1:
            number = number/float(base)
            str_power = powers[i+1]
        else:
            break

    if decimals:
        number = str(round(number, decimals))
        if len(number.split('.'))==2:
            decimals_len = len(number.split('.')[-1])
            number = number+'0'*(decimals-decimals_len)
        if len(number.split('.'))==1:
            number = number+'.'+'0'*(decimals)
    else:
        number = str(int(number))

    return number+str_power+suffix

# print friendly_number(12341234, decimals=1)
# print friendly_number(1024000000, base=1024, suffix='iB')
# print friendly_number(12000000, decimals=3)
# print friendly_number(102, decimals=2)
# print friendly_number(12341234, decimals=1)=='12.3M'
# print friendly_number(255000000000, powers=["","k","M"])
print friendly_number(4294967297, base=2, powers=["p0","p1","p2","p3","p4","p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16","p17","p18","p19","p20","p21","p22","p23","p24","p25","p26","p27","p28","p29","p30","p31"])
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

