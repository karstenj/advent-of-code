import hashlib


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        secret = fh.read().strip()
    while True:
        key = secret + str(result)
        hash = hashlib.md5(key.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            print(hash)
            break
        result += 1
    return result


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        secret = fh.read().strip()
    while True:
        key = secret + str(result)
        hash = hashlib.md5(key.encode('utf-8')).hexdigest()
        if hash.startswith('000000'):
            print(hash)
            break
        result += 1
    return result
