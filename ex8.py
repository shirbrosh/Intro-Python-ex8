####### part 1 #######


def check_row(row, num, board):
    """A function that returns True if a given number appear in a given row in
    the game board or False otherwise"""
    return num in board[row]


def check_column(column, num, board):
    """A function that returns True if a given number appear in a given column
    in the game board or False otherwise"""
    for row in board:
        if row[column] == num:
            return True
    return False


def check_square(row, col, num, board):
    """A function that returns True if a given number appear in a given square
    in the game board or False otherwise"""
    # finding the start row and column of the square:
    begin_row = int(((row // (len(board) ** 0.5)) * (len(board) ** 0.5)))
    end_row = int(begin_row + (len(board) ** 0.5))
    # finding the end row and column of the square:
    begin_col = int(((col // len(board) ** 0.5) * len(board) ** 0.5))
    end_col = int(begin_col + len(board) ** 0.5)
    for i in range(begin_row, end_row):
        for j in range(begin_col, end_col):
            if board[i][j] == num:
                return True
    return False


def is_empty(board, col, row):
    """A function that returns True if the given cell is already filled or
    False if its empty"""
    if board[row][col] != 0:
        return True
    return False


def illegal_placement(row, col, num, board):
    """A function that returns True if its illegal to assign a number to a
    specific cell (illegal assign will be if the number already appears in the
    same row, column or square or if the cell is full) or False otherwise"""
    if check_column(col, num, board) or check_row(row, num, board) or \
            check_square(row, col, num, board) or is_empty(board, col, row):
        return True
    else:
        return False


def fill_sudoku_col(board, col, num):
    """A function that fills the sudoku board using recursion, it receives a
    number and a game board and fills the number according to the game rules
    moving threw columns and rows"""
    if col == len(board):
        return solve_sudoku_help(board, num + 1)
    if check_column(col, num, board):
        return fill_sudoku_col(board, col + 1, num)
    for row in range(len(board)):
        if illegal_placement(row, col, num, board):
            continue
        board[row][col] = num
        if fill_sudoku_col(board, col + 1, num):
            return True
        board[row][col] = 0
    return False


def solve_sudoku_help(board, num):
    """A function that operates the function- 'fill_sudoku_col' each time on a
    different number using recursion"""
    if num == len(board) + 1:
        return True
    if fill_sudoku_col(board, 0, num):
        return True
    return False


def solve_sudoku(board):
    """A function that receives a sudoku board and solves the game, if the game
    can be solved it will return True otherwise it will return False"""
    original_board = board
    if solve_sudoku_help(board, 1):
        return True
    board = original_board
    return False


####### part 2 #######
# question 1 #

def print_set(cur_set):
    """A function that receives a list filled with True and False and prints a
    list of all the indexes that had a True value"""
    sub_list = []
    for (idx, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            sub_list.append(idx)
    print(sub_list)


def k_subset_helper(cur_set, k, index, picked):
    """A function that receives a list, and 3 numbers-k, index, picked, and
    recursively go through the numbers and operates the function print_set"""
    if k == picked:
        print_set(cur_set)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    k_subset_helper(cur_set, k, index + 1, picked + 1)
    cur_set[index] = False
    k_subset_helper(cur_set, k, index + 1, picked)


def print_k_subsets(n, k):
    """A function that receives 2 numbers- n,k and prints all the subsets from
    0 to n-1 by length k """
    if k < 0:
        pass
    print_bad_input = bad_input(n, k)
    if print_bad_input is not False:
        print(bad_input(n, k))
    else:
        cur_set = [False] * n
        k_subset_helper(cur_set, k, 0, 0)


# question 2 #


def print_set_lst(cur_set, lst):
    """A function that receives a list filled with True and False and another
    list and adds to the list lists of all the indexes that had a True value"""
    sub_list = []
    for (idx, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            sub_list.append(idx)
    lst.append(sub_list)


def k_subset_helper_lst(cur_set, k, index, picked, lst):
    """A function that receives 2 lists- cur_set and lst, and 3 numbers-k,
    index, picked, and recursively go through the numbers and operates the
    function print_set"""
    if k == picked:
        print_set_lst(cur_set, lst)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    k_subset_helper_lst(cur_set, k, index + 1, picked + 1, lst)
    cur_set[index] = False
    k_subset_helper_lst(cur_set, k, index + 1, picked, lst)


def fill_k_subsets(n, k, lst):
    """A function that receives 2 numbers- n,k and fills a list with all the
    subsets from 0 to n-1 by length k"""
    if k < 0:
        pass
    lst = bad_input(n, k)
    if lst is not False:
        pass
    else:
        lst= []
        cur_set = [False] * n
        k_subset_helper_lst(cur_set, k, 0, 0, lst)


# question 3 #


def k_subset_helper_return(n, k, index):
    """A function that builds sub lists in recursion and returns a list of all sub
    lists"""
    if index == k - 1:
        first_lst = []
        for i in range(n - k + 1):
            first_lst.append([i])
        return first_lst
    first_index_list = k_subset_helper_return(n, k, index + 1)
    result_lst = []
    for lst in first_index_list:
        for i in range(lst[-1] + 1, n):
            subset_list = lst + [i]
            result_lst.append(subset_list)
    return result_lst


def return_k_subsets(n, k):
    """A function that receives 2 numbers- n,k and returns a list with all the
    subsets from 0 to n-1 by length k"""
    if k < 0:
        pass
    print_bad_input = bad_input(n, k)
    if print_bad_input is not False:
        return bad_input(n, k)
    else:
        return k_subset_helper_return(n, k, 0)


def bad_input(n, k):
    """A function that checks the inputs and returns a result suitable according to
    the demands"""
    if k == 0:
        return [[]]
    elif (n == 0 and k != 0) or n < k:
        return []
    else:
        return False


