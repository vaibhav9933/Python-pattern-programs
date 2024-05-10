# NOTE :- instread of star (*) we can print anything that we want
# [1] Python program to print
"""
*
**
***
****
*****
or
a
aa
aaa
aaaa
aaaaa
"""

"""
num = int(input("Enter the no of rows:-"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""


# [2] Pyhon program to print
"""
*
***
*****
"""

"""
num = int(input("Enter the no of rows:-"))
k = 1
for i in range(1, num+1):
    for j in range(1, k+1):
        print("*", end="")
    k = k+2
    print()
"""


# [3] Pyhon program to print
"""
    *
   * *
  * * *
 * * * *
"""
"""
num = int(input("Enter the no of rows:-"))
for i in range(0, num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
"""

# [4] Pyhon program to print
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
"""
num = int(input("Enter a number of rows :- "))
for i in range(num, 0, -1):
    for j in range(0, num-i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()
"""


# [5] Pyhon program to print
"""
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""
"""
def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'* '*(i+1))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'* '*(j))
pyramid(10)
"""


# [6] Pyhon program to print
"""
* * * * *
* * * *
* * *
* *
*
"""
"""
num = int(input("Enter a number of rows here:- "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
"""


# [7] Pyhon program to print
"""
  * * *
*       *
*       *
* * * * * 
*       *
*       *
*       *
"""
"""
for row in range(7):
    for col in range(5):
        if ((col == 0 or col ==4) and row!=0) or ((row==0 or row==3) and(col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [8] Pyhon program to print
"""
#a)           b)
* * * *      * * * * * 
*       *    *       *
*       *    *       *
* * * *      * * * * * 
*       *    *       *
*       *    *       *
* * * *      * * * * * 

"""
# a)
"""
for rows in range(7):
    for col in range(5):
        if (col == 0) or (col == 4 and ( rows != 0 and rows != 3 and rows != 6)) or ((rows == 0 or rows == 3 or rows == 6) and (col >0 and col < 4)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""

# b)
"""
for rows in range(7):
    for col in range(5):
        if (col == 0 or col == 4) or ((rows == 0 or rows == 3 or rows == 6) and (col >0 and col < 4)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""


# [9] Pyhon program to print
"""
a)           b)
* * * *       * * * * 
*           *       
*           *       
*           *
*           *       
*           *       
* * * *       * * * * 
"""
# a)
"""
for row in range(7):
    for col in range(5):
        if (col==0) or ((row == 0 or row == 6) and (col>0)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""
# b)
"""
for row in range(7):
    for col in range(5):
        if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col>0)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [10] Pyhon program to print
"""
* * * *
*       *
*       *
*       *
*       *
*       *
* * * * 
"""
"""
for row in range(7):
    for col in range(5):
        if (col == 0) or (col == 4 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col>0 and col<4)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""
# [11] Pyhon program to print
"""
* * * * *
*
*
* * * * *
*
*
* * * * *
"""
"""
for row in range(7):
    for col in range(5):
        if col == 0 or ((row == 0 or row == 3 or row == 6) and (col > 0)):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""


# [12] Pyhon program to print
"""
* * * * *
*
*
* * * * *
*
*
*
"""
"""
for row in range(7):
    for col in range(5):
        if (col == 0) or ((row == 0 or row==3)and col>0):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""

# [13] Pyhon program to print
"""
* * * * *
*
*
*     * * *
*       *
*       *
* * * * *
"""
"""
for row in range(7):
    for col in range(6):
        if col == 0 or (col == 4 and (row != 1 and row != 2)) or ((row == 0 or row == 6) and (col>0 and col<4)) or (row==3 and (col ==3 or col ==5)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [14] Pyhon program to print
"""
*       *
*       *
*       *
* * * * *
*       *
*       * 
*       *
"""
"""
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or (row==3 and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [15] Pyhon program to print
"""
* * * * *
    *
    *
    *
    *
    *
* * * * * 
"""
"""
for row in range(7):
    for col in range(5):
        if col ==2 or ((row ==0 or row == 6) and col!=2 ):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [16] Pyhon program to print
"""
* * * * *
    *
    *
    *
    *
    *
* * *
"""
"""
for row in range(7):
    for col in range(5):
        if col == 2 or (row == 0 and col != 2) or (row==6 and col<2):
           print("*",end=" ")
        else:
            print(end="  ")
    print()
"""
# [17] Pyhon program to print
"""
*       * 
*     *   
*   *     
* *       
*   *     
*     *   
*       * 
"""
"""
i = 0
j = 4
for row in range(7):
    for col in range(5):
        if col == 0 or (row == col+2 and col > 1):
            print("*", end=" ")
        elif ((row==i and col==j) and col>0):
            print("*", end=" ")
            i = i+1
            j = j-1
        else:
            print(end="  ")
    print()
"""


# [18] Pyhon program to print
"""
*         
*         
*         
*         
*         
*         
* * * * * 
"""
"""
for row in range(7):
    for col in range(5):
        if col == 0 or (row == 6 and col > 0):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""


# [19] Pyhon program to print
"""
*           * 
* *       * * 
*   *   *   * 
*     *     * 
*           * 
*           * 
*           * 
"""
"""
for row in range(7):
    for col in range(7):
        if col == 0 or col == 6 or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [20] Pyhon program to print
"""
*         * 
* *       * 
*   *     * 
*     *   * 
*       * * 
*         * 
"""
"""
for row in range(6):
    for col in range(6):
        if (col == 0 or col == 5) or (row == col and (col>0 and col<5)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [21] Pyhon program to print
"""
  * * *   
*       * 
*       * 
*       * 
*       * 
*       * 
  * * *   
"""
"""
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [22] Pyhon program to print
"""
* * * *   
*       * 
*       * 
* * * *   
*         
*         
*         
"""
"""
for row in range(7):
    for col in range(5):
        if col ==0 or (col==4 and (row==1 or row==2)) or ((row ==0 or row==3) and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [23] Pyhon program to print
"""
  * * *   
*       * 
*       * 
*       * 
*       * 
* *     * 
  * * *   
      *   
"""
"""
for row in range(8):
    for col in range(5):
        if ((col==0 or col==4) and (row>0 and row<6)) or ((row==0 or row==6)and (col>0and col<4)) or (row==5 and col==1) or (row==7 and col==3):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [24] Pyhon program to print
"""
* * * *   
*       * 
*       * 
* * * *   
*       * 
*       * 
*       * 
"""
"""
for row in range(7):
    for col in range(5):
        if col==0 or (col==4 and (row!=0 and row!=3)) or ((row==0 or row==3) and(col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [25] Pyhon program to print
"""
  * * *   
*         
*         
  * * *   
        * 
        * 
  * * *   
"""
"""
for row in range(7):
    for col in range(5):
        if ((row==0 or row==3 or row==6)and (col>0 and col<4)) or ((col==0) and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [26] Pyhon program to print
"""
* * * * * 
    *     
    *     
    *     
    *     
    *     
    * 
"""
"""
for row in range(7):
    for col in range(5):
        if col ==2 or (row==0 and col!=2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [27] Pyhon program to print
"""
*       * 
*       * 
*       * 
*       * 
*       * 
*       * 
  * * *
"""
"""
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=6) or(row==6 and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [28] Pyhon program to print
"""
*           * 
  *       *   
    *   *     
      *  
"""
"""
i=0
j=6
for row in range(4):
    for col in range(7):
        if row==col:
            print("*",end=" ")
        elif row==i and col==j:
            print("*",end=" ") 
            i=i+1
            j=j-1
        else:
            print(end="  ")
    print()
"""


# [29] Pyhon program to print
"""
*     *     * 
*   *   *   * 
* *       * * 
*           * 
"""
"""
i = 0
j = 3
for row in range(4):
    for col in range(7):
        if col == 0 or col == 6 or (col == 5 and row == 2) or (col == 4 and row == 1):
            print("*", end=" ")
        elif row == i and col == j:
            print("*", end=" ")
            i = i+1
            j = j-1
        else:
            print(end="  ")
    print()
"""


# [30] Pyhon program to print
"""
*       * 
  *   *   
    *     
  *   *   
*       * 
"""
"""
i = 0
j = 4
for row in range(5):
    for col in range(5):
        if row == i and col == j:
            print("*",end=" ")
            i = i+1
            j = j-1
        elif row == col:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [31] Pyhon program to print
"""
*       * 
  *   *   
    *     
    *     
    * 
"""
"""
for row in range(5):
    for col in range(5):
        if (col == 2 and row > 1) or (row == col and col < 2) or (row == 0 and col == 4) or (row == 1 and col == 3):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
"""


# [32] Pyhon program to print
"""
* * * * * * 
        *   
      *     
    *       
  *         
* * * * * *
"""
"""
i = 1
j = 4
for row in range(0, 6):
    for col in range(0, 6):
        if row == 0 or row == 5:
            print("*", end=" ")
        elif row == i and col == j:
            print("*", end=" ")
            i = i+1
            j = j-1
        else:
            print(end="  ")
    print()
"""


# [33] Pyhon program to print a stars in Hollow Right Triangle shape
"""
* * * * * 
  *     * 
    *   * 
      * * 
        * 
"""
"""
n = int(input("Enter the number of rows:- "))
for row in range(0, n):
    for col in range(0, n):
        if row == 0 or col == (n-1) or row == col:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""


# [34] Pyhon program to print Floyd's Triangle
"""
1 
2 3 
4 5 6 
7 8 9 10
"""
"""
n = int(input("Enter the number of rows:-"))
num = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(num, end=" ")
        num = num+1
    print()
"""


# [35] Pyhon program to print String in Right Triangle Shape
"""
P 
P y 
P y t 
P y t h 
P y t h o 
P y t h o n 
"""
"""
string= input("Enter the string:")
length=len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col],end=" ")
    print()
"""


# [36] Pyhon program to printing numbers in right triangle shape
"""
# a)                b)
1 2 3 4 5            5 5 5 5 5 
1 2 3 4              4 4 4 4
1 2 3                3 3 3
1 2                  2 2
1                    1
"""
# a)
"""
n = int(input("Enter the number of rows:-"))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
"""
# b)
"""
n = int(input("Enter the number of rows:-"))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()
"""


# [37] Pyhon program to printing stars in hollow Equilateral Triangle shape
""" 
a)                     b)
      *                     *
    *   *                 *   *
  *       *             *       *
* * * * * * *         *           *
                    *   *   *   *   * 
"""
# a)
"""
n = int(input("Enter the number of rows"))
for row in range(1,n+1):# for row in range(1,5):
    for col in range(1,2*n):#for col in range (1,8):
        # if row==4 or row+col==5 or col-row==3:
        if row == n or row+col == n+1 or col-row == n-1:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
"""
# b)
"""
n = int(input("Enter the number of rows"))
k=2
for row in range(1,n+1):
    for col in range(1,2*n):
        if row+col == n+1 or col-row == n-1:
            print("*", end=" ")
        elif row == n and col!=k:
            print("*",end=" ")
            k=k+2
        else:
            print(end="  ")
    print()
"""


# [38] Pyhon program to printing stars in Right Triangle shape using while loop
"""
* 
* * 
* * * 
* * * *
"""
"""
num = int(input("Enter the number of rows:- "))
row = 0
while row < num:
    star = row+1
    while star>0:
        print("*", end=" ")
        star = star-1
    row = row+1
    print()
"""
# [39] Pyhon program to printing a stars in pyramid shape using while loop
"""
   * 
  * * 
 * * * 
* * * * 
"""
"""
num = int(input("Enter the numbers of rows :-"))
row = 0
while row < num:
    spcace = num-row-1
    while spcace > 0:
        print(end=" ")
        spcace = spcace-1
    star = row+1
    while star > 0:
        print("*", end=" ")
        star = star-1
    row = row+1
    print()
"""


# [40] Pyhon program to printing  a hollow diamond shape
"""
  *   
 *  *  
*    * 
 *  *  
  * 
"""
"""
for row in range(5):
    for col in range(5):
        if row + col == 2 or row - col == 2 or col - row == 2 or row + col == 6 :
            print("*", end=" ")
        else:
            print(end=" ")
    print()
"""


# [41] Pyhon program for printing stars in heart shape
"""
  * *   * *   
*     *     * 
*           * 
  *       *   
    *   *     
      * 
"""
"""
for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3!=0) or (row == 1 and col%3 == 0) or (row-col==2) or (row + col ==8):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""


# [42] Pyhon program for printing numbers in a square shape
"""
1	2	3	4	5	
16	17	18	19	6	
15	24	25	20	7	
14	23	22	21	8	
13	12	11	10	9
"""
"""
num = int(input("Enter the numbers of rows: "))
n_list = [[0 for x in range(num)] for y in range(num)]
n = 1
low = 0
high = num - 1
count = int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        n_list[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        n_list[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        n_list[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        n_list[j][low]=n
        n=n+1
    low=low+1
    high=high-1
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()
"""


# [43] Pyhon program for printing number pattern(pyramid shape)
"""
      1 
    2 1 2 
  3 2 1 2 3 
4 3 2 1 2 3 4 
"""
"""
num = int(input("Enter a number of rows: "))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end=" ")
    for j in range (i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()
"""


# [44] Pyhon program to printing numbers in right triangle shape
"""
1 
2 6 
3 7 10 
4 8 11 13 
5 9 12 14 15 
"""
"""
num = int(input("enter the number of rows: "))
for row in range(num):
    val = row+1
    dec = num-1
    for col in range(row+1):
        print(val,end=" ")
        val = val +dec
        dec =dec-1
    print()
"""