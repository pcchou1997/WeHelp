#!/usr/bin/env python
# coding: utf-8

#-----------------第一題-----------------#

def calculate(min, max, step):
    
    # 加總數
    count = int(((max-min)/step)+1)
    
    # 檢查最大值是否為等差數，先試算加總數列最大值
    testMax = min+(count-1)*step
    
    # 判斷試算值==最大值，並計算「等差數列和」
    # 「等差數列和」: (首項+末項)*項數/2
    if testMax != max:
        print(int((min+testMax)/2*count))
    else:
        print(int((min+max)/2*count))

# calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3,最後印出 6
# calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8,最後印出 18
# calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1,最後印出 0




#-----------------第二題-----------------#

def avg(data):
    Money = 0 # 非管理職員工薪資加總
    numNonManager = 0 # 非管理職人數
    
    # 進入資料，若 "manager" == false，加總 "salary"，同時「非管理職人數」+1
    for outdata in data.values():
        for indata in outdata:
                if indata["manager"] == False:
                    Money += indata["salary"]
                    numNonManager += 1
                    
    # 計算非管理職員工平均薪資 = 非管理職員工薪資加總 / 非管理職人數
    print(int(Money/numNonManager))

# avg({"employees":[{"name":"John","salary":30000,"manager":False},
#                   {"name":"Bob","salary":60000,"manager":True},
#                   {"name":"Jenny","salary":50000,"manager":False},
#                   {"name":"Tony","salary":40000,"manager":False}]})
#     # 呼叫 avg 函式





#-----------------第三題-----------------#

def func(a):
    def func2(b,c):
        return(a+b*c)
    return func2

# func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
# func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
# func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# # 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果






#-----------------第四題-----------------#

# 固定一個數，與陣列其他數相乘，若乘積 > 目前相乘最大值，則取代成為目前相乘最大值
def maxProduct(nums):
    maxNum = nums[0]*nums[1]
    for target in nums:
        for others in nums:
            if others != target and target*others > maxNum:
                maxNum = target*others
    print(maxNum)

# maxProduct([5, 20, 2, 6]) # 得到 120
# maxProduct([10, -20, 0, 3]) # 得到 30
# maxProduct([10, -20, 0, -3]) # 得到 60
# maxProduct([-1, 2]) # 得到 -2
# maxProduct([-1, 0, 2]) # 得到 0
# maxProduct([5,-1, -2, 0]) # 得到 2
# maxProduct([-5, -2]) # 得到 10





#-----------------第五題-----------------#

def twoSum(nums, target):
    indexList = []
    for main in nums:
        for sub in nums:
            if main != sub and main + sub == target:
                indexList.append(nums.index(main))
                indexList.append(nums.index(sub))
                return indexList
            
# result=twoSum([2, 11, 7, 15], 9)
# print(result) # show [0, 2] because nums[0]+nums[2] is 9




#-----------------第六題-----------------#

def maxZeros(nums):
    contiZero = 0
    contiZeroList = []
    for i in nums:
      if i == 0:
        contiZero += 1;
      else:
        contiZero = 0;
      contiZeroList.append(contiZero)
    MaxContiZero = max(contiZeroList)
    return MaxContiZero

# maxZeros([0, 1, 0, 0]) # 得到 2
# maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
# maxZeros([1, 1, 1, 1, 1]) # 得到 0
# maxZeros([0, 0, 0, 1, 1]) # 得到 3
