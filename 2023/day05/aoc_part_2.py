import sys
import unittest
import re

def get_number_part1(input_file_name):
    result = sys.maxsize
    with open(input_file_name) as fh:
        lines = fh.readlines()

    act_list = None
    map_list = [[], [], [], [], [], [], []]
    for l in lines:
        if l.startswith('seeds:'):
            seeds = [int(m.group(0)) for m in re.finditer(r'\d+', l)]
        elif l.startswith('seed-to-soil map:'):
            act_list = map_list[0]
        elif l.startswith('soil-to-fertilizer map:'):
            act_list = map_list[1]
        elif l.startswith('fertilizer-to-water map:'):
            act_list = map_list[2]
        elif l.startswith('water-to-light map:'):
            act_list = map_list[3]
        elif l.startswith('light-to-temperature map'):
            act_list = map_list[4]
        elif l.startswith('temperature-to-humidity map:'):
            act_list = map_list[5]
        elif l.startswith('humidity-to-location map:'):
            act_list = map_list[6]
        elif l.startswith('\n'):
            act_list = None
        elif act_list is not None:
            act_list.append([int(n) for n in l.split()])

    #print(map_list)
    result_map = {}
    for i in range(0, len(seeds), 2):
        #print(seeds[i], seeds[i + 1])
        s = seeds[i]
        while s < seeds[i]+seeds[i+1]:
            seed = s
            if seed in result_map: continue
            #print('Seed', s)
            min_length = sys.maxsize
            for l in map_list:
                for (dest, src, length) in l:
                    if seed >= src and seed < src+length:
                        min_length = min(min_length, length - (seed - src))
                        seed = dest + seed - src
                        break
                #print(s)
            result_map[s] = seed
            result = min(seed, result)
            s += min_length
            #print(s)
    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input1.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
