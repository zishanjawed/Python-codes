""""
Name : One of the most efficient way to find the Nth febonacci number

@aurthor: Zishan Jawed
"""
def febonacci(dic, N):
    """
    input : dic is a dictionry(a predefine data structure) to keep the record of the
    calculation that has been already done , N is the number whoes febonacci is to find

    output: Check if the calculation for a particular number is already done, return the value
    of if not calculate the value for that particular number by calling itself(recoursively) and
    store the value in dic
    """
    if N in dic:
        return dic[i]
    else:
        ans = febonacci(N-1) + febonacci(N-2)
        dic[N] = ans
        return ans
    
N = (int)(input("Enter the Number : "))
dic = {1:1, 2:2}
febonacci(dic,N)
