
# -*- coding: UTF-8 -*-
#usage: sys.argv[0] url output
# http://www.shengzhujiage.com/zjg/mao/ 

import sys
import urllib
import urllib2
import re
import os

########################
#####   Functions  #####
########################

def getHtml(url):
	request = urllib2.Request(url)
	respones = urllib2.urlopen(request)
	html = respones.read()
	return html

def getLinks(html):
	#get the each day link
	ms1 = u'毛猪价格</a>]·'.encode('CP936')
	ms2 = u'[0-9\u4e00-\u9fa5]+全国毛猪[\u4e00-\u9fa5]+'.encode('CP936')
	r1 = r'%s<a href=\'?\"?([\w|\s|\d|.:/]+)\'?\"?>%s' % (ms1,ms2)
	r1_compile = re.compile(r1)
	link_list = re.findall(r1_compile,html)
	return link_list

def replace(x):
	re_Br = re.compile('<br />|<br>') 
	re_Addr = re.compile('<a.*?>|</a>')
	re_tab = re.compile('[ ]+')
	x = re.sub(re_Addr,"",x)
	x = re.sub(re_Br,"\n",x)
	x = re.sub(re_tab,"\t",x)
	return x

def getInfo1(subHtml):
	#get the subHtml info
	r1 = r'data"(.+)<\/div>'
	sub_re = re.compile(r1)
	r1_result = re.findall(sub_re,subHtml)
	return r1_result

def getTitle(subHtml):
	#get the subHtml title
	patten = re.compile('<title>(.*)?</title>') 
	result = re.findall(patten,subHtml)
	return result
'''
def makeDir(path):
	if os.path.exists(path):
		print "[INFO]",path,u"路径存在，数据将保存在此目录中"
	else:
		print u"[INFO] 具体数据将保存在目录",path,u"中！"
		print u"[INFO] 正在创建目录：",path
		os.makedirs(path)
'''

########################
#####      Main    #####
########################

print
print '==============================================='
print 
#make the directory
path = r'D:/PIG_PRICE' #change the dir_path as you like
if os.path.exists(path):
	number = 1
	print "[INFO]",path,u"路径存在，数据将保存在此目录中"
	print u'[NOTE] 仅更新第一个链接！'
	print
else:
	number = 10
	print u"[INFO] 具体数据将保存在目录",path,u"中！"
	print u"[INFO] 正在创建目录：",path
	print u'[NOTE] 将处理10个网页，如需更多，请改源代码！'
	print
	os.makedirs(path)

print '==============================================='

for i in range(1, number + 1):
	tmp = str(i)
	url = r'http://www.shengzhujiage.com/zjg/mao/list_' + tmp + r'.html'
	print
	print u'[INFO]开始处理链接：'+url
	print 
	html = getHtml(url) #
	#print html
	#get the each day link
	list = getLinks(html)

	#get useful info from each link
	for link in list:
		print u"[INFO] 当前链接为："+link
		subHtml = getHtml(link)
		title = getTitle(subHtml)
		filename = path+'/'+title[0]+".xls"
		#print filename
		if os.path.exists(filename):
			print '[INFO]',filename,u'文件存在'
			continue
		else:
			print u'[INFO] 创建文件：',filename
			Info = getInfo1(subHtml)
			out=open(filename,"w")
			for info in Info:
				info = replace(info)
				#print info
				out.write(info)
				print u"[DONE] 已获取到",title[0]+".xls",u"数据"
				print
			out.close()
	print u"[FINISH] 完成链接：",url,u"中的所有日期"
	print '-----------------------------------------------'
#print



