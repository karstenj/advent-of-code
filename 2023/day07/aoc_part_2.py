import unittest
import re

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    hands = []
    for l in lines:
        l = l.strip()
        cards = l.split()[0]
        score = int(l.split()[1])
        cards = [c for c in cards]
        #print(cards)
        cards_set = set(cards)
        #print(cards_set)
        card_count = []
        joker = 0
        for c in cards_set:
            if c != 'J':
                card_count.append(cards.count(c))
            else:
                joker = cards.count(c)
        card_count.sort(reverse=True)
        if len(card_count) > 0:
            card_count[0] += joker
        else:
            card_count.append(joker)
        #print(card_count)
        rank = 0
        if card_count[0] == 5:
            # five of a kind
            rank = 0
        elif card_count[0] == 4:
            rank = 1
        elif card_count[0] == 3 and card_count[1] == 2:
            rank = 2
        elif card_count[0] == 3:
            rank = 3
        elif card_count[0] == 2 and card_count[1] == 2:
            rank = 4
        elif card_count[0] == 2:
            rank = 5
        else:
            rank = 6
        card_value = []
        card_values = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
        for c in cards:
            card_value.append(card_values.index(c))
        hands.append((rank, card_value, score))
    hands.sort(key=lambda x: (x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4]), reverse=True)
    for i, (rank, card_value, score) in enumerate(hands):
        result += (i + 1) * score
    #print(hands)
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
