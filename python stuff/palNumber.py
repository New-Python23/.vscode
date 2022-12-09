def checkIfPalindrome(oldNum):
    oldNum = str(oldNum)
    newNum = oldNum[::-1]
    if oldNum == newNum:
        print("This number is a palindrome")
    else:
        print("This number is not a palindrome")

checkIfPalindrome(101)