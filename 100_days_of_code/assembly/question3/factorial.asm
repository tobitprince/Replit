section .text
    global _FactorialDiff    ; Export for C calling

_FactorialDiff:
    push ebp
    mov ebp, esp

    ; Get parameters a and b
    mov ecx, [ebp + 8]    ; a
    mov edx, [ebp + 12]   ; b

    ; Calculate a!
    push ecx
    call calculate_factorial
    add esp, 4
    mov ebx, eax          ; Store a! in ebx

    ; Calculate b!
    push edx
    call calculate_factorial
    add esp, 4

    ; Calculate a! - b!
    sub ebx, eax
    mov eax, ebx          ; Return result in eax

    pop ebp
    ret

calculate_factorial:
    push ebp
    mov ebp, esp

    mov ecx, [ebp + 8]    ; Get number
    mov eax, 1            ; Initialize result

factorial_loop:
    test ecx, ecx         ; Check if counter is 0
    jz factorial_done     ; If zero, we're done

    mul ecx               ; Multiply result by counter
    dec ecx              ; Decrease counter
    jmp factorial_loop

factorial_done:
    pop ebp
    ret