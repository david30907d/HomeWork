 INCLUDE Irvine32.inc
.data
 bigEndian   BYTE 12h, 34h, 56h, 78h
 littleEndian DWORD ?
 array DWORD 3,3,3,4,5,8,6,9,5
 array2 DWORD 0,2,5,9,5,3,5,7,9,3,3
 array7 DWORD 9,5,3,5,3
 array3 SDWORD 3,3,3,4,5,8,6,9,5,8,4
 array4 SDWORD 0,2,5,9,5,3,5,7,9,3,3
 array5 SDWORD 3,3,3,4
 array6 SDWORD 0,2,5,9
 qString BYTE "Question",0
 displace DWORD 3

.code
main PROC
;Q4
	mov edx,OFFSET qString
	call WriteString
	mov eax,4
	call WriteDec
	call crlf
	
	push OFFSET array
	push LENGTHOF array
	call FindT
	call writeInt
	call crlf
	push OFFSET array2
	push LENGTHOF array2
	call FindT
	call writeInt
	call crlf
	push OFFSET array7
	push LENGTHOF array7
	call FindT
	call writeInt
	call crlf

;Q9
	mov edx,OFFSET qString
	call WriteString
	mov eax,9
	call WriteDec
	call crlf
	call crlf

	push OFFSET array3
	push LENGTHOF array3
	push OFFSET array4
	push LENGTHOF array4
	push displace
	call CountNear
	call writeInt
	call crlf
	push OFFSET array5
	push LENGTHOF array5
	push OFFSET array6
	push LENGTHOF array6
	push displace
	call CountNear
	call writeInt
	call crlf

	call   waitmsg
	exit
main ENDP

FindT PROC
	push ebp
	mov ebp,esp
	push ecx
	push esi
	push ebx
	mov ecx,[ebp+8]
	mov esi,[ebp+12]
	L1:
		cmp ecx,0
		je L2
		mov ebx,[esi]
		add esi,TYPE DWORD
		sub ecx,1
		cmp ebx,3
		jne L1
		cmp ecx,0
		je L2
		mov ebx,[esi]
		add esi,TYPE DWORD
		sub ecx,1
		cmp ebx,3
		jne L1
		cmp ecx,0
		je L2
		mov ebx,[esi]
		add esi,TYPE DWORD
		sub ecx,1
		cmp ebx,3
		jne L1
		mov eax ,1
		pop ebx
		pop esi
		pop ecx
		mov esp,ebp
		pop ebp
		ret 8
	L2:
		mov eax ,0
		pop ebx
		pop esi
		pop ecx
		mov esp,ebp
		pop ebp
		ret 8

FindT ENDP
CountNear PROC
	push ebp
	mov ebp,esp
	push ebx
	push ecx
	push esi
	push edx
	
	mov ecx,[ebp+12]
	inc ecx
	mov esi,[ebp+16]
	mov edx,[ebp+24]
	mov eax,0
	L3:
		dec ecx
		cmp ecx,0
		je L5
		mov ebx,[esi]
		sub ebx,[edx]
		add esi,TYPE SDWORD
		add edx,TYPE SDWORD
		cmp ebx,0
		jg L4
		neg ebx
	L4:
		cmp ebx,[ebp+8]
		jg L3
		inc eax
		jmp L3
	L5:
		pop edx
		pop esi
		pop ecx
		pop ebx
		mov esp,ebp
		pop ebp
		ret 20
CountNear ENDP
END main
