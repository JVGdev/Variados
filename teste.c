#include <stdio.h>

struct node {
	struct node* left;
	int val;
	struct node* right;
};


int main(){
	struct node a;
	struct node b;
	struct node c;

	a.val = 3;
	a.left = &b;
	a.right = &c;
	
	a.left->val = 6;
	
	printf("%d\n", a.left->val);	

	return 0;
}
