from typing import List
from heapq import heappush, heappop


class Tweet:

    def __init__(self, tId, time):
        self.tId = tId
        self.createdAt = time


class Twitter:

    followedMap = None  # <Integer, HashSet<Integer>>
    tweetsMap = None  # <Integer, List<Tweet>>
    times = None

    def __init__(self):
        self.times = 1
        self.followedMap = {}
        self.tweetsMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        # want to follow myself before tweeting
        self.follow(userId, userId)
        if userId not in self.tweetsMap:
            self.tweetsMap[userId] = []
        t = Tweet(tweetId, self.times)
        self.times += 1
        self.tweetsMap[userId].append(t)

    def getNewsFeed(self, userId: int) -> List[int]:
        pq = []  # of type Tweet
        # get the users that userId is following
        followed = None
        if userId in self.followedMap:
            followed = self.followedMap[userId]
        if followed is not None:
            for fId in followed:
                fTweets = None
                if fId in self.tweetsMap:
                    fTweets = self.tweetsMap[fId]
                if fTweets is not None:
                    le = len(fTweets)
                    i = le-1
                    # java equivalent:
                    # for int i = le-1; i >= 0 && i >= le-11; i--
                    while i >= 0 and i >= le-11:  # O(k) (k=10 tweets)
                        currTweet = fTweets[i]
                        heappush(pq, (currTweet.createdAt, currTweet))
                        if len(pq) > 10:
                            heappop(pq)
                        i -= 1
                    # for fTweet in fTweets: # O(Nlog10) -> O(N)
                    #     heappush(pq, (fTweet.createdAt, fTweet))
                    #     if len(pq) > 10:
                    #         heappop(pq)

        # get all recent tweets from priority q
        result = []
        while len(pq) != 0:
            # appending to the start since most recent at bottom of heap
            result.insert(0, heappop(pq)[1].tId)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followedMap:
            self.followedMap[followerId] = set()
        # by reference (pointer)
        self.followedMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # do not want to unfollow myself
        if followerId in self.followedMap and followerId != followeeId:
            if followeeId in self.followedMap[followerId]:
                self.followedMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
