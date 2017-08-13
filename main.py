import random
import json
width = 10
height = 10
random_width = random.choice(range(width))
random_height = random.choice(range(height))

if __name__ == '__main__':

    with open('data.json') as f:
        data = json.load(f)

    random.shuffle(data['level1'])
    correct_word = data['level1'][0][0]
    dummy_word = data['level1'][0][1]
    for w in range(width):
        for h in range(height):
            if w == random_width and h == random_height:
                print(dummy_word, end="")
            else:
                print(correct_word, end="")
        print()

