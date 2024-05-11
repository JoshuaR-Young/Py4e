sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
if fh > 40 :
    reg = fh * fr
    opt = (fh - 40) * (fr * 0.5)
    xp = reg + opt
else:
    xp = fh * fr
print("Pay:",xp)