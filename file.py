import json

def get_config(file_name) :
    with open(file_name,'r') as f:
        config_file = json.load(f)
    return config_file


def get_log_reader(_log_file) :
    with open(_log_file,'r') as f:
        for line in f.readlines():
             yield line


def get_reverse_line(_log_file):
     with open(_log_file, 'r') as f:
         for lines in reversed(f.readlines()):
             print(lines,end='')


# get_reverse_line('log_file.txt')

def read_nth_line(_log_file,n):
    with open(_log_file, 'r') as f:
        count =0
        for line in f.readlines():
            count+=1
            if count == n:
                print(line)
            else:
                continue


def get_return_line(_log_file):
    for lines in get_log_reader(_log_file):
        print(lines,end ='')


def get_report(_log_file,n):
    d= { }
    with open(_log_file, 'r') as f:
        for lines in f:
            for i in lines.split():
                if i not in d.keys():
                    d[i]=0
                d[i]+=1
    print(n,':','occured',d[n],'times')
