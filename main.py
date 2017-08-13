import random, os, json

if __name__ == '__main__':

    with open('data.json') as f:
        data = json.load(f)

    for width, height in [(4,4), (6,6), (10,10)]:

        random_width = random.choice(range(width))
        random_height = random.choice(range(height))
        geo = str(width) + "x" + str(height)
        random.shuffle(data['level1'])

        for i in range(len(data['level1'])):
            correct_word = data['level1'][i][0]
            dummy_word = data['level1'][i][1]
            with open("./q"+geo+"/q"+str(i)+"_"+geo, "w") as f:
                for w in range(width):
                    for h in range(height):
                        if w == random_width and h == random_height:
                            f.write(dummy_word)
                        else:
                            f.write(correct_word)
                    f.write("\n")

    os.system('./q2png.sh')

    # when 4
    # convert -font ./AquaKana.ttc -size 800x800 -pointsize 200 label:@tmp tmp.png

    # when 6
    # convert -font ./AquaKana.ttc -size 600x600 -pointsize 100 label:@tmp tmp.png

    # when 10
    # convert -font ./AquaKana.ttc -size 1000x1000 -pointsize 100 label:@tmp tmp.png

    # when 20
    # convert -font ./AquaKana.ttc -size 1000x1000 -pointsize 50 label:@tmp tmp.png