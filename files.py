import os

os.chdir('C:\\New folder (2)')
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    f_title = file_name.split('-')
    print(f_title)
    