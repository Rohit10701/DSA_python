from collections import defaultdict


def groupAnagrams(strs):
        
        hashmap = { }

        for s in strs:
            x = tuple(sorted(s))
            hashmap[x] = hashmap.get(x,[]) +[s]

        return hashmap.values()

ls=["ab","ba","a"]
print(groupAnagrams(ls))