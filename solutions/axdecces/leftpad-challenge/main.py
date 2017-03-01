from sys import stdout
from Leftpad import Leftpad

formattedNumber = Leftpad('123', '12')

print 'This id the output if I use the easy way out (but it\'s wrong, so it\'s no real solution): '
print str(formattedNumber.value).zfill(int(formattedNumber.length))
print ''
print 'This is the output:'

for item in formattedNumber.output:
    stdout.write(item)



