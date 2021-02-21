

'''

 | | | | 0
-------- 1
 | | | | 2
-------- 3
 | | | | 4
012345678

'''

max_row=49
min_columns=204

def board(rows,columns):
    if (rows>max_row or columns>min_columns) or (rows<=1 or columns<=1):
        print("The board is not available ")
        return False
    for row in range(0,rows):

        if row %2==0:
            for col in range (0,columns):
                if col %2==0:
                    space=''
                    if col==columns-1:
                        space='/n'
                        print(" ",end=space)
                    else:
                        print(" ",end=space)
                else:
                    print("|",end='')
        else:
            print("")
            print('-'*columns)

    return True


rows=int(input("Enter row size:").strip())

columns=int(input("Enter columns size:").strip())
board(rows,columns)


