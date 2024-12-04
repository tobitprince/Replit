section .data
    message db 'The factorial of 5 is: ', 0  ; The message to print before the result
    newline db 0x0A  ; Newline character for formatting

section .bss
    buffer resb 16  ; Buffer to store the number as a string

section .text
    global _start

_start:
    ; Print the message "The factorial of 5 is: "
    mov eax, 4                ; syscall number for sys_write
    mov ebx, 1                ; file descriptor (1 = stdout)
    lea ecx, [message]        ; load address of message
    mov edx, 23               ; length of the message string
    int 0x80                  ; Make the syscall to write to stdout

    ; Calculate the factorial of 5 (5! = 120)
    mov eax, 5
    call factorial
    ; The result (120) is now stored in eax

    ; Convert the result (eax) to a string
    lea edi, [buffer + 15]    ; Point to the end of the buffer
    mov byte [edi], 0x0A      ; Add a newline character at the end

    ; Call the conversion logic to convert the number in eax to string
    call convert

    ; Write the result to the console
    mov eax, 4                ; syscall number for sys_write
    mov ebx, 1                ; file descriptor (1 = stdout)
    lea ecx, [edi]            ; pointer to the string to be printed
    lea edx, [buffer + 16]    ; buffer length (16 bytes)
    sub edx, ecx              ; calculate length by subtracting addresses
    int 0x80                  ; Make the syscall to write to stdout

    ; Exit the program
    mov eax, 1                ; syscall number for sys_exit
    xor ebx, ebx              ; exit status 0
    int 0x80                  ; Make the syscall to exit

; Factorial function using recursion
factorial:
    cmp eax, 1                ; Check if eax is 1 (base case)
    jz end_recursion          ; If eax == 1, jump to the end

    ; Save the current value of eax
    push eax

    ; Decrement eax and call factorial recursively
    dec eax
    call factorial

    ; Multiply the result returned in eax with the saved value of eax
    pop ebx
    imul eax, ebx             ; eax = eax * ebx

    ret

end_recursion:
    mov eax, 1                ; Return 1 when eax is 1 (base case)
    ret

; Conversion of eax to string (ASCII digits)
convert:
    dec edi                   ; Move buffer pointer backwards
    xor edx, edx              ; Clear edx for division
    mov ecx, 10               ; Base 10 for division
    div ecx                   ; Divide eax by 10, result in eax, remainder in edx
    add dl, '0'               ; Convert remainder to ASCII character
    mov [edi], dl             ; Store ASCII character in buffer
    test eax, eax             ; Check if eax is zero
    jnz convert               ; If eax is not zero, continue converting
    ret
