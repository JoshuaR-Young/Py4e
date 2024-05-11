def computepay(hours, rate) :
    #print("in computepay",hours, rate)
    if hours > 40 :
        reg = rate * hours
        opt = (hours - 40) * (rate * 0.5)
        pay = reg + opt
    else:
        pay = hours * rate
    #print("returning",pay)
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:",xp)