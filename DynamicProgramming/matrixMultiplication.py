import sys


class matrixMultiplication:

    def bottomUp(self,dim,num):

        mem = [[0 for x in range(num+1)] for y in range(num + 1)]

        print(mem)

        for grp in range(2,num + 1):
            # print("value of grp is",grp)
            #previously the for loop was not looping correctly (for i in range(1,num - grp + 1))
            #so when i was not iterating for last value of loop .Hence an extra 1 is added here.
            for i in range(1,num - grp + 2):
                j = i + grp - 1
                mem[i][j] = sys.maxsize
                for k in range(i,j):
                    q = mem[i][k] + mem[k+1][j] + (dim[i-1] * dim[k] * dim[j])
                    if q < mem[i][j]:
                        mem[i][j] = q
        return mem




if __name__ == '__main__':

    num = 3
    dim = [10,100,5,50]

    obj = matrixMultiplication()
    ans = obj.bottomUp(dim,num)

    print(ans)




