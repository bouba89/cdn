#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,os,re,glob
#print(os.listdir(sys.argv[1]))

def error_exit ():
	print('Error: an argument (Folder) is require for running script !')
	print('type ./' + str(sys.argv[0]) + ' <arg>' )
	sys.exit()

if __name__ ==  '__main__':
	''' DEBUG
	'''
	'''
	print("Nom du fichier : ", sys.argv[0])
	print("Nombre d'arguments: ", len(sys.argv))
	print("Liste des arguments: " , str(sys.argv))
	'''
	''' END DEBUG
	'''
	if len(sys.argv) > 1 and len(sys.argv) < 3:
	
		folder = sys.argv[1]
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
		markdown.write("#" + folder  + "\n")
		for file in glob.glob(pathname, recursive=True):
			print(file)
		
			#remove folder/ from folder/path/file
			file_replaced = re.sub(folder, '', file)

			
			#[Link to another page](./another-page.html).
			markdown.write("\n")
			markdown.write("[" + file + "](." + file_replaced + ").\n")
			
		markdown.close()


	else:
		error_exit()