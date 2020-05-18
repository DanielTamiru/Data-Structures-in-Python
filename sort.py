# /**
#  File: sort.c
#     check sort.h for details
# */

# #include <stdio.h>
# #include <assert.h>
# #include <limits.h>

# static void swap(int *p1, int *p2) {
#     int temp = *p1;
#     *p1 = *p2;
#     *p2 = temp;
# }

# void bubble_sort(int a[], const int len) {
#     for(int upper = len - 1; upper >= 0; upper--) {
#         for(int i = 0; i < upper; i++) {
#             if (a[i] > a[i + 1]) {
#                 swap(&a[i], &a[i + 1]);
#             }
#         }  
#     }  
# }

# void selection_sort(int a[], const int len) {  
#     for (int lower = 0; lower < len - 1; lower++) {
#         int min_pos = lower;
#         for(int i = lower + 1; i < len; i++) {
#             if (a[i] < a[min_pos]) {
#                 min_pos = i;
#             } 
#         }
#         swap(&a[min_pos], &a[lower]);
#     }
# }

# //my implementation. Not bad but could be a lot more concise
# void my_insertion_sort(int a[], const int len) {
#     int sorted = 0;//right-most index of sorted left-partition 
#     for(int i = 1; i < len; i++){
#         if (a[i] < a[sorted]) {
#             swap(&a[i], &a[sorted]);//put breaking conditions in loop cond
#             for(int p = sorted - 1; p >= 0 && a[p] > a[p + 1] ; p--) {
#                 swap(&a[p], &a[p + 1]);
#             }
#         }
#         sorted++;
#     }  
# }

# //CS136's implementation. They don't have a 'sorted' index tracker.
# //It just starts at 1 and continuously checks at indexes below from the start
# void insertion_sort(int a[], int len) { 
#     for (int i = 1; i < len; ++i) {
#         for (int j = i; j > 0 && a[j - 1] > a[j]; --j) { 
#             swap(&a[j], &a[j - 1]);
#         } 
#     }
# }


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
