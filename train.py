import pickle
import re
import random
import sys

def fit(model, input_dir=None):
    print(input_dir)
    text = ''
    if input_dir is None:
        print("Введите текст. Чтобы закончить ввод введите Exit:")
        for line in sys.stdin:
            text += '\n'+line
            if 'Exit' == line.rstrip():
                break
        text = text[:-5]
    else:
        with open(input_dir, encoding="utf8") as f:
            text = f.read()
    reg = re.compile('[\W_]+-\s')
    text = reg.sub('', text)
    words = text.lower().split()
    grams = {}
    frequences = {}
    print('Обучение модели')
    for i in range(len(words) - 1):
        ans = grams.get(words[i], 0)
        if ans == 0:
            grams[words[i]] = [words[i + 1]]
            frequences[words[i]] = [1]
        else:
            try:
                index_of_word = grams[words[i]].index(words[i + 1])
            except ValueError:
                index_of_word = -1
            if index_of_word >= 0:
                array = frequences[words[i]]
                array[index_of_word] += 1
                frequences[words[i]] = array
            else:
                array = grams[words[i]]
                array.append(words[i + 1])
                grams[words[i]] = array
                array = frequences[words[i]]
                array.append(1)
                frequences[words[i]] = array
    with open(f"{model}/model.pickle", 'wb') as f:
        pickle.dump(grams, f)
    print("Модель обучена")

