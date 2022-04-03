
from hashmap import Map
import time
trial = [200000, 300000, 400000]
for k in trial:
    m = Map(k)
    starts = time.time()
    with open("./Data/english_small.txt", 'r') as english_text:
        large = english_text.readlines()
    t_read_datas = time.time()
    print(f"time to read the english small data : {t_read_datas - starts}")

    for item in large:
        m[item] = len(item)
    time_stores = time.time()
    print(f"the time to store to hashtable : {time_stores - t_read_datas}")

    startl = time.time()
    with open("./Data/english_large.txt", 'r') as english_text:
        large = english_text.readlines()
    t_read_datal = time.time()
    print(f"time to read the english large data : {t_read_datal - startl}")

    for item in large:
        m[item] = len(item)
    time_storel = time.time()
    print(f"the time to store to hashtable : {time_storel - t_read_datal}")


