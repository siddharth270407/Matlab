"""
=============================================================================
                    MATrix Club - Member Selection Test
                      Python Question 2: The Palindrome Portal
=============================================================================

🌟 THE STORY:
============
Welcome to the mystical world of Wordlandia! You are a brave adventurer who 
has discovered an ancient portal that only opens for magical words called 
"palindromes." These are special words that read the same forwards and 
backwards, like "radar" or "level."

The portal guardian has challenged you: "Only those who can identify the 
magical palindromes shall pass through to the treasure chamber!" You must 
create a spell (program) that can detect these magical words to help other 
adventurers on their quest.

Legend says that palindromes hold ancient power because they represent 
balance and symmetry in the universe. Some famous palindromes include:
- "mom" and "dad" (family magic)
- "radar" (detection magic)
- "level" (balance magic)
- "madam" (respectful magic)

🎯 YOUR QUEST:
=============
Write a Python program that helps adventurers determine if their word is a 
magical palindrome that will open the portal. Your program should check any 
word or phrase and tell them if they can proceed to the treasure chamber.

📋 REQUIREMENTS:
===============
1. Create a function called `is_palindrome(text)` that takes a string as input
2. The function should return True if the text is a palindrome, False otherwise
3. Your check should be case-insensitive (ignore uppercase/lowercase differences)
4. Ignore spaces and punctuation (focus only on letters)
5. Create a main program that asks the user to input text and displays the result
6. Make your program engaging with magical-themed messages

📊 TEST CASES:
=============
Your spell should work correctly for these examples:

Example 1:
Input: "radar"
Output: "✨ 'radar' is a magical palindrome! The portal opens before you! ✨"

Example 2:
Input: "hello"
Output: "😞 'hello' is not a palindrome. The portal remains sealed."

Example 3:
Input: "A man a plan a canal Panama"
Output: "✨ 'A man a plan a canal Panama' is a magical palindrome! The portal opens before you! ✨"

Example 4:
Input: "race a car"
Output: "😞 'race a car' is not a palindrome. The portal remains sealed."

Example 5:
Input: "Was it a rat I saw?"
Output: "✨ 'Was it a rat I saw?' is a magical palindrome! The portal opens before you! ✨"

Example 6:
Input: "Madam"
Output: "✨ 'Madam' is a magical palindrome! The portal opens before you! ✨"

💡 HINTS:
========
1. Convert the string to lowercase for comparison
2. Remove spaces and punctuation before checking
3. Compare the string with its reverse
4. You can reverse a string using slicing: text[::-1]
5. Use string methods like .replace() to remove spaces
6. Consider using .isalpha() to keep only letters
7. Think about how to handle empty strings

📝 INPUT FORMAT:
===============
- Any string (word or phrase) from the user
- May contain uppercase/lowercase letters, spaces, and punctuation

📤 OUTPUT FORMAT:
================
- A magical message indicating if the text is a palindrome
- Include encouraging or consoling words for the adventurer

🎯 EVALUATION CRITERIA:
======================
- Correctness: Does your function correctly identify palindromes?
- Robustness: Does it handle different cases (upper/lower, spaces, punctuation)?
- Code Quality: Is your code clean and well-commented?
- User Experience: Are your messages engaging and clear?
- Algorithm: Is your approach logical and efficient?

⚠️ IMPORTANT NOTES:
==================
- Handle both single words and phrases
- Make your function case-insensitive
- Ignore spaces and punctuation marks
- Add comments to explain your magical algorithm
- Test with various examples to ensure your spell works
- The portal is very picky - make sure your detection is accurate!

🕒 TIME LIMIT: 30 minutes
💯 POINTS: 25 points

📁 SUBMISSION INSTRUCTIONS:
==========================
- Create a new Python file named "Palindrome_Portal_[YourName].py"
- Save your solution in your personal folder inside the "Submissions" folder
- Do NOT modify this question file
- Include your name and roll number as comments at the top of your solution file

May the magic of palindromes guide you on your coding quest! 🏰✨

===============================================================================
                        SUBMISSION TEMPLATE:
===============================================================================

# Name: [Your Full Name]
# Roll Number: [Your Roll Number] 
# Question: Palindrome Portal
# Time: 30 minutes

# Write your solution below this line
"""
