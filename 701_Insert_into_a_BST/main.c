/*
 * Insert new node into BST.
 * (Original problem statement does not mention
 * requirement to keep tree balanced.)
 */

#include <stdio.h>
#include <assert.h>

typedef struct tree_s {
	int key;
	struct tree_s* left_p;
	struct tree_s* right_p;
} tree_t;

void bst_insert(tree_t** root_pp, tree_t* node_p)
{
	assert(root_pp && node_p);

#if 1    // Recursive.
	tree_t* this_node_p = (*root_pp);
	if (this_node_p == NULL) {  /* New node is root of tree. */
		(*root_pp) = node_p;
	} else if (this_node_p->key <= node_p->key) {
		bst_insert(&(this_node_p->left_p), node_p);
	} else {
		bst_insert(&(this_node_p->right_p), node_p);
	}

	return;
#else    // Iterative.
#endif
}

