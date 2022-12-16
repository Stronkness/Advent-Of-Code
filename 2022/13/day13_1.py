import ast

def cmp(left, right):
    # Pre-condition to see if empty lists exist in the input, makes code faster
    if type(left) != int and type(right) != int:
        if len(left) == 0 and len(right) > 0:
            return -1
        elif len(left) > 0 and len(right) == 0:
            return 1
        elif len(left)== 0 and len(right) == 0:
            return 0

    if type(left) == int and type(right) == int: # straight up comparision
        return left - right
    if type(left) == list and type(right) == int: # recursively return right as a list to get to the condition which requires two lists so comparision can happen
        right = [right]
        return cmp(left, right)
    if type(left) == int and type(right) == list: # recursively return left as a list to get to the condition which requires two lists so comparision can happen
        left = [left]
        return cmp(left, right)
    if type(left) == list and type(right) == list: # time for real comparision
        for l,r in zip(left, right): # compare one element at a time from both lists, one index at a time
            approved = cmp(l,r) # first condition of this function
            if approved != 0: # the numbers at this index is not the same and we can draw a conclusion if its above 0 or not
                return approved
        # if all else "fails" we can then check length of the list to see which is bigger, if right is bigger than left then it is correct
        if len(left) > len(right):
            return 1
        if len(right) > len(left):
            return -1 # this is what we are looking for
        else:
            return 0 # same length and same elements

lists = open('input').read().split('\n\n')
result_indexing = 0

for i, check in enumerate(lists):
    check = check.split('\n')
    left, right = ast.literal_eval(check[0]), ast.literal_eval(check[1]) # string representation of list to list
    if cmp(left, right) < 0: # this is the case if left is smaller than right and in the right order then
        result_indexing += i+1

print(result_indexing)