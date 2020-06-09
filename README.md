# Advanced Malware Obfuscation techniques
A repository of obfuscation techniques and poc code

# Abstract
Traditional antiviruses used signature based schemes to detect and classify malware. While this approach is fast and premptive it falls victim to one of the problems of false positives and true negatives. While false positives cause frequent minor inconvienices true negatives have more insidious effect. A true negative malware will bypass all forms of protection and will hit where the impact is the most severe. Our objective is not to devise a solution to this problem. We demonstrate by examples how trivial it is algorithmically to force a true negative on an otherwise known malware. Our collections of examples are our contributions in highlighting how easy it is to exploit the problem. We conclude alternative detection mechanisms are nessecary to detect malware. On its own signature detection is not sufficient for acceptable security. Our contributions are the examples and algorithms that describe how evade signature based detection.

# Introduction
Our project highlights the problem of false negatives in the realm of antivirus software. When a malware sample when placed in an enviroment where an antivirus software is functional and the sample survives detection and is able to carry out the intentions of its creator then the sample is known to be a true negative. That is to say the sample was malware but the antivirus software failed to detect it therefore failed to stop it. The reason why this problem is significant is because even isolated air gaped computing devices are under threat from malware via an infected flash drive or storage exchanges. Another reason why true negative are a problem is because they are relatively easy to produce and the techniques and iterations in which they can be used are diverse as well as prevalent.
Our project is a demonstration of these techniques. We will in the interest of time we will present functional algorithms for two of the mentioned techniques and provides examples for the rest. One metamorphic generator is present on [github](https://github.com/a0rtega/metame). We believe we have made a somewhat improvement on this by adding dynamic NOP sledges, junk code amoung other features as well as parameterizing the mutations that occur. The evaluation is done by diffing the original payload to the 1st generation of morphing. Then dry running the generations vs the original payload to see if the result is the same. Our results were with each generation the payload becomes more indistiguishable for metamorphism as well as increasing in size most of the time. For polymorphism each payload generation is different but a set of instructions that are responsible for the mutation remain similar.
While they accomplish the same job polymorphism is limited by design and is not as well assimilated into the payload as metamorphism.
This github repository contains our contributions.

# Related Work
There is little to no academic literature describing algorithms that can be used to obfuscate executable code beyond trivial cases. Few particularly intresting application of obfuscation is [the paper on wierd machines](http://stedolan.net/research/mov.pdf). This paper provides examples on how solely the MOV instruction can be used to implement metamorphism as a form of a wierd machine. [Another paper](https://www.usenix.org/system/files/conference/woot13/woot13-bangert.pdf) discusses implementation of wierd machines with components like the interrupt handler and MMU. Our example on virtual machine is quite similar in principle to the discussed work.

# Adversary Model
Our adversary is a computing device with limitless computational ability but it is restricted to the most efficient string matching (signature detection) algorithm. It also has at its disposal a large database encompassing all the malware that has ever been written addiitonally it has already recorded the first N-generations of our payload.

# Design
..* Packed and or encrypted code (polymorphism):
The process consists of an unwrapper and an encrypted payload and decryption key. the process first decrypts the payload executes it and produces another generation with the same payload encrypted under a different key. 
..* Customized virtual machines/Interpreters (metamorphism):
The process becomes a host for emulating a machine whose instruction set is generated randomly so instead of changing the the payload which is executing, this approach changes the entire platform under which it is executing and therefore makes nessecary changes to the payload as well.
..* Alternate arithmatic/logic
The way in which the ALU is used can be varied to have the same result. This technique takes advantage of that fact. Since there are infinite ways to write a program that is functionally identical to the original program enables this technique to be used for obfuscation.
..* Junk instructions (NOPS)
The most trivial way of introducing metamorphism goes a long way to defeat most signature matching algorithms. NOPs or junk instructions are instructions that are desgined to be exectuted as normal instructions but do not intefere or change functionality where ever they are introduced.
..* Order of independent instructions
Some chunks of instructions or instructions themselves can be shuffled such that instructions that depend on the shuffled instruction or the instructions the shuffled instruction depends on occur in the same sequence. While the exploitation of this technique is limited to where it may be applicable and the frequency of its possible occurances (both of which in a large payload are abundant) the size of each generation takes the same space. Another benefit of this is its very stealthy and leaves little to no evidence. 
..* Renaming symbols/storage locations
This technique requires instructions be checked for dependancy. A symbol table must be populated and instruction must be changed to accomodate the same symbols but via different locations of storage. Since registers and locations are a part of the instruction the payload changes drastically with each generation.
..* Code compression
Common code structures can be enumerated and stored in a serperate location which are called where ever they are located. While this does implment a limited form of metamorphism it serves to reduce the size of the payload.
..* Jump mangling/bridging


