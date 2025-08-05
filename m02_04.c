#include <stdio.h>

int sum(int a, int b) {
    return (a + b);
}

int main(void) {
	int a = 0;
	int b = 5;

	if (a > b) {
		puts("a is greater than b");
	} else {
		puts("a is not greater than b");
	}

    a = sum(3, 3);
}