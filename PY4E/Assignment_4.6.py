## Using functions for grosspay calculation
def computepay(h, r):
    if h > 40:
        eh = 1.5 * (h - 40)+40 #Overtime rate 
        grosspay = eh*r
    else: #regular hours
        grosspay = h*r
    return grosspay
hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")
h =float(hrs)
r=float(rph)
p = computepay(h, r)
print("Pay:", p)