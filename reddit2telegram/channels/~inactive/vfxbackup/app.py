#encoding:utf-8

subreddit = 'vfx'
t_channel = '@vfxbackup'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
