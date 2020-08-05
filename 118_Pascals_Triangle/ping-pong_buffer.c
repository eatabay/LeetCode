#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
	int row_idx = atoi(argv[1]);

	int bufferA[34] = {1, 0},
	    bufferB[34] = {1, 0};

	/*
	 * These will ping-pong between bufferA & bufferB, with
	 * one buffer thereby serving as the "previous row" at 
	 * any given time.
	 */
	int* curr_row_p = bufferA;
	int* prev_row_p = bufferB;

	int row = 1, col = 0;
	for (; row <= row_idx; row++) {
		prev_row_p = curr_row_p;
		curr_row_p = (curr_row_p == bufferA) ? bufferB : bufferA;
		for (col = 1; col <= row_idx; col++) {
			curr_row_p[col] = prev_row_p[col-1] + prev_row_p[col];
		}
	}

	for (col = 0; col <= row_idx; col++) {
		printf("%d ", curr_row_p[col]);
	}
	printf("\n");

	return 0;
}

