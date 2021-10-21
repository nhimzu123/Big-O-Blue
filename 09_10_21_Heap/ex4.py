"""
HackerEarth: Roy and Trending Topics
"""

import heapq


class Topic:
    def __init__(self, topic_id, old_zscore, post, like, comment, share):
        self.topic_id = topic_id
        self.old_zscore = old_zscore
        self.post = post
        self.like = like
        self.comment = comment
        self.share = share
        self.new_zscore = self.post * 50 + self.like * 5 + self.comment * 10 + self.share * 20
        self.change_in_zscore = self.new_zscore - self.old_zscore

    def __lt__(self, other):
        return (self.change_in_zscore, self.topic_id) > (other.change_in_zscore, other.topic_id)


max_heap = []
for i in range(int(input())):
    topic = list(map(int, input().split()))
    heapq.heappush(max_heap, Topic(topic[0], topic[1], topic[2], topic[3], topic[4], topic[5]))

for i in range(5):
    print(max_heap[0].topic_id, max_heap[0].new_zscore)
    heapq.heappop(max_heap)
