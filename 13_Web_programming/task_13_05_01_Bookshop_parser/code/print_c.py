def print_c(first, *args,**kargs):
    try:
        print(first, *args, **kargs)
    except UnicodeEncodeError as err:
        print(err.start, err.end)
        print_c(first[:err.start], *args, **kargs)
    except Exception as err:
        print (err)
    
