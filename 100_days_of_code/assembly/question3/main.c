#include <stdio.h>
#include "factorial.h"

int main() {
    int a = 5;
    int b = 3;

    int result = FactorialDiff(a, b);
    printf("%d! - %d! = %d\n", a, b, result);

    return 0;
}