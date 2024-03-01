import sys
def get_triangle(rows: int): #-> List[List[int]]
 #which will return the triangle as a list of lists with the specified number of rows:
        get_triangle = []
        for i in range(0, rows): #making amount of rows
          row = [] #empty row
          for j in range(0, i+1): #i - amount of elements in each list
            if j==0 or j==i:#if this element is the 1st or the last in a row it=1
                j=1
            else:
                j=get_triangle[i-1][j-1] + get_triangle[i-1][j]

            row.append(j)
          get_triangle.append(row)
        return(get_triangle)

rows = int(sys.argv[1])
x = get_triangle(rows)

for i in range(0,len(x)):
    y =" "*(len(x)-i)
    for j in x[i]:
        y+=str(j)+' '
    print(y)

