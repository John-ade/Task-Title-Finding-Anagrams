# Task-Title-Finding-Anagrams
Python Assignment

# Check if two words are anagrams 


def find_anagram(s1, s2):
    print(sorted(s1), sorted(s2))
    if(sorted(s1) == sorted(s2)):
       print(sorted(s1), sorted(s2))
       return True
    return False

print(find_anagram("listen", "silent"))
