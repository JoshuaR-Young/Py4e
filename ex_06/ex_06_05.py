str = 'X-DSPAM-Confidence: 0.8475'
atnum = str.find('0')
#print(atnum)

sppos = str.find('5')
#print(sppos)

host = float(str[atnum:sppos+1])
print(host)