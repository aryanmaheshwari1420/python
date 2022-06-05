import os
file1 = 'sample2.txt'
file2 = 'Renamed_by_python.txt'

with open(file1) as f:
    content = f.read()

with open(file2,'w') as f:
    f.write(content)     

os.remove(file1)



