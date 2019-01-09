import wordtools
import random

if __name__ == "__main__":

    try:
        symbols = wordtools.abc+wordtools.marks + ' ' * 10
        text = ''
        for i in range(300):
            text += symbols[random.randrange(len(symbols))]

        print('Random text:\n\t' + text + '\n')
        print('clean:\n\t{}\n\nwords:\n\t{}\n\nword_count:\n\t{}\n\n\
longest_word:\n\t{}\n\nchar_stats:\n\t{}'.format(wordtools.clean(text),
                                                 wordtools.words(text),
                                                 wordtools.word_count(text),
                                                 wordtools.longest_word(text),
                                                 wordtools.char_stats(text)
                                                 ))

    except Exception as err:
        print('Error occured during execution:', err)
        print('Type:', type(err))
