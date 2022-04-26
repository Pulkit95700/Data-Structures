import os 
def find_files(suffix,path):
	if suffix == "":
		return []
	if len(os.listdir()) <= 0:
		return []
	
	path_elements = os.listdir(path)
	path_files = [file for file in path_elements if "." + suffix in file]
	path_folders = [file for file in path_elements if "." not in file]

	for folder in path_folders:
		path_files.extend(find_files(suffix = suffix ,path =  path + "/" + folder))

	return path_files

#%% Testing official
# Testing preparation
path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files(suffix='h', path=path_base))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []