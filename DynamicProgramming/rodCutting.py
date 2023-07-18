# divide and conquer version of rod cutting.


class rodCutting:

    def __init__(self,top):
        self.top = top
        # self.l = l
    def max(self,x,y):
        if x > y:
            return x
        else :
            return y

    #top - table of price , l = lenght of rod
    def naiveRecursiveSol(self,l):
        if l == 0:
            return 0
        q = -9999
        for i in range(0,l):
            q = max(q, top[i][1] + self.naiveRecursiveSol(l-i-1))
        return q

    '''
    max(q, top[0][1] + naiveRecursiveSol(3) ) , max(q, top[1][1] + naiveRecusiveSol(2)) , max(q,top[2][1] + naiveRecursiveSol(1)) , max(q, top[3][1] + naiveRecursiveSol(0))
    '''


    def top_down_aux(self,top,len,rev):
        if len == 0:
            return 0
        if rev[len-1] >= 0:
            return rev[len-1]
        else:
            q = -9999
            for i in range(len):
                q = max(q,top[i][1] + self.top_down_aux(top,len - 1 - i,rev))
            rev[len-1] = q
        return q

    ''' top_down_aux(top,4,rev) = max(q, top[0][1] + top_down_aux(top,3, rev)) , max(q, top[1][1] + top_down_aux(top,2,rev) , max(q,top[2][1] + top_down_aux(top,1,rev))),
    max(q,top[3][1] + top_down_aux(top,0, rev))'''


    #top-down (memoization) solution
    # p - price and length array.
    # r - revenue array.
    # l - length of array.

    def top_down(self,top,len):
        rev = [-9999] * len
        return self.top_down_aux(top,len,rev)


    def bottom_up(self,top,len):
        rev = []
        rev.append(0)
        for j in range(1,len + 1):
            q = -9999
            for i in range(1,j+1):
                q = max(q,top[i-1][1] + rev[j-i])

            rev.append(q)
        return rev[len]


if __name__ == '__main__':
    #table of price = top
    top = ((1,1),(2,5),(3,8),(4,9),(5,10),(6,17),(7,17),(8,20),(9,24),(10,30))
    # top = ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 10),(11,11),(12,1))
    rod_length = 6
    rc = rodCutting(top)
    max_revenue_naive = rc.naiveRecursiveSol(rod_length)
    max_revenue = rc.top_down(top,rod_length)
    max_revenue_bot = rc.bottom_up(top,rod_length)
    print(max_revenue == max_revenue_naive)

    print(max_revenue)
    print(max_revenue_naive)
    print(max_revenue_bot)
