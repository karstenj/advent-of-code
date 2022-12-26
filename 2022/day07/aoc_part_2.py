
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

def get_wanted_size(cd, space_to_be_deleted):
    s = []
    for d in cd.dirs:
        ret = get_wanted_size(d, space_to_be_deleted)
        s.extend(ret)
    if cd.size >= space_to_be_deleted:
        #print(f'{cd.name} {cd.size}')
        s.append(cd)
    return s

def get_number_part2(input_file_name):
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
    free_space = 70000000 - root.size
    required_space = 30000000
    space_to_be_deleted = required_space - free_space
    print(f'space_to_be_deleted = {space_to_be_deleted}')

    dirs = get_wanted_size(root, space_to_be_deleted)
    dirs = sorted(dirs, key=lambda d: d.size)


    return dirs[0].size
