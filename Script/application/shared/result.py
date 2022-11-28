class Result:
    message = ""
    messages = []

    def hasMessage(self):
        return self.message != "" or len(self.messages) > 0