/* 
'''
Track the Robot (Part 2)
This robot roams around a 2D grid. It starts at (0, 0) facing North. After each 
time it moves, the robot rotates 90 degrees clockwise. Given the amount the 
robot has moved each time, you have to calculate the robot's final position.

To illustrate, if the robot is given the movements 20, 30, 10, 40 then it will 
move:

20 steps North, now at (0, 20)
30 steps East, now at (30, 20)
10 steps South. now at (30, 10)
40 steps West, now at (-10, 10)
...and will end up at coordinates (-10, 10).

Examples
trackRobot(20, 30, 10, 40) ➞ [-10, 10]

trackRobot() ➞ [0, 0]
// No movement means the robot stays at (0, 0).

trackRobot(-10, 20, 10) ➞ [20, -20]
// The amount to move can be negative.
'''
*/

const trackRobot = function (...steps) {
    let lst = steps
    let [n, e, s, w] = lst

    for (let i=1; i == lst.length; i++) {
        if (!lst[i]) {
            lst[i] = 0
        }
    }

    return [e - w, n - s]
}

console.log(trackRobot(20, -30, 10, 40))
console.log(trackRobot(1, 2, 3, 4))
console.log(trackRobot(undefined, undefined, undefined, undefined ))