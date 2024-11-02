; Yourname Here
.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

include C:\Irvine\Irvine32.inc  ; Irvine location

.data
msgInput db "Enter your marks: ", 0  ; Message to prompt user for input
msgOutput db "Updated marks: ", 0    ; Message to display updated marks
marks dd ?                           ; Variable to store user input marks
updatedMarks dd ?                    ; Variable to store updated marks

.code
main PROC
    ; Print the input prompt message
    call Clrscr
    mov edx, OFFSET msgInput
    call WriteString

    ; Read user input into the 'marks' variable
    call ReadInt
    mov marks, eax

    ; Move the input marks into the EAX register
    mov eax, marks

    ; Add 5 to the value in EAX
    add eax, 5

    ; Store the updated marks back into the 'updatedMarks' variable
    mov updatedMarks, eax

    ; Print the output prompt message
    mov edx, OFFSET msgOutput
    call WriteString

    ; Print the updated marks
    mov eax, updatedMarks
    call WriteInt

    ; Exit the program
    invoke ExitProcess, 0
main ENDP
END main