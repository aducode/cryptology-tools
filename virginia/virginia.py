#!/bin/python
#-*- coding:utf-8 -*-
"""
维吉尼亚密码
"""
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

def encode(plaintext, key):
	if not key or not plaintext:
		return plaintext
	key_idx = 0
	ret=[]
	for alpha in plaintext:
		validated = validate(alpha)
		idx=0
		if validated==1:
			#小写
			idx=ord(alpha)-ord('a')
		elif validated==2:
			#大写
			idx=ord(alpha)-ord('A')
		else:
			ret.append(alpha)
			continue
		k=ord(key[key_idx % len(key)].lower()) -ord('a')
		ret.append(chr((idx + k)%26+(ord('a') if validated==1 else ord('A'))))
		key_idx += 1
	return ''.join(ret)

def decode(ciphertext, key):
	if not key or not ciphertext:
		return ciphertext
	key_idx = 0
	ret = []
	for alpha in ciphertext:
		validated = validate(alpha)
		idx = 0
		if validated == 1:
			#小写
			idx = ord(alpha) - ord('a')
		elif validated == 2:
			#大写
			idx = ord(alpha) - ('A')
		else: 
			ret.append(alpha)
			continue
		k = ord(key[key_idx%26].lower()) - ('a')
		ret.append(chr((idx-k)%26+(ord('a') if validated==1 else ord('A'))))
		key_idx += 1
	return ''.join(ret)

if __name__ == '__main__':
	import sys
	key = None
	mode = None
	inputfile = None
	outputfile = None
	try:
		mode = sys.argv[1]
	except:
		pass
	if mode == 'help':
		print 'Usage:python virginia.py [encode/decode] key in out'
                sys.exit(1)

	if not mode:
		mode = raw_input('Please input mode [encode/decode]:')
	if mode == 'decode':
		f = decode
	else:
		f = encode
	try:
		key = sys.argv[2]
	except:
		pass
	if not key:
		key = raw_input('Please input the key:')
	try:
		inputfile = sys.argv[3]
	except:
		pass
	try:
		outputfile = sys.argv[4]
	except:
		pass
	if not inputfile and not outputfile:
		while True:
			plaintext = raw_input('>')
			print '#%s' % encode(plaintext,key)
	else:
		if inputfile and not outputfile:
			with open(inputfile) as input_file:
				for line in input_file:
					print f(line,key)
		else:
			with open(inputfile) as input_file:
				with open(outputfile, 'w') as output_file:
					for line in input_file:
						output_file.write(f(line,key))
