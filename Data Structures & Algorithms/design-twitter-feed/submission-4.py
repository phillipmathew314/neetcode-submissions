class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.tweet_counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.follow(userId, userId)
        self.tweets[userId].append((self.tweet_counter, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # you could store each person's feed as a max heap. con would be that there's a lot of duplicate data
        # you could compute it on the fly based on the following. but this is slow
        heap = [self.tweets[followee][-1] + (followee,len(self.tweets[followee])-1) for followee in self.following[userId] if self.tweets[followee]]
        heapq.heapify_max(heap)
        res = []
        print(heap)
        while len(res) < 10 and heap:
            tweet_counter, tweetId, followee, ind = heapq.heappop_max(heap)
            res.append(tweetId)
            if ind > 0:
                heapq.heappush_max(heap, self.tweets[followee][ind-1] + (followee, ind-1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
