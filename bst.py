# /////////////////////////////////////////////////////////////////////////////
# // INTEGRITY INSTRUCTIONS (v2)

# // Explicitly state the level of collaboration on this question
# // Examples:
# //   * I discussed ideas with classmate(s) [include name(s)]
# //   * I worked together with classmate(s) in the lab [include name(s)]
# //   * Classmate [include name] helped me debug my code
# //   * I consulted website [include url]
# //   * None
# //
# // A "None" indicates you completed this question entirely by yourself
# // (or with assistance from course staff, which you do not have to mention)
# /////////////////////////////////////////////////////////////////////////////
# // INTEGRITY STATEMENT:
# // I received help from and/or collaborated with:

# // None

# // Name: Daniel Tamiru
# // login ID: dtamiru
# ///////////////////////////////////////////////////////////////////////////
# #include <assert.h>
# #include <stdlib.h>
# #include <stdio.h>
# #include "bst.h"
# #include "pow2.h"

# ///////////////////////////////////////
# // The following functions have been
# // provided for your convenience
# // 
# // You will have to MODIFY them
# ///////////////////////////////////////

# struct bst *bst_create_empty(void) {
#     struct bst *tree = malloc(sizeof(struct bst));
#     tree->root = NULL;
#     return tree;
# }

# static struct bstnode *new_leaf(int i) {
#     struct bstnode *leaf = malloc(sizeof(struct bstnode));
#     leaf->item = i;
#     leaf->count = 1;
#     leaf->left = NULL;
#     leaf->right = NULL;
#     return leaf;
# }

# bool bst_contains(int i, const struct bst *tree) {
#     assert(tree);
#     struct bstnode *node = tree->root;
#     while (node) {
#         if (node->item == i) {
#             return true;
#         }
#         if (i < node->item) {
#             node = node->left;
#         } else {
#             node = node->right;
#         }
#     }
#     return false;
# }

# void bst_insert(int i, struct bst *tree) {
#     assert(tree);
#     struct bstnode *node = tree->root;
#     struct bstnode *parent = NULL;
#     if (bst_contains(i, tree)) {
#         return;
#     }
#     while (node) {
#         if (node->item == i) {
#             return;
#         }
#         parent = node;
#         parent->count++;
#         if (i < node->item) {
#             node = node->left;
#         } else {
#             node = node->right;
#         }
#     }
#     if (parent == NULL) {// tree was empty
#         tree->root = new_leaf(i);
#     } else if (i < parent->item) {
#         parent->left = new_leaf(i);
#     } else {
#         parent->right = new_leaf(i);
#     }
# }

# static struct bstnode *remove_bstnode(int i, struct bstnode *node) {
#     // key did not exist:
#     if (node == NULL) return NULL;
    
#     // search for the node that contains the key
#     if (i < node->item) {
#         node->count--;
#         node->left = remove_bstnode(i, node->left);
#     } else if (i > node->item) {
#         node->count--;
#         node->right = remove_bstnode(i, node->right);
#     } else if (node->left == NULL) {//found it.
#         struct bstnode *new_root = node->right;
#         free(node);
#         return new_root;//promote right if left NULL (both NULL accounted for)
#     } else if (node->right == NULL) {
#         struct bstnode *new_root = node->left;
#         free(node);
#         return new_root;//promote left if right NULL
#     } else {
#         // find next largest key and its parent
#         struct bstnode *next = node->right;
#         struct bstnode *parent_of_next = NULL;
#         while (next->left) {
#             next->count--;
#             parent_of_next = next;
#             next = next->left;
#         }
#         // free old value & replace key/value of this node
#         node->item = next->item;
#         node->count--;
#         // remove next largest node
#         if (parent_of_next) {
#             parent_of_next->left = next->right;
#         } else {
#             node->right = next->right;
#         }
#         free(next);
#     }
#     return node;
# }
# void bst_remove(int i, struct bst *tree) {
#     assert(tree);
#     if (!bst_contains(i, tree)) {
#         return;
#     }
#     tree->root = remove_bstnode(i, tree->root);
# }


# static int select_node(int k, struct bstnode *node) {
#     assert(node && 0 <= k && k < node->count);
#     int left_count = 0;
#     if (node->left) {
#         left_count = node->left->count;
#     }
#     if (k < left_count) {
#         return select_node(k, node->left);
#     }
#     if (k == left_count) {
#         return node->item;
#     }
#     return select_node(k - left_count - 1, node->right);
# }
# int bst_select(int k, struct bst *tree) {
#     assert(tree);
#     return select_node(k, tree->root);
# }

# static void free_bstnode(struct bstnode *node) {
#     if (node) {
#         free_bstnode(node->left);
#         free_bstnode(node->right);
#         free(node);
#     }
# }
# void bst_destroy(struct bst *tree) {
#     assert(tree);
#     free_bstnode(tree->root);
#     free(tree);
# }

# ///////////////////////////////////////
# // The following functions are
# // for you to implement:
# // (only critical documentation shown)
# ///////////////////////////////////////


# // node_to_sorted_array(arr, length, root) inserts a value from a bstnode 
# // into a sorted array arr at position length recursively, ultimately filling 
# // the arr with the contents in root in increasing order
# // effects: modifies arr
# // requires: a is valid (non-null), (running) length is non-negative        
# // time: O(n)
# static void node_to_sorted_array(int *arr, int *length, 
#                                  const struct bstnode *root) {
#     assert(*length >= 0);
#     assert(arr);
    
#     if (!root) {//dead-end
#         return;
#     } else if (!root->left && !root->right) {
#         arr[*length] = root->item; //insert
#         (*length)++;
#         return;
#     }
#     node_to_sorted_array(arr, length, root->left);
#     arr[*length] = root->item; 
#     (*length)++;
#     node_to_sorted_array(arr, length, root->right); 
# }

# int *bst_to_sorted_array(const struct bst *tree, int *len) {
#     assert(tree);
#     if (!tree->root) {
#         *len = 0;
#         return NULL;
#     } else {
#         int running_length = 0; 
#         int *l = &running_length; //length pointer that will increment in helper
#         *len = tree->root->count; //modify len
#         int *sorted_arr = malloc((*len) * sizeof(int));//client free 
#         node_to_sorted_array(sorted_arr, l, tree->root);
#         return sorted_arr;
#     } 
# }


# // node_create_balanceda, len) creates a tree of bstnodes from a subarray
# // of sorted array a, the first index of which being front and back being one 
# // more than the last index, such that the tree of bstnodes is balanced
# // effects: modifies node   
# //          allocates memory
# // requires: a is valid (not null), a's length is positive, and a is sorted
# //           0 <= font <= back <= a's length
# // time: O(n)
# static struct bstnode *node_create_balanced(struct bstnode *node, const int *a, 
#                                      const int front, const int back) {
#     assert(a);
#     assert(front >= 0);
#     assert(back >= front);
    
#     if (front == back) {
#         return node;
#     }
#     int middle = (front + back)/2;
#     node = new_leaf(a[middle]);
#     node->count = back - front;
#     //recurse on left and right children
#     node->left = node_create_balanced(node->left, a, front, middle);
#     node->right = node_create_balanced(node->right, a, ++middle, back);
#     return node;
# }

# struct bst *bst_create_balanced(int a[], int len) {
#     assert(a);
#     assert(len > 0);
#     struct bst *balanced = bst_create_empty();
#     balanced->root = node_create_balanced(balanced->root, a, 0, len);
#     return balanced;
# }



# void bst_insert_rebalance(int i, struct bst *tree) {
#     //Regular insert with slight changes:
#     assert(tree);
#     if (bst_contains(i, tree)) {
#         return;
#     }
#     int depth = 1;
#     struct bstnode *node = tree->root;
#     struct bstnode *parent = NULL;
#     while (node) {
#         if (node->item == i) {
#             return;
#         }
#         parent = node;
#         parent->count++;
#         if (i < node->item) {
#             node = node->left;
#         } else {
#             node = node->right;
#         }
#         depth++;//increment depth
#     }
#     if (parent == NULL) {  // tree was empty
#         tree->root = new_leaf(i);
#     } else if (i < parent->item) {
#         parent->left = new_leaf(i);
#     } else {
#         parent->right = new_leaf(i);
#     }
#     // Note: min_height(count) = log2ceil(count + 1), max_height(count) = count
#     int count = tree->root->count;
#     int min_height = log2ceil(count + 1);
#     if (depth > 2 * min_height) {
#         int length = 0;
#         int *arr_len = &length;
#         int *arr = bst_to_sorted_array(tree, arr_len);
#         struct bstnode *old_root = tree->root;
#         tree->root = node_create_balanced(tree->root, arr, 0, length);
#         free_bstnode(old_root);
#         free(arr);
#     }
# }



# // bst_create_compact(node, a, first, last) creates a tree of bstnodes 
# // from a subarray of sorted array a, starting at index first
# // and ending at index last, such that it is a complete tree. 
# // effects: modifies node
# //          allocates memory
# // requires: a is valid (not null), a's length is positive, and a is sorted
# //           0 <= first <= last < length of a
# // time: O(n)
# static struct bstnode *node_create_compact(struct bstnode *node, const int a[], 
#                                      const int first, const int last) {
#     assert(a);
#     assert(first >= 0);
#     assert(last >= first);
#     int length = last - first + 1;//length of subarray
    
#     if (length == 1) {//Base case 1: single node
#         node = new_leaf(a[first]);
#         return node;
#     } else if (length == 2) {//Base case 2: node pair
#         node = new_leaf(a[last]);
#         node->count = 2;
#         node->left = node_create_compact(node->left, a, first, first);
#         return node;
        
#     } else {//subarray longer than two
#         int max_middle = pow2(log2floor(length)) - 1;
#         int middle = length - max_middle - 1;
#         middle += pow2(log2floor(length) - 1);
#         if (max_middle < middle) {
#             middle = max_middle;
#         }
#         middle += first;
#         node = new_leaf(a[middle]);
#         node->count = length;
#         //recurse on left and right children
#         node->left = node_create_compact(node->left, a, first, middle - 1);
#         node->right = node_create_compact(node->right, a, middle + 1, last);
#         return node;
#     }
# }

# void bst_compact(struct bst *tree) {
#     assert(tree);
#     if (!tree->root) {
#         return;
#     }
#     int len = 0;
#     int *arr_len = &len;
#     int *arr = bst_to_sorted_array(tree, arr_len);//make sorted array from bst
#     struct bstnode *old_root = tree->root;
#     //change nodes of current bst to compact tree 
#     int last = len - 1;
#     tree->root = node_create_compact(tree->root, arr, 0, last);
#     //free old nodes
#     free_bstnode(old_root);
#     free(arr);
# }

