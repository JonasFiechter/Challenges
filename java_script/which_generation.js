/* 
Which Generation Are You?
Try finding your ancestors and offspring with code.

Create a function that takes a number x and a character y ("m" for male, "f" 
for female], and returns the name of an ancestor (m/f] or descendant (m/f].

If the number is negative, return the related ancestor.
If positive, return the related descendant.
You are generation 0. In the case of 0 (male or female], return "me!".
Examples
generation(2, "f"] ➞ "granddaughter"

generation(-3, "m"] ➞ "great grandfather"

generation(1, "f"] ➞ "daughter"
Notes
Check the Resources tab for helpful hints.

Generation	Male	Female
-3	great grandfather	great grandmother
-2	grandfather	grandmother
-1	father	mother
0	me!	me!
1	son	daughter
2	grandson	granddaughter
3	great grandson	great granddaughter

*/

function generation(number, character) {
    const generations = {
                0: ['great grandfather', 'great grandmother'],
                1: ['grandfather', 'grandmother'],
                2: ['father', 'mother'],
                3: ['me!', 'me!'],
                4: ['son', 'daughter'],
                5: ['grandson', 'granddaughter'],
                6: ['great grandson', 'great granddaughter']
    }
    if(number > 3 || number < -3) {
        return -1
    } else {return character === 'm' ? generations[number + 3][0] : generations[number + 3][1]
}
}

console.log(generation(-3, 'm'))