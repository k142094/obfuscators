JMP	LOC_000000
LOC_000005:
INC	EAX
MOV	EBX,0x80
JMP	LOC_000006
...
LOC_000000:
MOV	EAX,0x90
PUSH	EAX
JMP	LOC_000001
...
LOC_000003:
CALL	func1
JMP	[ECX]
JMP	LOC_000004
...
LOC_000006:
ADD	EBX,EAX
MOV	ECX,EDX
JMP	LOC_000007
...
LOC_000004:
MOV	EAX,0x90
PUSH	EAX
JMP	LOC_000005
...
LOC_000002:
ADD	EBX,EAX
MOV	ECX,EDX
JMP	LOC_000003
...
LOC_000007:
CALL	func1
JMP	[ECX]
JMP	LOC_000008
...
LOC_000001:
INC	EAX
MOV	EBX,0x80
JMP	LOC_000002
