// ==================   要求一:函式與流程控制   ==================
// 完成以下函式,在函式中使用迴圈計算最小值到最大值之間,固定間隔的整數總和。
// 其中你可以假設 max 一定大於 min 且為整數,step 為正整數。
// ============================================================

function calculate(min, max, step) {
    count = parseInt(((max - min) / step) + 1);
    testMax = min + (count - 1) * step;
    if (testMax != max) {
        res = ((min + testMax) / 2 * count | 0);
        console.log(res);
    }

    else {
        res = (min + max) / 2 * count;
        console.log(res);
    }
    return res;

}
calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3,最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8,最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1,最後印出 0



// ==================要求二:Python 字典與列表、JavaScript 物件與陣列==================
// 完成以下函式,正確計算出非 manager 的員工平均薪資,所謂非 manager 就是在資料中
// manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工,程式需考慮員工資料數量
// 不定的情況。
// ==============================================================================

function avg(data) {
    let sum = 0;
    let num = 0;
    var dataKey = Object.keys(data); //['employees']
    var content = data[dataKey]; // 'employees'的值（陣列內容）
    dataKeyLen = content.length; // 4
    for (i = 0; i < dataKeyLen; i++) {
        if (content[i].manager == false) {
            sum += content[i].salary;
            num++;
        }
    }
    res = sum / num;
    console.log(res);
    return res;
}

avg({
    "employees": [
        {
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
}); // 呼叫 avg 函式


// =================要求三:=================
// 完成以下函式,最後能印出程式中註解所描述的結果。
// ========================================

function func(a) {
    function func2(b, c) {
        console.log(a + b * c);
        return (a + b * c);
    }
    return func2;
}
func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


// ====================================要求四:====================================
// 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中,兩兩數字相乘後的最大值。
// 提醒:請勿更動題目中任何已經寫好的程式,不可以使用排序相關的內建函式。
// ==============================================================================

function maxProduct(nums) {
    mulMax = nums[0] * nums[1];
    for (i = 0; i < nums.length; i++) {
        for (j = 0; j < nums.length; j++) {
            if (nums[i] * nums[j] > mulMax && i != j) {
                mulMax = nums[i] * nums[j];
            }
        }
    }
    console.log(mulMax);
    return mulMax;
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10


// =========================================要求五:=========================================
// Given an array of integers, show indices of the two numbers such that they add up to a
// specific target. You can assume that each input would have exactly one solution, and you
// can not use the same element twice.
// ========================================================================================

function twoSum(nums, target) {
    var result = [];
    for (i = 0; i < nums.length; i++) {
        for (j = 0; j < nums.length; j++) {
            if (nums[i] + nums[j] == target && i != j) {
                result.push(i, j);
                // result.push(j)
                return result;
            }
        }
    }
}

let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


// ================================要求六 ( Optional ):================================
// 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。
// ===================================================================================

function maxZeros(nums) {
    var contiZero = 0;
    var contiZeroList = [];

    //把 contiZero(0累積數量) 裝進 陣列
    for (i = 0; i < (nums.length); i++) {
        if (nums[i] == 0) {
            contiZero++;
        }
        else {
            contiZero = 0;
        }
        contiZeroList.push(contiZero);
    }

    // 求陣列最大值
    var maxContiZero = 0;
    for (j = 0; j < (contiZeroList.length); j++) {
        if (contiZeroList[j] > maxContiZero) {
            maxContiZero = contiZeroList[j];
        }
    }
    console.log(maxContiZero);
    return maxContiZero;
}
maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3