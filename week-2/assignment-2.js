// Demand - 1
function calculate(min, max, step) {
  let sum = 0
  for (let i = min; i <= max; i += step) {
    sum += i
  }
  return sum
}

// console.log(calculate(1, 3, 1)) // 你的程式要能夠計算 1+2+3，最後印出 6 
// console.log(calculate(4, 8, 2)) // 你的程式要能夠計算 4+6+8，最後印出 18 
// console.log(calculate(-1, 2, 2)) // 你的程式要能夠計算 -1+1，最後印出 0


// Demand - 2
function avg(data) {
  const employees = data.employees
  let num = 0
  let sum = 0
  for (let employee of employees) {
    if (employee.manager === false) {
      num ++
      sum += employee.salary
    }
  }
  return sum / num
}

const data = {
  "employees": [{
      "name": "John",
      "salary": 30000,
      "manager": false
    },
    {
      "name": "Bob",
      "salary": 60000,
      "manager": true
    },
    {
      "name": "Jenny",
      "salary": 50000,
      "manager": false
    },
    {
      "name": "Tony",
      "salary": 40000,
      "manager": false
    }
  ]
}
// console.log(avg(data))


// * Demand - 3 *
function func(a) {
  return (b, c) => a + b * c
}

// console.log(func(2)(3, 4)) // 你補完的函式能印出 2+(3*4) 的結果 14
// console.log(func(5)(1, -5)) // 你補完的函式能印出 5+(1*-5) 的結果 0
// console.log(func(-3)(2, 9)) // 你補完的函式能印出 -3+(2*9) 的結果 15 
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

// * Demand - 4 *
// 方法一：O(n^2)
function maxProduct(nums) {
  let maxProduct = -Infinity
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = Number(i) + 1; j < nums.length; j++) {
      maxProduct = Math.max(maxProduct, nums[i] * nums[j])
    }
  }
  return maxProduct
}

// console.log(maxProduct([5, 20, 2, 6])) // 得到 120 
// console.log(maxProduct([10, -20, 0, 3])) // 得到 30 
// console.log(maxProduct([10, -20, 0, -3])) // 得到 60 
// console.log(maxProduct([-1, 2])) // 得到 -2 
// console.log(maxProduct([-1, 0, 2])) // 得到 0 或 -0 
// console.log(maxProduct([5, -1, -2, 0])) // 得到 2 
// console.log(maxProduct([-5, -2])) // 得到 10

// Demand - 5
function twoSum(nums, target) {
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = Number(i) + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j]
    }
  }
}
let result = twoSum([2, 11, 7, 15], 9);
// console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


// Demand - 6
function maxZeros(nums) {
  let maxCount = 0
  let count = 0
  for (let i of nums) {
    i === 0 ? count++ : count = 0
    maxCount = Math.max(maxCount, count)
  }
  return maxCount
}
// console.log(maxZeros([0, 1, 0, 0])); // show 2
// console.log(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])); // show 4
// console.log(maxZeros([1, 1, 1, 1, 1])); // show 0
// console.log(maxZeros([0, 0, 0, 1, 1])) // show 3