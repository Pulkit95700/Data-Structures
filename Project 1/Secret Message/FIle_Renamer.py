import os 
def rename_files(path):
	if len(os.listdir()) <= 0:
		return []
	path_elements = os.listdir()
	lst = [f"{i}" for i in range(10)]
	path_files = [file for file in path_elements if "." in file]
	for file_names in path_files:
		new_string = ""
		old_string = file_names
		for char in file_names:
			if char in lst:
				continue
			else:
				new_string+=char
		os.rename(old_string,new_string)

	return path_files

# #%% Testing official
# # Testing preparation
path_base = os.getcwd() + '/Secret Message'

# # Normal Cases:
print(rename_files(path=path_base))
# # ['t1.c', 'a.c', 'a.c', 'b.c']
	
# print(find_files(suffix='h', path=path_base))
# # ['t1.h', 'a.h', 'a.h', 'b.h']

# print(find_files(suffix='z', path=path_base))
# # []

# # Edge Cases:
# print(find_files(suffix='', path=path_base))
# # []