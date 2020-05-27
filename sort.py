
#SAMPLE LISTS FOR SORTING
#numeric lists
list0 = []
list1 = [1]
list2 = [-4, 1, 0, 19, 2.23, -12, 99, -99, 16.4, 5.25, 37]
list3 = [-9, 1, -9, 14, 18, -12.6, 1509, 43.7, -12.6, 4]
#other lists
strlist = ["hello", "I'm gonna talk until you fall asleep", "hi", "", "this is a long greeting"]
lencomp = lambda str1, str2 : len(str1) > len(str2)

class Student :
    def __init__(self, name, grade, average) :
        self.name = name
        self.grade = grade
        self.avg = average
    def __repr__(self) :
        res = "({}: In grade {} - Avg is {})".format(self.name, self.grade, self.avg)
        return res

student_list = [Student("Daniel", 12, 97), Student("Adam", 12, 100), Student("Evan", 10, 55)]
def compare_students(s1, s2) :
    if s1.grade > s2.grade:
        return True
    elif s1.grade < s2.grade:
        return False
    elif s1.name > s2.name:
        return True
    elif s1.name < s2.name:
        return False
    elif s1.avg > s2.avg:
        return True
    else :
        return False
#-------------------------------


#O(n)
def bubble_sort(arr, left_GreaterThan_right=lambda a, b: a > b) :
    """
    Bubble-right to get largest element, n-1 times. Afterwards, 
    the last element (at index 0) is guaranteed to be the smallest
    """
    for _ in range(len(arr) - 1) :
        for i in range(len(arr) - 1) :
            if left_GreaterThan_right(arr[i], arr[i + 1]) :
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

#O(n)
def selection_sort(arr,left_GreaterThan_right=lambda a, b: a > b) :
    """
    for each index but the last, find the smallest element in the
    right subarray and swap it with its leftmost element, the current min

    """
    for i in range(len(arr)) :
        for j in range(i + 1, len(arr)) :
            if left_GreaterThan_right(arr[i], arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

#O(n) but fast if mostly sorted
def insertion_sort(arr,left_GreaterThan_right=lambda a, b: a > b) :
    """
    like selection sort, create a left sorted partition of smaller
    elements but by only selecting the next element and bubbling left until no longer smaller

    """
    for i_after_sorted in range(1, len(arr)) :
        j = i_after_sorted
        while j > 0 and left_GreaterThan_right(arr[j - 1], arr[j]) :
            arr[j - 1], arr[j] = arr[j], arr[j - 1] 
            j-= 1

def quick_sort(arr, left_GreaterThan_right=lambda a, b: a > b) :
    """
    quick_sort is a wrapper to sort
    recursively select a pivot a move all larger elements to the right of 
    it and smaller to the left. Recurse on left and right subarrays
    """
    def sort(low, high) :
        if low < high :
            pivot, divider = arr[high], low
            #partition
            for i in range(low, high) :
                if left_GreaterThan_right(pivot , arr[i]):
                    arr[i], arr[divider] = arr[divider], arr[i]
                    divider += 1
            arr[high], arr[divider] = arr[divider], arr[high]
            #sort subarrays
            sort(low, divider - 1)
            sort(divider + 1, high)

    sort(0, len(arr) - 1)


def merge_sort(arr, left_GreaterThan_right=lambda a, b: a > b) :
    """
    recursively split array into two subarrays, sort them
    and combine parts
    """
    if len(arr) <= 1 :  
        return

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left, left_GreaterThan_right)
    merge_sort(right, left_GreaterThan_right)

    #Now, merge
    i = l = r = 0

    while l < len(left) or r < len(right) :
        if  l >= len(left) :
            arr[i] = right[r]
            r += 1
        elif r >= len(right) :
            arr[i] = left[l]
            l += 1
        elif left_GreaterThan_right(right[r], left[l]) :
            arr[i] = left[l]
            l += 1
        else :
            arr[i] = right[r]
            r += 1
        i += 1
            


    
