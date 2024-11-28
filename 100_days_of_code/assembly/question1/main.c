#include <stdio.h>
#include <stdint.h>

// Declaration of the assembly subroutine
void MultiplyUnsigned(uint32_t multiplicand, uint32_t multiplier, uint64_t* product);

int main() {
    uint32_t a = 12345;
    uint32_t b = 6789;
    uint64_t result = 0;

    MultiplyUnsigned(a, b, &result);

    printf("Product = %llu\n", result);
    return 0;
}