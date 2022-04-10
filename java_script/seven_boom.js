/*
Create a function that takes an array of numbers and return "Boom!" 
if the digit 7 appears in the array. Otherwise, return "there is no 7 in the 
array".
Examples

sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!"
// 7 contains the number seven.

sevenBoom([8, 6, 33, 100]) ➞ "there is no 7 in the array"
// None of the items contain 7 within them.

sevenBoom([2, 55, 60, 97, 86]) ➞ "Boom!"
// 97 contains the number seven.
*/
const test = [2, 55, 60, 97, 86]

const seven_boom = function(arr) {
    for (let i = 0; i < arr.length; i++) {
        arr_in = arr[i].toString()
        if (arr[i] === 7) {
            return 'Boom!'
        } else {
            for (let i_2 = 0; i_2 < arr_in.length; i_2++) {
                if (arr_in[i_2] === '7') {
                    return 'Boom!'
                }
            }
        }
    } return 'there is no 7 in array'
}

console.log(seven_boom(test))