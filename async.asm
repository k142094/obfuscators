MOV	ECX,EDX
MOV	EAX,0x90
MOV	EBX,0x80
PUSH	EAX
INC	EAX
ADD	EBX,EAX
CALL	func1
JMP	[ECX]
...
MOV	ECX,EDX
MOV	EAX,0x90
MOV	EBX,0x80
PUSH	EAX
INC	EAX
ADD	EBX,EAX
CALL	func1
JMP	[ECX]
