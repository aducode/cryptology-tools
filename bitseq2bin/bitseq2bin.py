#!/bin/python
#-*-  coding:utf-8 -*-
"""
用于将01组成的字符串序列转换成bin文件
"""
import struct,types
def conv(seq, filename):
	seq=seq.strip()
	if not isinstance(filename,types.StringTypes):
		print 'Can not convert,  seq is not StringTypes'
		return False
	if len(seq)%8!=0:
		print 'Can not convert,len(seq)%8!=0'
		return False
	for bit in seq:
		if bit != '0' and bit != '1':
			print 'Invalid bit, just 0/1 correct'
			return False
	with open(filename, 'wb') as binfile:
		for i in xrange(0,len(seq),8):
			u32=int(seq[i:i+8],2)
			bit = chr(u32)
			binfile.write(struct.pack('c',bit))
	return True

if __name__ == '__main__':
	import sys
	if len(sys.argv)!=3:
		print 'Usage:python bitseq2bin.py infile outfile'
		sys.exit(1)
	infile = sys.argv[1]
	outfile = sys.argv[2]
	seq=None
	with open(infile) as inbin:
		seq = inbin.read()
	if not seq or not conv(seq,outfile):
		sys.exit(1)
		
		
