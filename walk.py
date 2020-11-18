import os

for foldername, subfolders, filenames in os.walk('D:\\Videos&Movies'):
            for i in filenames:
                print(os.path.abspath(os.path.join(foldername, i)))
                continue


