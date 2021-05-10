"""
File: boggle.py
Name: Johsuan
----------------------------------------
This programs runs the boggle game for the 4X4 digits given by the user.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

SIZE = 4                                  # define the size of the boggle
WORD_LENGTH = 4                           # define the minimum length of the found word

dict = {}
count = 0


def main():
    """
    This programs runs the boggle game for the 4X4 digits given by the user.
    """
    read_dictionary()
    boggle = boggle_lst([])
    # search within the boggle and use each letter as the start point of the game
    for i in range(SIZE):
        for j in range(SIZE):
            search(i, j, boggle, [], [])
    print('There are', count, 'words in total.')


def search(x, y, lst, cur, final):
    """
    :param x: x index for the given digit
    :param y: y index for the given digit
    :param lst: list, the boggle list that user entered
    :param cur: list, the temporary list for boggle calculation
    :param final: list, the final list of boggle found
    :return: there is no return in this function
    """
    # Base case
    global count
    if len(cur) == WORD_LENGTH:
        if cur[0] == cur[2] or cur[1] == cur[3] or cur[2] == cur[3]:
            pass
        else:
            word = ''
            for tuple in cur:
                i = tuple[0]
                j = tuple[1]
                word += lst[i][j]
            if word in dict and word not in final:
                final.append(word)
                print('Found: ' + word)
                count += 1
    if len(cur) > WORD_LENGTH:
        if cur[2] == cur[4]:
            pass
        else:
            word = ''
            for tuple in cur:
                i = tuple[0]
                j = tuple[1]
                word += lst[i][j]
            if word in dict and word not in final:
                final.append(word)
                print('Found: ' + word)
                count += 1
    else:
        # Choose
        cur.append((x, y))
        # Explore
        for m in range(-1, 2):
            for n in range(-1, 2):
                if m == 0 and n == 0:
                    pass
                else:
                    if 0 <= x+m <= 3 and 0 <= y+n <= 3:
                        search(x+m, y+n, lst, cur, final)
        # Un-choose
        cur.pop()


def boggle_lst(lst):
    """
    :return: the boggle list entered and prepared for word search
    """
    for i in range(SIZE):
        row = input('Please enter rows of letter: ')
        if ' ' not in row or len(row) != SIZE+3:
            print('Illegal Format!')
        else:
            k = row.lower().split(' ')
            lst.append(list(k))
    return lst


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global dict
    with open(FILE, 'r') as f:
        for line in f:
            dic = line.strip()
            dict[dic] = 0


def has_prefix(sub_s):
    """
    :param sub_s: str, A substring that is constructed by neighboring letters
    on a 4x4 square grid
    :return: bool, If there is any words with prefix stored in sub_s
    """
    for ele in dict:
        if ele.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
