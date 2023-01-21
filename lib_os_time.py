import os

print(os.getcwd())
os.chdir('C:\\Users\\karol\\Desktop\\nauka git')
print(os.getcwd())
os.rename('new_folder', 'new_folder2')
os.rmdir('new_folder2')

