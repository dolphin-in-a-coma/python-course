def print_c(*args,**kargs):
    try:
        print(*args, **kargs)
    except UnicodeEncodeError:
        
    
