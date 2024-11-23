from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def isOneOff(w1, w2):
            difference = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    difference += 1
                    if difference > 1:  
                        return False
            return difference == 1

        def buildGraph():
            graph = defaultdict(list)
            for i, word in enumerate(wordList):
                for word2 in wordList[i+1:]:
                    if isOneOff(word, word2):
                        graph[word].append(word2)
                        graph[word2].append(word)
            return graph

        if beginWord not in wordList:
            wordList = [beginWord] + wordList
        
        if endWord not in wordList:
            return 0
        
        # Build the graph
        graph = buildGraph()
        
        queue = deque([(beginWord, 1)])  
        visited = set([beginWord])  
        
        while queue:
            current_word, depth = queue.popleft()  
            
            # Check if we reached the endWord
            if current_word == endWord:
                return depth
            
            for neighbor in graph[current_word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        return 0
