#!/bin/python
#-*- coding:utf-8 -*-
alphalist={
	'upper':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'lower':'abcdefghijklmnopqrstuvwxyz',
}
def validate(alpha):
	"""
	判断是否是字母
	:param alpha 字符
	:return 0不是字母 1 小写 2 大写
	"""
	if alpha in alphalist['lower']:
		return 1
	elif alpha in alphalist['upper']:
		return 2
	else:
		return 0
def encode(plaintext, key=13):
	"""
	凯撒密码加密
	:param plaintext 明文
	:param key 密钥（位移）
	:return 密文
	"""
	buf=[]
	for alpha in plaintext:
		validated = validate(alpha)
		if validated==1:
			idx = ord(alpha) - ord('a')
			idx += key
			if idx>25:
				idx-=26
			buf.append(chr(idx+ord('a')))
		elif validated==2:
			idx = ord(alpha) - ord('A')
			idx+=key
			if idx>25:idx-=26
			buf.append(chr(idx+ord('A')))
		else:
			buf.append(alpha)	
	return ''.join(buf)
def decode(ciphertext, key=13):
	"""
	凯撒密码解密
	:param ciphertext 密文
	:param key 密钥（位移）
	:return 明文
	"""
	return encode(ciphertext, 26-key)


def autocomp(infile):
	rate={}
	with open(infile) as i_file:
		for line in i_file:
			for alpha in line:
				alpha = alpha.lower()
				if validate(alpha)==1:
					if alpha not in rate:
						rate[alpha]=1
					rate[alpha]+=1
	max_key = None
	max_value= 0
	for k, v in rate.items():
		print k,'\t\t',v
		if max_value<v:
			max_value=v
			max_key=k
	print 'MAX rate:\n',max_key,'\t\t',max_value
	ret = ord(max_key) - ord('e')
	if ret<0:
		ret+=26
	return ret

if __name__ == '__main__':
	import sys
	def print_usage():
		usage=[
			'Usage:',
			'\t1. caesar encode|decode',
			'\t   console mode',
			'\t2. caesar encode|decode infile outfile [key]',
			'\t   if not input key, It will auto compute',
		]
		print '\n'.join(usage)
	if len(sys.argv)==1:
		print_usage()
		sys.exit(1)
	if len(sys.argv)==2 and sys.argv[1] in ('encode','decode'):
		print 'IN ', sys.argv[1].upper(),' MODE'
		key = int(raw_input('please the key:'))
		print 'Please input plaintext:'
		while True:
			text = raw_input('> ')
			print '#',globals()[sys.argv[1]](text,key)
	elif len(sys.argv)>=4 and sys.argv[1] in ('encode','decode'):
		op=sys.argv[1]
		infile=sys.argv[2]
		outfile=sys.argv[3]
		key = None
		if len(sys.argv)==5:
			try:
				key = int(sys.argv[4])
			except:
				pass
		if not key:
			key = autocomp(infile)
			print 'try the key:',key
		with open(infile) as f_input:
			with open(outfile,'w') as o_file:
				for line in f_input:
					o_file.write(globals()[op](line, key))
	else:
		print_usage()
		sys.exit(1)
