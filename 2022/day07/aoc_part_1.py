
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent=None):
        self.files = []
        self.dirs = []
        self.parent = parent
        self.name = name
        self.size = 0


def get_size(cd):
    s = 0
    for f in cd.files:
        s += f.size
    for d in cd.dirs:
        s += get_size(d)
    cd.size = s
    #print(f'{cd.name} {s}')
    return s

def get_wanted_size(cd):
    s = 0
    for d in cd.dirs:
        s += get_wanted_size(d)
    if cd.size <= 100000:
        s += cd.size
        #print(f'{cd.name} {s}')
    return s

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    root = Directory('/')
    cd = root
    for l in lines:
        l = l.strip()
        if l.startswith('$ cd'):
            p = l[5:]
            if p == '/':
                cd = root
            elif p == '..':
                cd = cd.parent
            else:
                nd = Directory(p, parent=cd)
                cd.dirs.append(nd)
                cd = nd
        elif not l.startswith('$') and not l.startswith('dir'):
            s, n = l.split(' ')
            f = File(n, int(s))
            cd.files.append(f)

    get_size(root)
    result = get_wanted_size(root)

    return result
