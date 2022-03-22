/* 
Create a function that takes two numbers as arguments (num, length) and returns 
an array of multiples of num until the array length reaches length.
Examples

arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]

arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]

Notes

Notice that num is also included in the returned array.
*/


function multiples_array(num, length) {
    my_array = []
    for (let i = num; my_array.length < length; i++) {
        if (i % num === 0) {
            my_array.push(i)
        }
    } return my_array
}

console.log(multiples_array(7, 5), multiples_array(12, 10), multiples_array(17, 6))