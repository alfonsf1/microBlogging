getUserTimeline(username):
    #first check if user is in db
    #if not, return error
    #else find the post with the most recent date
getPublicTimelinme():
    #first, check if user is in db
    #if not, return error
    #else return all the post from that user
getHomeTimeline(username):
    #first, checkf if user is in db
    #if not, return error
    #else return recent posts from all the users that this user is following
postTweet(username, text):
    #first check if the ussername exist
    #if not, error
    #else, post the new tweet