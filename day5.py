#strings
#lower
s="I am Isha Negi"
print(s.lower())

#strip
s1="  mumbai  "
print(s1.strip())

#replace
s2="ML ml AI"
print(s2.replace(" ml "," ")) #MLAI #ML AI

#split()
s3="I am Isha Negi"
print(s3.split('I'))  

#join
s4=["I","ML","AI"]
print(" ".join(s4))

#startswith()
s5="i am good"
print(s5.startswith("isha"))

#count()
s6="ML ML ML ML ML AI M L"
print(s6.count("M L"))