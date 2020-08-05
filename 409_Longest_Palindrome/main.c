/*
 * Considerations:
 * - 'Pairs' of letters are required for viable palindromes.
 * - Any one (1) single letter may be placed in the middle
 *   lengthen the palindrome by 1 - once.
 */

/*
 * My approach:
 * 1. Create map/hash table of letters (case sensitive)
 *    - the keys - to instances of that latter - the values.
 * 2. Determine sum of letter-pairs in map.
 * 3. Add "1" if any letter exists without a pair.
 */

/* 
 * Regarding hashing function - per ASCII:
 * - 'A' - 'Z' == 65 -  90 (respectively)
 * - 'a' - 'z' == 97 - 122 (respectively)
 */

#include <stdio.h>
#include <assert.h>

/* Hash function. */
int key_to_hash_idx(char hash_key)
{
	return (hash_key < 'a') ? (hash_key - 'A') : (hash_key - 'a' + 26);
}

char hash_idx_to_key(int hash_idx)
{
	return (hash_idx < 26) ? (hash_idx + 'A') : (hash_idx - 26 + 'a');
}

void print_table(int* hash_table, int hash_table_n)
{
	assert(hash_table && hash_table_n);

	int i = 0;
	for (; i < hash_table_n; i++) {
		printf("%c : %d\n", hash_idx_to_key(i), hash_table[i]);
	}
	
	return;
}

int main(int argc, char* argv[])
{
	printf("Input string: %s\n", argv[1]);

	/*
	 * Build hash table.
	 * We are able to map keys to array indexes in this case; so,
	 * we don't need a special-purpose data structure.
	 */
	int hash_table[52] = {0};  // All counts are initialized to "0".

	/* Populate hash table. */
	char* key_p = argv[1];
	while ((*key_p) != '\0') {
		hash_table[key_to_hash_idx((*key_p++))]++;
	}

	print_table(hash_table, 52);

	/* Count pairs and such. */
	int add_one = 0;
	int palindrome_len = 0;
	int i = 0;
	for (; i < 52; i++) {
		if (hash_table[i] == 0) { continue; }
		if (hash_table[i] % 2) {
			palindrome_len += (hash_table[i]-1);
			add_one = 1;
		} else {
			palindrome_len += hash_table[i];
		}
	}

	printf("Longest palindrome: %d\n", palindrome_len + add_one);

	return 0;
}

