# #Objective: script runs through folder structure and copies files to seperate folder
# #files that need to be copied begin with "Kontoliste_"

#import glob works, but only for on folder -> no sub-folders

# import glob, os, shutil

# source = ("/users/sebastianwayan/desktop/Nancy_Templeton_vanished_heiress")
# destination = ("/users/sebastianwayan/desktop/copytest")

# files = glob.iglob(os.path.join(source, "*.jpg"))
# for file in files:
#     if os.path.isfile(file):
#         shutil.copy2(file, destination)

#-------------

# runs, but not returning files
# import os, shutil

# source = ("/users/sebastianwayan/desktop/Nancy_Templeton_vanished_heiress")
# destination = ("/users/sebastianwayan/desktop/copytest")

# for root, dirs, files in os.walk(source):
# 	for file in files:
# 		if file.endswith ("*.jpg"):
# 			shutil.copy2(file, destination)


#-------------

# runs, but not returning files
# import os, shutil

# source = ("/users/sebastianwayan/desktop/Nancy_Templeton_vanished_heiress")
# destination = ("/users/sebastianwayan/desktop/CopyTest")

# for root, dirs, files in os.walk(source, topdown = True):
# 	for file in files:
# 		if file.endswith ("*.jpg"):
# 			#path_file = os.path.join(root,file)
# 			shutil.copy2(files, destination)	


#-------------
# solve with regular expressions & os - copy object

import os, re

source = ("/users/sebastianwayan/desktop/Nancy_Templeton_vanished_heiress")
destination = ("/Users/sebastianwayan/desktop/copytest")

for root, dirs, files in os.walk(source):
	for file in files:
		if re.match(r'Kontoliste_.*', file, re.M| re.I):
				shutil.copy2(files, destination)




		