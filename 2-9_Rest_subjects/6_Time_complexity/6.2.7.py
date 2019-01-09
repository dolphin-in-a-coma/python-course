
import random
import time

def get_time(func, data):

    time1 = time.time()
    ret = func(data)
    time2 = time.time()
    print(ret)
    return round((time2-time1) * 1000.0, 2)

stop_words = ["buy", "!!!", "die", "sale", "shop", "dicount", "forex"]
stop_dict={i:True for i in stop_words}

#сложность = O(N^2)
def is_spam1(text):
    stop_count = 0
    for word in text.split(' '):
        if word.lower() in stop_words:
            stop_count += 1

    return stop_count * 2 > len(text.split(' '))

#сложность = O(N)
def is_spam2(text):
    text = text.lower()
    text_list=text.split(' ')
    lst = [i for i in text_list if stop_dict.get(i,False)]
    return len(lst) * 2 > len(text_list)


res = [["i", "1 (мс.)", "2 (мс.)"]]
for i in (100, 1000, 10000, 100000,250000,500000,1000000,2000000,4000000):
    data=''
    words=("buy", "!!!", "die", "sale", "shop",
         "dicount","forex", "hi" ,"wazap", "dude", ")))",
         "go", "hang", "out")
    for j in range(i):
        data+=(' '+random.choice(words))
    res.append([i,
                get_time(is_spam1, data),
                get_time(is_spam2, data),])

format_str = "{:>10}" * len(res[0])
for r in res:
    print(format_str.format(*r))
