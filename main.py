# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def list_gen():
    a_lst = list(input().split(' '))
    a_len = a_lst[0][0]
    a_lst.insert(1, a_lst[0][2:]); a_lst.pop(0)

    b_lst = list(input().split(' '))
    b_len = b_lst[0][0]
    b_lst.insert(1, b_lst[0][2:]); b_lst.pop(0)
    a_lst = list(map(int, a_lst))
    a_len = int(a_len)
    b_lst = list(map(int, b_lst))
    b_len = int(b_len)
    print(a_lst)
    return a_len, a_lst, b_len, b_lst

def con(a_list, a_length, b_list, b_length):
    a_list = dict(enumerate(a_list))
    b_list = dict(enumerate(b_list))
    N = a_length + b_length - 1
    x0 = [0 for _ in range(N)]
    X = []
    for i in range(N):
        s = 0
        for j in range(a_length):
            s += a_list[j] * b_list.get(i - j, 0)
        x0[i] = s
        X.append(x0)
    return X


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """
3,1 2 3
4,4 5 6 7
    """
    a_len, a_lst, b_len, b_lst = list_gen()
    #print(a_len, a_lst, b_len, b_lst)
    print(con(a_len, a_lst, b_len, b_lst))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
