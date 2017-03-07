 INCLUDE Irvine32.inc
.data
 arr DWORD 0,6,-9,3,-1,5,6,7,8,9
 ij BYTE "please input the value of j",0
 ik BYTE "please input the value of k",0
 range BYTE "input range:0~",0
 question BYTE "Question",0
 ordinary_text BYTE "This is a Plaintext message",0
 encryt_key BYTE "ABXmv#7",0

 topic BYTE "please input the number of choice: ",0
 choice_1 BYTE "1.x AND y",0
 choice_2 BYTE "2.x OR y",0
 choice_3 BYTE "3.NOT x",0
 choice_4 BYTE "4.x XOR y",0
 choice_5 BYTE "5.Exit program",0
 CaseTable BYTE 1	; lookup value
	DWORD AND_op	; address of procedure
	EntrySize = ($ - CaseTable) ; Chap 3, PP. 56~57
	BYTE 2
	DWORD OR_op
	BYTE 3
	DWORD NOT_op
	BYTE 4
	DWORD XOR_op
NumberOfEntries = ($ - CaseTable) / EntrySize
input_x BYTE "please input the value of x: ",0
input_y BYTE "please input the value of y: ",0
ans BYTE "ans= ",0
.code
main PROC

;Q2
	mov edx,OFFSET question
	call WriteString
	mov eax,2
	call WriteDec
	call crlf
	call crlf

	push eax
	mov eax,0
	call SUM
	call WriteInt
	call crlf
	call crlf
	call SUM
	call WriteInt
	call crlf
	call crlf

;Q6
	mov edx,OFFSET question
	call WriteString
	mov eax,6
	call WriteDec
	call crlf
	call crlf
	
	L4:
		mov edx,OFFSET choice_1
		call WriteString
		call crlf
		mov edx,OFFSET choice_2
		call WriteString
		call crlf
		mov edx,OFFSET choice_3
		call WriteString
		call crlf
		mov edx,OFFSET choice_4
		call WriteString
		call crlf
		mov edx,OFFSET choice_5
		call WriteString
		call crlf
		call crlf
		mov edx,OFFSET topic
		call WriteString
		call ReadInt
		mov ebx,OFFSET CaseTable	; point EBX to the table
		mov ecx,NumberOfEntries	; loop counter

	L5:	cmp al,[ebx]	; match found?
		jne L6	; no: continue
		call NEAR PTR [ebx + 1]	; yes: call the procedure
		jmp L4	; and exit the loop
	L6:	add ebx,EntrySize	; point to next entry
		loop L5	; repeat until ECX = 0
	
	L7:
		cmp al,5
		jne L4
		call crlf

;Q8
	mov edx,OFFSET question
	call WriteString
	mov eax,8
	call WriteDec
	call crlf
	call crlf

	call EN_OR_DECRYPT
	call EN_OR_DECRYPT

	call waitmsg
	exit
main ENDP
SUM PROC
	push ecx
	push esi
	push ebx
	push edx
	mov ebx,0
	mov edx,OFFSET ij
	call WriteString
	call crlf
	mov edx,OFFSET range
	call WriteString
	mov eax,0
	mov eax,lengthof arr
	call WriteInt
	call crlf
	mov eax,0
	call ReadInt
	mov ecx ,eax
	mov edx,OFFSET ik
	call WriteString
	call crlf
	mov edx,OFFSET range
	call WriteString
	mov eax,0
	mov eax,lengthof arr
	call WriteInt
	call crlf
	mov eax,0
	call ReadInt
	mov esi,eax
	cmp ecx ,esi
	ja L1
	mov eax,ecx
	mov ecx ,esi
	mov esi,eax
	L1:
		mov eax,ecx
		mov dl,TYPE arr
		mul dl
		add ebx,DWORD PTR arr[eax]
		cmp ecx,esi
		je BREAK
		loop L1
	BREAK:
		mov eax,ebx
		pop edx
		pop ebx
		pop esi
		pop ecx
		ret
SUM ENDP
EN_OR_DECRYPT PROC
	mov ecx,LENGTHOF ordinary_text
	dec ecx
	mov eax,0
	mov edx,0
	mov esi,0
	L2:
		mov ah,BYTE PTR encryt_key[edx]
		mov al,BYTE PTR ordinary_text[esi]
		XOR al,ah
		mov BYTE PTR ordinary_text[esi],al
		
		inc edx
		cmp edx,LENGTHOF encryt_key
		jb L3
		mov edx,0
		L3:
			inc esi
		loop L2
	mov edx,OFFSET ordinary_text
	call WriteString
	call crlf
	ret
EN_OR_DECRYPT ENDP
AND_op PROC
	push eax
	push ebx
	push ecx
	mov eax,0
	mov edx,OFFSET input_x
	call WriteString
	call ReadHex
	mov ebx,eax
	mov eax,0
	mov edx,OFFSET input_y
	call WriteString
	call ReadHex
	mov ecx,eax
	AND ebx,ecx
	mov eax,ebx
	mov edx,OFFSET ans
	call WriteString
	call WriteHex
	call crlf
	call crlf
	pop ecx
	pop ebx
	pop eax
	ret
AND_op ENDP
OR_op PROC
	push eax
	push ebx
	push ecx
	mov eax,0
	mov edx,OFFSET input_x
	call WriteString
	call ReadHex
	mov ebx,eax
	mov eax,0
	mov edx,OFFSET input_y
	call WriteString
	call ReadHex
	mov ecx,eax
	OR ebx,ecx
	mov eax,ebx
	mov edx,OFFSET ans
	call WriteString
	call WriteHex
	call crlf
	call crlf
	pop ecx
	pop ebx
	pop eax
	ret
OR_op ENDP
NOT_op PROC
	push eax
	mov eax,0
	mov edx,OFFSET input_x
	call WriteString
	call ReadHex
	NOT eax
	mov edx,OFFSET ans
	call WriteString
	call WriteHex
	call crlf
	call crlf
	pop eax
	ret
NOT_op ENDP
XOR_op PROC
	push eax
	push ebx
	push ecx
	mov eax,0
	mov edx,OFFSET input_x
	call WriteString
	call ReadHex
	mov ebx,eax
	mov eax,0
	mov edx,OFFSET input_y
	call WriteString
	call ReadHex
	mov ecx,eax
	XOR ebx,ecx
	mov eax,ebx
	mov edx,OFFSET ans
	call WriteString
	call WriteHex
	call crlf
	call crlf
	pop ecx
	pop ebx
	pop eax
	ret
XOR_op ENDP
END main
