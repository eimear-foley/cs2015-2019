mov dl, 0   ;move 0 in to the dl register this will represent the number
            ;of items to to be checked

input:  
    in 00   ;keyboard input

    cmp al, 2e        ;if full stop, then we have reached end of string
    jz is_palindrome  ;go check if palindrome
    


    push al  ;push character onto stack
    inc dl   ;gives us the number of items to be compared
jmp input    ;get more keyboard input until full stop given

is_palindrome:  ;checks if palindrome or not
    mov cl, bf  ;move the start of the stack pointer into cl register
        
    move_stack: 
        mov bl, [cl]  ;move the value of the start of the stack pointer to bl
        pop al        ;pop value of item at the end of the stack
        sub dl, 2     ;comparing two items so decrement number of items 
                      ;to be checked by 2
        cmp al, bl    ;compare end and start of stack
        jnz no        ;if not equal, Z Flag is not set, jump to no
        dec cl        ;decrement cl to move along the stack i.e. bf to be
        cmp dl, 2     ;compare number of items to be checked to 2
        js yes        ;if the S Flag is set then dl is less than 2 there are 0
                      ;0 items to be checked or 1 item left i.e. the b in "aba" 
                      ;hence jump to yes
    jmp move_stack    ;else jump back to move_stack

no:               ;prints 'n' to the VDU
    mov cl, 6e
    mov [c0], cl
jmp clear     

yes:              ;prints 'y' to the VDU
    mov cl, 79
    mov [c0], cl
jmp clear

clear:
mov dl, 0
mov cl, bf
mov bl, [cl]
pop al
cmp bl, 00
jz input
jmp clear

end   
