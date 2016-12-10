def computepay(hrs,rate):
    try:
        hrs=float(hrs)
        rate=float(rate)
        if hrs < 0 or rate < 0 :
   			print "Hours and payrate can not be negative numbers"
        elif hrs > 40:
            overtime=((hrs-40)*(rate*1.5))
            reghrs=(40*rate)
            totalpay=overtime+reghrs
            return totalpay
        elif hrs <= 40 and hrs >= 1 :
            totalpay=hrs*rate
            return totalpay
    except:
        print "Invialid numbers entered"
        quit()
hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Payrate:")
p = computepay(hrs,rate)
print p
"""Coded By:Miguel Jimenez"""
