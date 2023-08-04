class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = []

        for letter in s.lower():
            if letter.isalnum():
                new_string.append(letter)

        backwards = new_string[::-1]
        return new_string == backwards


'''
Commentary: This iterates through the string one time, and then checks equality which is two passes. 
This is O(n)
I initially tried to use .reverse() but that changes the input inplace so I decided to use slicing instead
'''