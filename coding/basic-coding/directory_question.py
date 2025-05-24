# Random:  In current directory of file with .txt using code (IMP)
import os
current_dir = os.getcwd()
ls = os.listdir(current_dir)
txt_files = [file for file in ls if file.endswith('.txt')]
for txt_file in txt_files:
    with open(txt_file, 'w') as file:
        file.write('hello')
    print(f"hello has been written into {txt_file}")