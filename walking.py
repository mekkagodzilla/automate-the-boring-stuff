import os
p = '/home/phil/RPGs'

with open(p + '/listfiles.txt', 'w') as f:

    for folderName, subfolders, filenames in os.walk(p):
        print('The current folder is ' + folderName)
        f.write('The current folder is ' + folderName + '\n')
        for subfolder in subfolders:
            print('Subfolder of ' + folderName + ': ' + subfolder)
            f.write('Subfolder of ' + folderName + ': ' + subfolder + '\n')
        for filename in filenames:
            print('File inside ' + folderName + ': ' + filename)
            f.write('File inside ' + folderName + ': ' + filename + '\n')
        print('')
        f.write('')
