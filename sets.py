# Sets can be used to identify problems with "unique" requirement
import collections

def work_set():
        arr = [90,2,5,5,1,-100,0,90,-200]
        print(set(arr))

        wordList = ["hot","dot","dog","lot","log","cog"]
        L = 3
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        print(all_combo_dict)