#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

// 'a' == 97

int main()
{
	const char* pattern = "abba";
	const char* string = "dog cat cat dog";

	size_t string_sz = sizeof(char) * (strlen(string) + 1);
	char* p_buff = malloc(string_sz);
	assert(p_buff);
	strncpy(p_buff, string, string_sz);

	int match = 0;

	const char* ht[26] = {NULL};
	int ht_idx = -1;

	printf("match pattern : %s\n", pattern);
	printf("match string  : %s\n", string);
	printf("\n");

	const char* token = strtok(p_buff, " ");
	size_t i = 0;
    	for (; i < strlen(pattern); i++) {
		printf("processing \"%s\"...\n", token);

		ht_idx = pattern[i] - 'a';
		if (ht[ht_idx] == NULL) {
			printf("storing \"%s\" in ht[%d]...\n", token, ht_idx);
			ht[ht_idx] = token;
		} else if (strcmp(ht[ht_idx], token) != 0) {
			printf("ht[%d] != \"%s\"\n", ht_idx, token);
			goto early_exit;
		}

		token = strtok(NULL, " ");
	}
	if (!token) {
		match = 1;
	}

early_exit:
	printf("%s\n", match ? "True" : "False");
	return 0;
}

