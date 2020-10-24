# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sort


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def run_sort_test():
    test_arr = [
        [1],
        [],
        [1, 2],
        [2, 1],
        [2, 12, 4, 34, 1],
    ]

    for arr in test_arr:
        print("Orign arr = %s" % arr)
        #sort_arr = sort.select_sort(arr)
        #sort_arr = sort.bubble_sort(arr)
        #sort_arr = sort.insertion_sort(arr)
        sort_arr = sort.shell_sort(arr)
        print("Sort arr = %s" % sort_arr)
        #print("Orign arr = %s" % arr)

def arg_pass(a, b):
    a[0], b[0] = b[0], a[0]

if __name__ == '__main__':
    print_hi('PyCharm')
    run_sort_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
