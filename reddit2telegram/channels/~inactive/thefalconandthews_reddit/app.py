#encoding:utf-8

subreddit = 'thefalconandthews'
t_channel = '@thefalconandthews_reddit'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
