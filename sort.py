
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
        while j > 0 and arr[j - 1] > arr[j] :
            arr[j - 1], arr[j] = arr[j], arr[j - 1] 
            j-= 1


# static int *select_pivot(int *s, int *m, int *e) {
#     if((*s <= *m && *s >= *e) || (*s >= *m && *s <= *e)) {
#         return s;
#     }
#     else if ((*m <= *s && *m >= *e) || (*m >= *s && *m <= *e)){
#         return m;
#     }
#     else {
#         return e;
#     }      
# }
# //you learned a valuable lesson with quicksort. Never think published info is
# //not the most efficient and concise without mathematically checking your method
# void quicksort(int *arr, int len) {
#     assert(arr);  
#     if (len == 0){
#         return; 
#     }
#     int *pivot = select_pivot(arr, arr + len/2, arr + len - 1);
#     int *boarder = arr + len - 1;

#     for (int *i = arr + len - 1; i >= arr; i--) {
#         if (*i > *pivot) {
#             swap(i, boarder);
#             //if you happen to move the pivot around, make sure to track it
#             if(pivot == i) {
#                 pivot = boarder;
#             }
#             if(pivot == boarder) {
#                 pivot = i;
#             }
#             boarder--;
#         }
#     }

#     swap(pivot, boarder);
#     quicksort(arr, boarder - arr);
#     quicksort(boarder + 1, (arr + len) - (boarder + 1));
# }

insertion_sort(list3)
print(list3)    


# //O(n) helper funciton for mergesort
# //requires: arrays a and b are adjacent in memory and they are sorted
# static void merge(int a[], int a_len, int b[], int b_len) {
#     //assert(a + a_len == b);
#     int a_i = 0; // initial a->data index
#     int b_i = 0; // initial b->data index

#     int merged[1000];
#     int merged_len = 0;

#     while(a_i < a_len && b_i < b_len) {
#         //WLOG, set set a as pace setter
#         if (a[a_i] >= b[b_i]){
#             merged[merged_len] = b[b_i];
#             merged_len++;
#             if (a[a_i] == b[b_i]) {
#                 a_i++;
#                 merged[merged_len] = b[b_i];
#                 merged_len++;
#             }
#             b_i++;
#         }
#         else {
#             merged[merged_len] = a[a_i];
#             merged_len++;
#             a_i++;
#         } 
#     }  
#     //now append rest of longer set 
#     while (a_i < a_len) {
#         merged[merged_len] = a[a_i];
#         merged_len++;
#         a_i++;
#     }
#     while (b_i < b_len) {
#         merged[merged_len] = b[b_i];
#         merged_len++;
#         b_i++;
#     }     
#     //finally, overwrite a and b with the temporary array
#     for(int i = 0; i < a_len + b_len; i++) {
#         if (i < a_len) {
#             a[i] = merged[i];
#         }
#         else {
#             b[i - a_len] = merged[i];
#         }
#     }
# }
# //n log n   
# void mergesort(int a[], const int len) {
#     if (len == 1) {
#         return;
#     }
#     int *middle = a + len/2;
    
#     mergesort(a, middle - a);
#     mergesort(middle, (a + len) - middle);
    
#     merge(a, middle - a, middle, (a + len) - middle);
# }
