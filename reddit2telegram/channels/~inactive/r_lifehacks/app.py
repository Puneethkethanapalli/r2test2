#encoding:utf-8

subreddit = 'lifehacks'
t_channel = '@r_lifehacks'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
