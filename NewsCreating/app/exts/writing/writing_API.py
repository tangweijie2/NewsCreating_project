#!/usr/bin/env python
# encoding: utf-8

import json


def writing_API(path):
	f = open(path,encoding='utf-8',errors='ignore')
	data_init = json.loads(f.read())
	f.close()
	# print(data_init)
	# f_write = open(r'D:\Python\project\NewsCreating_project\NewsCreating\app\static\writing_source.txt','w',encoding='utf-8')
	single = {}
	#data_uesful = []
	# count = 0
	dict_str = ''
	for i in data_init:
		# count = 0
		for j in i:
			# count += 1
			single.update(j)
			# print(j.values())
		dict_str += "{}，{}，温度为{}，天气情况为{}，风力为{}，空气质量为{}".format(single['城市'],
										 single['时间'],
										 single['温度'],
										 single['天气情况'],
										 single['风力'],
										 single['空气质量'])
		# print(dict_str)
		# f_write.writelines(dict_str)
		# f_write.write('\n')
		dict_str += '\n'
		# print(dict_str)
	return dict_str

if __name__ == '__main__':
	path = r'D:\Python\project\NewsCreating_project\NewsCreating\app\static\writing_source.txt'
	print(writing_API(path))