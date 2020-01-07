file = 'moby_dick.txt'
file_read= read(file,mode='r')
print(file.read())
print(file.closed)
file.closed

#import txt file line by line
#file.readline() will print line by line
#context manager, the file will be bound with open('huck_fin.txt')
with open('huck_fin.txt') as file:
    print(file.readline())
    
