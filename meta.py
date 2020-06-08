import random

STACK=[
	"PUSH",
	"PUSHA",
	"PUSHAD",
	"PUSHF",
	"PUSHFD",
	"PUSHFQ",
	"CALL",
	"POP",
	"POPA",
	"POPAD",
	"POPF",
	"POPFD",
	"POPFQ"
]
REG=[
	"EAX",
	"EBX",
	"ECX",
	"EDX"
]
STK=[
	"ESP",
	"EBP",
]
IDX=[
	"EDI",
	"ESI",
]
ADDR=[
	"[]"
]

mutation=[]
def nop1(instruction,threshold):
	for i in range(0,threshold):
		instruction=instruction+"\nNOP"
	return instruction
def nop2(instruction,threshold):
	(operator,operands)=instruction.split('\t')
	operand=operands.split(',')
	if (operator in STACK) or (operand in STK):
		instruction=instruction+"\nPUSHA\nPOPA"
		return instruction
	else:
		for i in range(0,threshold):
			instruction="PUSHA\n"+instruction+"\nPOPA"
		return instruction
mutation.append(nop1)
mutation.append(nop2)
mutation_chance=0.5
patch=[]
code=open("payload.asm").read().split('\n')
for instruction in code:
	if mutation_chance>random.random():
		instruction=mutation[0](instruction,1)		
		instruction=mutation[1](instruction,1)
	patch.append(instruction)
for token in patch:
	print token
