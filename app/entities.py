class ChatLine:
    def __init__(self, username, message, date):
        self._username = username
        self._message = message
        self._date = date
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    def __str__(self):
        return f"[{self._date.strftime('%Y-%m-%d %H:%M:%S')}] {self._username}: {self._message}"