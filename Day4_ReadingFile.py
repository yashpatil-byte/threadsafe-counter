with open('test.txt','r') as f:
    size_to_read = 3
    f_contents = f.read(size_to_read)
    print(f_contents, end = '*')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents, end = '')
    
    ''' 
    f_content = f.readlines()
    print(f_content)
    print(f.readlines()) # This will print [] because the file pointer is at the end of the file adter readlines() method
    '''
