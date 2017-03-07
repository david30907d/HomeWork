 INCLUDE Irvine32.inc
.data
 bigEndian   BYTE 12h, 34h, 56h, 78h
 littleEndian DWORD ?
 arr BYTE 98h,88h,12h,37h
 arr2 BYTE 0,2,5,9,10
 source BYTE "This is the source string",0
 target BYTE SIZEOF source DUP('#')
 arr3 BYTE 10h,20h,30h,40h 
 question BYTE "Question",0

.code
main PROC
;Q1
	mov edx,OFFSET question
	call WriteString
	mov eax,1
	call WriteDec
	call crlf
	mov eax,0
	mov ebx,0
	mov al,BYTE PTR bigEndian+0
	mov bl,BYTE PTR bigEndian+1
	mov cl,BYTE PTR bigEndian+2
	mov dl,BYTE PTR bigEndian+3

	mov BYTE PTR littleEndian+0,dl
	mov BYTE PTR littleEndian+1,cl
	mov BYTE PTR littleEndian+2,bl
	mov BYTE PTR littleEndian+3,al
	mov eax,littleEndian
	call WriteHex 
	call crlf

;Q2
	mov edx,OFFSET question
	call WriteString
	mov eax,2
	call WriteDec
	call crlf
	mov esi,0
	mov ecx, LENGTHOF arr
	mov edx,0
	mov ebx,0
	L1:
		mov bl,BYTE PTR arr[esi]
		mov bh,BYTE PTR arr[esi+1]
		mov BYTE PTR arr[esi],bh
		mov BYTE PTR arr[esi+1],bl
		mov eax,DWORD PTR arr
		add esi,2
		sub ecx,1
		loop L1
	mov esi,0
	mov ecx, LENGTHOF arr
	mov eax,0
	print:
			movzx eax,BYTE PTR arr[esi]
			call WriteHex
			call crlf
			add esi,1
			loop print        
	call crlf
;Q3
	mov edx,OFFSET question
	call WriteString
	mov eax,3
	call WriteDec
	call crlf

	mov ecx, LENGTHOF arr2
	sub ecx ,1
	mov ebx,0
	L2:
		mov bl ,BYTE PTR arr2[ecx]
		sub bl,arr2[ecx-1]
		add bh,bl
		loop L2
	movzx  eax,bh
	call WriteHex
	call crlf
	call crlf

;Q5
	mov edx,OFFSET question
	call WriteString
	mov eax,5
	call WriteDec
	call crlf

	mov ecx,5
	mov edx,0
	mov dl,1
	mov dh,1
	mov ebx,0
	movzx  eax,dl
	call WriteHex
	call crlf
	movzx  eax,dh
	call WriteHex
	call crlf
	L3:
		mov bl,dl
		add bl,dh
		movzx  eax,bl
		call WriteHex
		call crlf
		mov dl,dh
		mov dh,bl
		loop L3
	call crlf

;Q7
	mov edx,OFFSET question
	call WriteString
	mov eax,7
	call WriteDec
	call crlf
	call crlf

	mov ebx,0
	mov ecx, LENGTHOF source
	sub ecx ,2
	mov eax,0
	L4:
		mov bl,BYTE PTR source[eax]
		mov BYTE PTR target[ecx],bl
		add eax,1
		loop L4
	mov ecx, LENGTHOF source
	mov bl,BYTE PTR source[ecx-2]
	mov BYTE PTR target[0],bl
	mov BYTE PTR target[ecx-1] ,0
	mov edx,OFFSET target
	call WriteString
	call crlf
	call crlf

;Q8
	mov edx,OFFSET question
	call WriteString
	mov eax,8
	call WriteDec
	call crlf
	call crlf

	mov ebx,0
	mov ecx, LENGTHOF arr3
	sub ecx ,1
	mov edx,0
	mov dl ,BYTE PTR arr3[ebx]
	add ebx,1
	L5:
		mov dh ,dl
		mov dl ,BYTE PTR arr3[ebx]
		mov BYTE PTR arr3[ebx],dh
		add ebx,1
		loop L5
	mov BYTE PTR arr3[0],dl
	mov  eax,0
	mov  eax,DWORD PTR arr3
	mov  esi, OFFSET arr3 	; starting OFFSET
	mov  ecx, LENGTHOF arr3 	; number of units
	mov  ebx, TYPE arr3 	
	call dumpmem
	call crlf
	call   waitmsg

	exit
main ENDP
END main
