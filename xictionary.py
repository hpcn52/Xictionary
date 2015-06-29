# -*- coding: utf-8 -*-
# XICTIONARY.PY
# Jun/28/2015
# hpjju@live.com

def load_file_passage(filename):
	file = open(filename)
	print 'successful: load passage file!'
	dic = {}
	cache = ''
	points = ['.', ',', '\"', '!', ':', ';', '(', ')', '?', '-']
	for line in file:
		words = line.strip().split()
		for word in words:
			if len(word) > 1 and word[len(word) - 1] == '-':
				cache += word[0:len(word) - 1]
				continue
			for point in points:
				word = word.replace(point,'')
			if cache != '':
				word = cache + word
				cache = ''
			if word == '' or word == ' ':
				continue
			if word in dic:
				dic[word] += 1
			else:
				dic[word] = 1
	print 'successful: passage file --> XICT'
	file.close()
	return dic

def load_file_dic(filename):
	if filename == '':
		print 'no XICT file'
		return{}
	file = open(filename)
	print 'successful: load dic file!'
	dic = {}
	line_num = 0
	for line in file:
		line_num += 1
		words = line.strip().split(' - ')
		if len(words) == 2:
			if words[0] in dic:
				dic[words[0]] += int(words[1])
			else:
				dic[words[0]] = int(words[1])
		else:
			print 'error: line %d in XICT file!' % line_num
	print 'successful: dic file --> XICT'
	file.close()
	return dic

def combine_dic(passage_xict, dic_xict):
	for word in passage_xict:
		if word in dic_xict:
			dic_xict[word] += passage_xict[word]
		else:
			dic_xict[word] = passage_xict[word]
	return dic_xict

def write_file_xict(xict, filename):
	file = open(filename, 'w')
	for line in xict:
		file.write(line[0] + ' - ' + str(line[1]) + '\n')
	file.close()
	print 'successful: write to new XICT is OK!'


dic_xict = load_file_dic(raw_input('please input XICT file name:'))
passage_xict = load_file_passage(raw_input('please input passage file name:'))
xict = sorted(combine_dic(passage_xict, dic_xict).items(), key = lambda i:i[1], reverse = True)
write_file_xict(xict, raw_input('please input new xict file name:'))