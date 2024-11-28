section .text
    global _Convert76_0625    ; Windows CDECL convention needs underscore

_Convert76_0625:
    push ebp
    mov ebp, esp

    ; Get pointer to store result
    mov edi, [ebp + 8]

    ; Load the pre-computed IEEE value for -76.0625
    mov eax, 0xC2980100

    ; Store the result
    mov [edi], eax

    pop ebp
    ret