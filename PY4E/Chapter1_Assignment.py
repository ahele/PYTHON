hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")

try:
    h =float(hrs)
    r=float(rph)
except:
    print("Error: Enter numeric value only")
    quit()

if h > 40:
    eh = 1.5 * (h - 40)+40 #Overtime rate 
    grosspay = eh*r
else: #regular hours
    grosspay = h*r 
print("Pay:",grosspay)

