# * Demand - 1 *
def calculate(min, max, step):
  sum = 0
  for i in range(min, max + 1, step): # range(start, stop, step) 不包含stop，所以要+1
    sum += i
  return sum

# print(calculate(1, 3, 1)) # 1 + 2 + 3
# print(calculate(4, 8, 2)) # 你的程式要能夠計算 4+6+8，最後印出 18
# print(calculate(-1, 2, 2)) # 你的程式要能夠計算 -1+1，最後印出 0

# * Demand - 2 *

def avg(data):
  employees = data['employees']
  salarySum = 0
  count = 0
  for employee in employees:
    if employee['manager'] == False:
      salarySum += employee['salary']
      count += 1
  return salarySum // count

result = avg({
  "employees": [
    {
      "name": "John",
      "salary": 30000,
      "manager": False
    },
    {
      "name": "Bob",
      "salary": 60000,
      "manager": True
    },
    {
      "name": "Jenny",
      "salary": 50000,
      "manager": False
    },
    {
      "name": "Tony",
      "salary": 40000,
      "manager": False
    }
  ]
})
# print(result)

# * Demand - 3 *
def func(a):
  def inner(b, c):
    return a + b * c
  return inner

# print(func(2)(3, 4)) # 你補完的函式能印出 2+(3*4) 的結果 14 
# print(func(5)(1, -5)) # 你補完的函式能印出 5+(1*-5) 的結果 0 
# print(func(-3)(2, 9)) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# Q: 為什麼不能這樣寫？
# def funcA(a):
#   def inner(b, c):
#     return b * c
#   return a + inner

# def funcB(a, b, c):
#   def inner(b, c):
#     return b * c
#   return a + inner(b, c)
# TypeError: unsupported operand type(s) for +: 'int' and 'function' (這裡inner還是function誒)

# * Demand - 4 *
def maxProduct(nums):
  maxProduct = float('-inf')
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      maxProduct = max(maxProduct, nums[i] * nums[j])
  return maxProduct

# print(maxProduct([5, 20, 2, 6])) # 得到 120 
# print(maxProduct([10, -20, 0, 3])) # 得到 30 
# print(maxProduct([10, -20, 0, -3])) # 得到 60 
# print(maxProduct([-1, 2])) # 得到 -2 
# print(maxProduct([-1, 0, 2])) # 得到 0 
# print(maxProduct([5,-1, -2, 0])) # 得到 2 
# print(maxProduct([-5, -2])) # 得到 10

# * Demand - 5 *
def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

result=twoSum([2, 11, 7, 15], 9)
# print(result) # show [0, 2] because nums[0]+nums[2] is 9


# * Demand - 6 *
def maxZeros(nums):
  count = 0
  maxCount = 0
  for x in nums:
    # count += 1 if x == 0 else count = 0  # Q: count = 0 --> SyntaxError: invalid syntax
    if x == 0:
      count += 1
    else:
      count = 0
    maxCount = max(maxCount, count)
  return maxCount

# print(maxZeros([0, 1, 0, 0])) # 得到 2
# print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])) # 得到 4 
# print(maxZeros([1, 1, 1, 1, 1])) # 得到 0 
# print(maxZeros([0, 0, 0, 1, 1])) # 得到 3
