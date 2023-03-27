/*
To the Power of _____
Create a function that takes a base number and an exponent number and returns 
the calculation.

Examples
СalculateExponent(5, 5) ➞ 3125

СalculateExponent(10, 10) ➞ 10000000000

СalculateExponent(3, 3) ➞ 27
Notes
All test inputs will be positive integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
*/

namespace challenges.Challenges.Scripts
{
    public class ToThePowerOf
    {        
        public static int CalculateExponent(int number, int exponent)
        {
            var original = number;
            while (exponent > 1)       
            {
                exponent = exponent - 1;
                number = original * number;
            }
            return number;
        }
    }

}