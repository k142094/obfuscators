#imports
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

#infector
P='''
print "establishing justice..."
print "boosting economy..."
print "developing infrastructure..."
print "rm -rf..."
'''
K=b64encode(get_random_bytes(32))
print E(P,K)
print K
print D('dta4O8tipUlIq2xX4awR2SM+5Z1ybC+qr+QRPkb5b66Zdbq8jjme66IjYjTYCK6fre8c6956Mz3ma9/uwx3redLhd0MYBZWTQ7tYO6z6vvfSYBskBXEOVJvHRv/fIUqDb7oy1wqOUu4kaoaIjuRXwg+A7ycglLyXjbh+JQ6Eih4==','QgOApNqJEK8LjndbE+uYBfyRfj4RRLbR1qm3D3CDV6M==')
