"""
=============================================================================
                    MATrix Club - Member Selection Test
                        Python Question 1: Prime Number Detective
=============================================================================

🔍 THE STORY:
============
You are a detective working for the Mathematical Investigation Bureau (MIB). 
Your latest case involves catching a notorious number thief who only steals 
"prime numbers" from a bank's security vault. The bank's security system 
needs your help to identify which numbers in their vault are prime numbers 
so they can put extra protection on them.

A prime number is a special number that has exactly two factors: 1 and itself.
For example, 7 is prime because it can only be divided by 1 and 7 without 
leaving a remainder.

🎯 YOUR MISSION:
===============
Write a Python program that helps the bank identify whether a given number 
is prime or not. Your program should be able to check any positive integer 
and tell the bank security team if they need to put extra protection on it.

📋 REQUIREMENTS:
===============
1. Create a function called `is_prime(number)` that takes a positive integer as input
2. The function should return True if the number is prime, False otherwise
3. Handle special cases properly (numbers less than 2 are not prime)
4. Create a main program that asks the user to input a number and displays the result
5. Make your program user-friendly with clear messages

📊 TEST CASES:
=============
Your program should work correctly for these examples:

Example 1:
Input: 7
Output: "7 is a prime number! 🚨 EXTRA SECURITY NEEDED!"

Example 2:
Input: 12
Output: "12 is not a prime number. Regular security is sufficient."

Example 3:
Input: 2
Output: "2 is a prime number! 🚨 EXTRA SECURITY NEEDED!"

Example 4:
Input: 1
Output: "1 is not a prime number. Regular security is sufficient."

Example 5:
Input: 29
Output: "29 is a prime number! 🚨 EXTRA SECURITY NEEDED!"

💡 HINTS:
========
1. Remember that prime numbers are greater than 1
2. The number 2 is the only even prime number
3. To check if a number is prime, try dividing it by all numbers from 2 to √n
4. If any division results in remainder 0, the number is not prime
5. You can use the modulo operator (%) to check remainders
6. Consider using a loop to check all possible divisors

📝 INPUT FORMAT:
===============
- A positive integer from the user
- Your program should handle invalid inputs gracefully

📤 OUTPUT FORMAT:
================
- A clear message stating whether the number is prime or not
- Include the security recommendation for the bank

🎯 EVALUATION CRITERIA:
======================
- Correctness: Does your function identify prime numbers correctly?
- Code Quality: Is your code readable and well-structured?
- User Experience: Are your messages clear and helpful?
- Edge Cases: Do you handle special cases (like 1, 2, negative numbers)?
- Efficiency: Is your algorithm reasonably efficient?

⚠️ IMPORTANT NOTES:
==================
- Do not use any built-in prime checking functions
- Write your own algorithm from scratch
- Add comments to explain your logic
- Test your function with multiple examples
- Make sure your code runs without errors

🕒 TIME LIMIT: 30 minutes
💯 POINTS: 25 points

📁 SUBMISSION INSTRUCTIONS:
==========================
- Create a new Python file named "Prime_Detective_[YourName].py"
- Save your solution in the "Submissions" folder
- Do NOT modify this question file
- Include your name and roll number as comments at the top of your solution file

Good luck, Detective! The Mathematical Investigation Bureau is counting on you! 🕵️‍♀️

===============================================================================
                        SUBMISSION TEMPLATE:
===============================================================================

# Name: [Your Full Name]
# Roll Number: [Your Roll Number] 
# Question: Prime Number Detective
# Time: 30 minutes

# Write your solution below this line
"""
