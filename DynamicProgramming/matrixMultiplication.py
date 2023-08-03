class matrixMultiplication:

    def bottomUp(self,dim,num):

        mem = [[-999 for x in range(num)] for y in range(num)]

        for i in range(num):
            mem[i][i] = 0

        for grp in range(2,num+1):
            for i in range(1,num):
                j = i + grp - 1
                for k in range(i,j):
                    q = mem[i][k] + mem[k+1][j] + (dim[k][1] * dim[j][0] * dim[j][1])
                    if q < mem[i][j]:
                        mem[i][j] = q
        return mem




if __name__ == '__main__':

    num = 3
    dim = [[10,100],[100,5],[5,50]]

    obj = matrixMultiplication()
    ans = obj.bottomUp(dim,num)

    print(ans)




