# Python-Renames
# by iCoACN
# https://www.icoa.cn
import os
old = input('请输入要替换的内容：')
new = input('请输入替换后的内容：')
for file in os.listdir():
	f_name = file
	if f_name.count(old) and not os.path.isdir(file):
		f_new = f_name.replace(old,new)
		os.rename(f_name,f_new)
		print(f_name,'>',f_new)
