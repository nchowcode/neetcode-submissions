from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # user: post
        self.following = defaultdict(set) # user: following

        # need logic to concat the feed of the users

    def postTweet(self, userId: int, tweetId: int) -> None:
        # post = (tweetid, time)
        # tweets = userid : post
        currTime = self.time
        self.time += 1
        post = (tweetId, currTime)
        # stamp post
        self.tweets[userId].append(post)

    def getNewsFeed(self, userId: int) -> List[int]:
        # no time constraint
        # min heap for time
        completeFeed = set()

        for fid in self.following[userId]:
            tweets = self.tweets[fid]
            completeFeed.update(tweets)

        completeFeed.update(self.tweets[userId])
        # now we must heapify with key time
        heap = [(time, tweet) for tweet, time in completeFeed]
        heapq.heapify_max(heap)

        k = 0
        res = []
        while k < 10 and heap:
            newestTweet = heapq.heappop_max(heap)
            res.append(newestTweet[1])
            k += 1
        # refill heap
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
