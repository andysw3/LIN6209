
def all_ops_part1(int1,int2):
    return (int1+int2, int1-int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2)

#all_ops_part1(5,3)

def all_ops_part2(int1,int2):
    return (int1<int2, int1<=int2, int1==int2, int1!=int2, int1>=int2, int1>int2)

#all_ops_part2(5,3)

assert all_ops_part1(5,3) == (8, 2, 15, 5/3, 1, 2)

assert all_ops_part2(5,3) == (False,False,False,True,True,True)