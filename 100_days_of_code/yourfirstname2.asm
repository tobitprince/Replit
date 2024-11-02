; Yourname Here
.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

include C:\Irvine\Irvine32.inc  ; Irvine location

.data
MTGrade word 54h          ; Midterm grade 84(decimal)
finalGrade word 37h       ; Final grade 55(decimal)
msg1 db "Total is ", 0    ; Message to display before total grade
totalGrade word ?         ; Variable to store the total grade 84 + 55= 139

.code
main PROC
    ; Move the value of MTGrade into the AX register
    mov ax, MTGrade

    ; Add the value of finalGrade to AX
    add ax, finalGrade

    ; Store the result (total grade) into the 'totalGrade' variable
    mov totalGrade, ax

    ; Print the message "Total is "
    mov edx, OFFSET msg1
    call WriteString

    ; Print the total grade
    movzx eax, totalGrade  ; Zero-extend the 16-bit totalGrade to 32-bit EAX
    call WriteInt

    ; Exit the program
    invoke ExitProcess, 0
main ENDP
END main