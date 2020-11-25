from typing import List
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    """
    end_idx = len(nums) - 1
    start_idx = 0
    for i in range(len(nums)):
        if nums[start_idx] == 0:
            nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]

            end_idx += 1
        else:
            start_idx += 1

    end_idx = len(nums) - 1
    start_idx = 0

    while start_idx != end_idx:
        if nums[start_idx] != 0:
            start_idx += 1
            continue
            
        if nums[end_idx] == 0:
            end_idx -= 1
            continue

    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i, len(nums)):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''        
        
class Solution_backtrace:
    def __init__(self):
        self.res = []

    def traceback(self, path, selection, idx):
        if len(selection) == idx :
            new_path = path[:]
            self.res.append(new_path)
            return

        for i in range(idx, len(selection)):
            path.append(selection[i])
            self.traceback(path, selection, i+1)
            path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []

        self.traceback(path, nums, 0)
        return self.res


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        p = root

        if p:
            stack.append(p)
        else:
            return

        while len(stack) != 0:
            item = stack.pop()

            if item.right:
                stack.append(item.right)

            if item.left:
                stack.append(item.left)

            p.right = item
            p.left = None
            p = p.right

'''


def preorder1(root: TreeNode) -> None:
    stack = [root]

    while len(stack) != 0:
        tmp = stack.pop()
        print("Node: %d" % tmp.val)

        if tmp.right:
            stack.append(tmp.right)

        if tmp.left:
            stack.append(tmp.left)

    return

def preorder(root: TreeNode) -> None:
    stack = []

    def visit_left_list(node: TreeNode, stack: List[TreeNode]):

        while node != None:
            print(node.val)

            if node.right:
                stack.append(node.right)

            node = node.left

        return

    sub_right = root

    while True:

        visit_left_list(sub_right, stack)
        if len(stack) == 0:
            break

        sub_right = stack.pop()

    return


def inorder1(root: TreeNode) -> None:
    stack = []

    def push_left_branch(r, s):
        while r != None:
            s.append(r)
            r = r.left

        return

    while True:

        push_left_branch(root, stack)

        if len(stack) == 0:
            break

        tmp = stack.pop()
        print(tmp.val)

        root = tmp.right
    return



if __name__ == '__main__':
    #arr = [1, 2, 3]
    #test = Solution_backtrace()
    #print(test.permute(arr))
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)

    a.left = b
    a.right = c
    b.left = None
    b.right = None
    c.left = d
    c.right = f
    d.left = None
    d.right = e

    #preorder1(a)
    inorder1(a)
