try:
    import os
    import praw
except ImportError:
    print()
    print("ERROR: Problem importing packages in {}").format(
        os.path.realpath(__file__))
    print("Please try \'pip install -r requirements.txt\' to install all required packages")
    print()


async def getRedditPost(PostType, AmountOfPosts):
    # create reddit read-only instance
    reddit = praw.Reddit(client_id="Client ID",
                         client_secret="Client Secret",
                         user_agent="User Agent")
    # print(reddit.read_only)  # True means authorized
    postContent = []

    if PostType == "t":
        for submission in reddit.subreddit("cars").top(limit=AmountOfPosts):
            # postContent.append(submission.title)
            postContent.append(submission.selftext)
    elif PostType == "h":
        for submission in reddit.subreddit("cars").hot(limit=AmountOfPosts):
            # postContent.append(submission.title)
            postContent.append(submission.selftext)
    elif PostType == "n":
        for submission in reddit.subreddit("cars").new(limit=AmountOfPosts):
            # postContent.append(submission.title)
            postContent.append(submission.selftext)

    # print(postContent)
    return postContent


if __name__ == '__main__':
    main()
