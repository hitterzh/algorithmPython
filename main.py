# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sort
import graph_algo

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
        #!!!sort_arr = sort.shell_sort(arr)
        #!!!sort_arr = sort.merge_sort(arr)
        sort_arr = sort.quick_sort(arr)
        print("Sort arr = %s" % sort_arr)
        #print("Orign arr = %s" % arr)

def run_lookup_test():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    graph_algo.bfs(graph, "you")


if __name__ == '__main__':
    print_hi('PyCharm')
    #    run_sort_test()
    run_lookup_test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
