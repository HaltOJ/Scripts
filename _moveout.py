import os, shutil


def listdir(path):
    """
    recursively walk directory to specified depth
    :param path: (str) path to list files from
    :yields: (str) filename, including path
    """
    for filename in os.listdir(path):
        yield os.path.join(path, filename)


def walk(path='.', depth=None):
    """
    recursively walk directory to specified depth
    :param path: (str) the base path to start walking from
    :param depth: (None or int) max. recursive depth, None = no limit
    :yields: (str) filename, including path
    """
    if depth and depth == 1:
        for filename in listdir(path):
            yield filename
    else:
        top_pathlen = len(path) + len(os.path.sep)
        for dirpath, dirnames, filenames in os.walk(path):
            dirlevel = dirpath[top_pathlen:].count(os.path.sep)
            if depth and dirlevel >= depth:
                dirnames[:] = []
            else:
                for filename in filenames:
                    yield os.path.join(dirpath, filename)


print('use this to move subtask1/data1 out and rename automatically')

li = walk(depth=2)

for f in li:
    if f.count('/')==2:
        shutil.copyfile(src=f,dst=f.split('/')[1]+'_'+f.split('/')[2])
    elif f.count('\\')==2:
        shutil.copyfile(src=f,dst=f.split('\\')[1]+'_'+f.split('\\')[2])
