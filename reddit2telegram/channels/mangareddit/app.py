#encoding:utf-8

subreddit = 'manga'
t_channel = '@mangareddit'
submissions_ranking = 'new'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
