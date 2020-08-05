#include <stdio.h>

int main()
{
	int pt[34][34] = {0};

	pt[0][0] = 1;
	int row = 1, col = 0;

	for (; row < 34; row++) {
		for (col = 0; col < row; col++) {
			if ((col == 0) || (col == row)) {
				pt[row][col] = 1;
			} else {
				pt[row][col] = pt[row-1][col-1] + pt[row-1][col];
			}
			printf("%d ", pt[row][col]);
		}
		printf("\n");
	}

	return 0;
}
