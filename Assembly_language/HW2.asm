 INCLUDE Irvine32.inc
.data
	start = 1
	chars BYTE 'H','A','C','E','B','D','F','G'
	links DWORD 0,4,5,6,2,3,7,0
	copy_arr BYTE LENGTHOF chars DUP('#'),0
	question BYTE "Question",0
	tab BYTE " ",0
	letter BYTE "A",0
.code
main PROC
;Q2
	mov edx,OFFSET question
	call WriteString
	mov eax,2
	call WriteDec
	call crlf

	mov ecx, LENGTHOF chars
	mov eax,0
	mov ebx,0
	mov al,start
	mov edx,0
	mov dh,4
	L1:
		mov dl,chars[eax]
		mov copy_arr[ebx],dl
		inc ebx 
		mul dh
		mov eax,links[eax]
		loop L1
	mov edx,OFFSET copy_arr
	call WriteString
	call crlf
	call crlf

;Q5
	mov edx,OFFSET question
	call WriteString
	mov eax,5
	call WriteDec
	call crlf

	mov ecx,50
	call Randomize
	L2:
		
		mov ebx,-300
		mov  eax,100
		sub eax,ebx
		call RandomRange
		add eax,ebx
		call writeint
		call crlf
		loop L2
	call crlf

;Q7
	mov edx,OFFSET question
	call WriteString
	mov eax,7
	call WriteDec
	call crlf

	mov esi,0
	mov ebx,0
	L3:
		call GetMaxXY
		movzx eax,dl
		dec eax
		call RandomRange
		mov ecx,eax
		inc ecx
		L4:
			
			mov edx,OFFSET tab
			call WriteString
			inc ebx
			loop L4
		
		cmp esi,100
		je L6
		mov edx,OFFSET letter
		call WriteString
		inc esi
	jmp L3
	L6:
		call crlf
		call   waitmsg
		exit
main ENDP
END main
