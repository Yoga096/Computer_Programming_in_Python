while True :
    try :
        a = eval(input())
        b = int(input())
        c = a/b
        print(str(a) + "/" + str(b), "= %.2f" %c)
        break
    except NameError:
        print('NameError')
    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')