import os
path='.'
def fileMerge(path: str):
    files_list=os.listdir(path)
    file_voc={}
    for text_file in files_list:
        if text_file.rfind('.txt') >=0:
            with open(os.path.join(path,'1.txt'),'r',encoding='utf-8')as file:
                file_voc["1.txt"]=file.readlines()
            with open(os.path.join(path,'2.txt'),'r',encoding='utf-8')as file:
                file_voc["2.txt"]=file.readlines()
            with open(os.path.join(path,'3.txt'),'r',encoding='utf-8')as file:
                file_voc["3.txt"]=file.readlines()
    with open('4.txt', 'w', encoding='utf-8')as file:
        for file_name, rows in sorted(file_voc.items(), key=lambda x: len(x[1])):
            file.write(file_name+'\n')
            file.write(str(len(rows))+'\n')
            if '\n' not in rows[-1]:
                rows[-1]+='\n'
            file.write(''.join(rows))
fileMerge(path)

