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
    def divideAndConquerSol(self,l):
        if l == 0:
            return 0
        q = -9999
        for i in range(0,l):
            q = max(q, top[i][1] + self.divideAndConquerSol(l-i-1))
        return q


if __name__ == '__main__':
    # top = ((1,1),(2,5),(3,8),(4,9),(5,10),(6,17),(7,17),(8,20),(9,24),(10,30))
    top = ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 10),(11,11),(12,1))
    rod_length = 12
    rc = rodCutting(top)
    max_revenue = rc.divideAndConquerSol(rod_length)
    print(max_revenue)