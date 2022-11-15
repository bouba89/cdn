#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,glob,time
def error_exit ():
	print('Error: an argument (Folder) is require for running script !')
	print('type ./' + str(sys.argv[0]) + ' <arg>' )
	sys.exit()
if __name__ ==  '__main__':
	''' DEBUG
	'''
	'''
	'''
	''' END DEBUG
	'''
	print("Script name  : ", sys.argv[0])
	print("How many arguments: ", len(sys.argv))
	print("List of arguments: " , str(sys.argv))
	if len(sys.argv) > 1 and len(sys.argv) < 3:
		folder = sys.argv[1]
		time.sleep(0.5)
		print("\nList of files and folders in " + folder + ':\n')
		print(os.listdir(folder))
		# search all files inside a specific folder
		# *.* means file name with any extension
		print('\n glob list files and folder recursively \n')
		directory = "./"
		pathname = folder + "/**/*.*"
		#export to html like file but it's a markdown  .md for github
		filename =  folder + '/index.md'	
		if os.path.exists(filename):
			append_write = 'a' # append if already exists
		else:
			append_write = 'w' # make a new file if not
		markdown = open(filename,append_write)
		# here the space is before #
		markdown.write("# " + folder  + " list of files and folders")
		markdown.write("\n") # readding an other space
		for file in glob.glob(pathname, recursive=True):
			print(file)
			# remove folder/ from folder/path/file
			file_replaced = re.sub(folder, '', file)
			# ignore if index.md is added in list of links  
			if file_replaced != '/index.md':
				markdown.write("\n") # readding an other space
				markdown.write("[" + file + "](." + file_replaced + ").\n")
			else:
				print('index.md ignored in ' + folder)
		markdown.write("\n") # readding an other space
		#adding backlink
		markdown.write("[back](https://cdn.wanalike.fr/)")
		markdown.close()
	else:
		error_exit()