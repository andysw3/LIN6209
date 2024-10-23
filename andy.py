
def all_ops_part1(int1,int2):
    return (int1+int2, int1-int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2)

#all_ops_part1(5,3)

def all_ops_part2(int1,int2):
    return (int1<int2, int1<=int2, int1==int2, int1!=int2, int1>=int2, int1>int2)

#all_ops_part2(5,3)

#assert all_ops_part1(5,3) == (8, 2, 15, 5/3, 1, 2)

#ssert all_ops_part2(5,3) == (False,False,False,True,True,True)


def magic_number(a_num):
    return "7" in str(a_num)


def hms_to_s(hours,minutes,seconds):
    return(hours*60*60+minutes*60+seconds)

def s_to_hms(seconds):
    hours = (seconds//3600)
    minutes =( seconds%3600)//60
    second = seconds%60
    return(hours,minutes,second)

#assert s_to_hms(5950)==(1,39,10)


def add_hms(hr1,min1,sec1,hr2,min2,sec2):
    total_seconds= hms_to_s(hr1,min1,sec1) + hms_to_s(hr2,min2,sec2)
    return s_to_hms(total_seconds)

#assert add_hms(0,0,3600,0,0,61) == (1,1,1)

def old_uk_psp_to_p(pounds,shillings,pennies):
    return pounds*240 +  shillings*12 + pennies

#assert old_uk_psp_to_p(1,0,1)== 241

def old_uk_p_to_psp(pennies):
    pounds=pennies//240
    shillings=(pennies%240)//12
    last_pennies=(pennies%240)%12
    return(pounds,shillings,last_pennies)

#assert old_uk_p_to_psp(0) == (0,0,0)
    
def add_old_uk(pounds1,shillings1,pennies1,pounds2,shillings2,pennies2):
    total_pennies= old_uk_psp_to_p(pounds1,shillings1,pennies1)+ old_uk_psp_to_p(pounds2,shillings2,pennies2)
    return old_uk_p_to_psp(total_pennies)

#assert add_old_uk(0,19,11,19,0,1)== (20,0,0)

def is_palindrome(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    return phrase == phrase[::-1]

#assert is_palindrome("Abba")

def 