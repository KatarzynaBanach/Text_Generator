from collections import Counter
import random


def int_check():
    error_msg1 = 'Enter integer, please:'
    error_msg2 = 'It must be positive number'

    while True:
        try:
            length = int(input())
        except:
            print(error_msg1)
        else:
            if length <= 0:
                print(error_msg2)
            else:
                return length

            
def file_check(mlp):
    print('Enter file:')
    while True:
        i_file = input()
        try:
            with open(i_file, 'r', encoding="utf-8") as file:
                text = file.read()
                text = text.split()
        except FileNotFoundError:
            print('No such file or directory, enter file again:')
        else:
            if len(text) < mlp:
                print(f'This File is to short to generate {mlp} word-long paragraphs. Enter another file:')
            else:
                return text



def create_head_dict(trigrams):
    head_dict = {}
    for head, tail in trigrams:
        head_dict.setdefault(head, []).append(tail)
    head_freqdict = {i[0]: dict(Counter(i[1])) for i in head_dict.items()}
    return head_freqdict


def end_with_punctuation(word):
    if word[-1] in ['!', '.', '?']:
        return True
    else:
        return False


def generate_paragraph(heads_freqdict, mlp):
    while True:
        paragraph = random.choice(list(heads_freqdict.keys()))
        paragraph = paragraph.split()
        if paragraph[0][0].isupper():
            break

    i = 0
    while True:
        head = ' '.join(paragraph[i:i+2])
        tails_weights = list(heads_freqdict[head].values())
        tails_list = list(heads_freqdict[head].keys())
        new_word = random.choices(tails_list, weights=(tails_weights))[0]

        paragraph.append(new_word)
        if len(paragraph) >= mlp and end_with_punctuation(paragraph[-1]):
            break
        i += 1
    return ' '.join(paragraph)


def text_generator():

    print('It\'s text generator\n')
    
    # ask for paramethers of text
    print('Enter minimal length of paragraphs:')
    min_length_paragraps = int_check()
    print('Enter number of paragraphs:')
    number_paragraps = int_check()
    
    # ask for file open it and read
    text = file_check(min_length_paragraps)
    
    # create 'trigrams' - sets of three adjacent words
    trigrams = [(' '.join([text[i],text[i+1]]), text[i+2]) for i in range(len(text)-2)]
    heads_freqdict = create_head_dict(trigrams)

    # create and print text
    for x in range(number_paragraps):
        sentence = generate_paragraph(heads_freqdict, min_length_paragraps)
        print('\n' + sentence)


text_generator()
