#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target)
{
	/* Use HT to store number indeces. */
	size_t ht_sz = numsSize * sizeof(int);
	int* ht_p = malloc(ht_sz);

	/* HF() is just (number % HT size). */
	int i = 0;
	for (; i < numsSize; i++) {
		ht_p[nums[i] % numsSize] = i;
	}

	int complement = 0;
	for (i = 0; i < numsSize; i++) {
		complement = target - nums[i];
		if (ht_p[complement % numsSize] != 

}

int main()
{
	int nums[] = {3,2,4};
	int target = 6;

	int nums_n = sizeof(nums)/sizeof(nums[0]);
	int* p_result = twoSum(nums, nums_n, target);

	printf("\n[%d, %d]\n", p_result[0], p_result[1]);

	return 0;
}
