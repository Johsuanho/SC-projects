"""
File: anagram.py
Name: Johsuan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

dict = {}
ans = []


def main():
    global ans
    read_dictionary()
    print('Welcome to StanCode "Anagram Generator" (or -1 to quit)')
    while True:
        k = input('Find anagrams for: ')
        ans = []
        if k != EXIT:
            find_anagrams(k)
        else:
            break


def read_dictionary():
    """
    This function reads file "dictionary.txt"
    stored in FILE and appends words in each line into a Python List
    """
    global dict
    with open(FILE, 'r') as f:
        for line in f:
            dic = line.strip()
            dict[dic] = 0


def find_anagrams(s):
    """
    :param s: str, the word keyed by the user for anagram search
    :return: no return in this function
    """
    start_time = time.time()
    helper(s, [])
    end_time = time.time()
    print(len(ans), 'anagrams:', ans)
    print('Total run time:', end_time - start_time)


def helper(s, cur):
    """
    :param s: str, the word keyed by the user for anagram search
    :param cur: list, the list used to store the index of possible
                order for anagram
    :return: no return in this function
    """
    global ans
    # base case
    if len(cur) == len(s):
        word = ''
        for i in cur:
            word += s[i]
        if word in dict and word not in ans:
            print('Search...')
            ans.append(word)
            print('Found: ' + word)
    else:
        for j in range(len(s)):
            if j not in cur:
                # choose
                cur.append(j)
                # explore
                helper(s, cur)
                # unchoose
                cur.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for ele in dict:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
