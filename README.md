# cryptology-tools
一些常见的加密算法的实现，供平时使用
* caesar  凯撒加密

  Usage:
	1. python caesar.py encode|decode
	   console mode
	2. python caesar.py encode|decode infile outfile [key]
	   if not input key, It will auto compute

* bitseq2bin: 将0/1组成的字符串序列转换成二进制文件
  
  Usage:

	python bitseq2bin.py bitseqstrfile outdatabinfile
