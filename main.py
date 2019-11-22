from sets import work_set
import collections
import heapq
from trees_practice import tree_ques

def valid(s):
            count = 0
            
            for c in s:
                count += 1 if c == '(' else -1 if c == ')' else 0
                if count < 0:
                    return False
            
            return count == 0


def main():
  tree_ques()
    
if __name__ == "__main__":
  main()