def leftpad(value, length):
    output = str(value).zfill(length)[-length:]
    return output
print 'This is the output'
print leftpad(12323,12)





