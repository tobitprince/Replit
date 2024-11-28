section .text
    global _MultiplyUnsigned    ; Add underscore for Windows CDECL

; void MultiplyUnsigned(uint32_t multiplicand, uint32_t multiplier, uint64_t* product)
_MultiplyUnsigned:              ; Add underscore here too
    ; Prologue
    push ebp
    mov ebp, esp

    ; Retrieve arguments from the stack
    mov eax, [ebp + 8]      ; multiplicand
    mov ebx, [ebp + 12]     ; multiplier
    mov edi, [ebp + 16]     ; product pointer

    ; Multiply
    mul ebx                 ; EDX:EAX = EAX * EBX

    ; Store the result
    mov [edi], eax          ; lower 32 bits
    mov [edi + 4], edx      ; higher 32 bits

    ; Epilogue
    mov esp, ebp
    pop ebp
    ret