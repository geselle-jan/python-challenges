def leftpad(value, length):
    output = str(value).zfill(length)[-length:]
    if length == 0:
        output = ''
    return output
print 'This is the output: '
print leftpad(12323,0)





