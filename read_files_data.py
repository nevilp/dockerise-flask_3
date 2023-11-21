from contextlib import contextmanager


@contextmanager
def file_reader(filename,mode='w'):
    file = open(filename,mode)
    try:
        yield file
    finally:
        file.close()

with file_reader('name.txt','w') as file:
    file.write('extra data')

