class User(object):
    # username, nickname, mobile, password, email, ctime
    def __init__(self, username, nickname, mobile, password, email, ctime):
        self.username = username
        self.nickname = nickname
        self.mobile = mobile
        self.password = password
        self.email = email
        self.ctime = ctime
