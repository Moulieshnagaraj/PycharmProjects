# program based on error handling
from termcolor import cprint
def compare(a=None, b=None, c=None):
    try:
        value=False
        a=int(a)
        b=int(b)
        c=int(c)
        print("VALUES ACCEPTED:",a,b,c)
        if a==b or a==c or b==c:
            value=True
    except ValueError:
        cprint("ValueError: only, numbers are allowed",'blue')
    except TypeError:
        cprint("Index error:Only integers values are allowed",'green')
    except Exception:
        cprint("Other kind of error has been occured",'red')
    finally:
        print("Everything excuted...")
        return value

print("RESULT:",compare(1,5,8))
print('\n')

print("RESULT:", compare('1','2',"3"))
print("\n")

print("RESULT:",compare('a','b','c'))
print('\n')

print("RESULT:",compare(True,' ',' '))
print('\n')

print('RESULT:',compare(True,False, True))
print('\n')

print("RESULT:",compare(" "," ",[1,3]))
print('\n')

print("RESULT:",compare('1','a',True))
print('\n')

print("RESULT:",compare(1,None,None))
print('\n')