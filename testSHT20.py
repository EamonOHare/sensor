from sensor import SHT20

# I2C bus=1, Address=0x40
#write the data into data.txt
file1 = open('data.txt', 'w')
sht = SHT20(1, 0x40)
for x in range(5):
    h, t = sht.all()  # read both at once
    file1.write(" ".join(str(s) for s in h))
    file1.write("\n")
    file1.write(" ".join(str(s) for s in l))
    file1.write("\n")


file1.close()

#h = sht.humidity()  # read humidity
print(h)            # namedtuple
print(h.RH)         # relative humidity

#t = sht.temperature()  # read temperature
print(t)               # namedtuple
print(t.C)             # Celsius

