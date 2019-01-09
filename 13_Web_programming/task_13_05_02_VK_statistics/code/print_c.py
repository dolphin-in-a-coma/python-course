def print_c(first, *args,**kargs):
    try:
        print(first, *args, **kargs)
    except UnicodeEncodeError as err:
        print_c(first[:err.start], first[err.end:], *args, **kargs)
    
