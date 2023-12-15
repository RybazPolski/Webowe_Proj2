class Session:
    session = []
    
    def __init__(self):
        print("Session cache initialized")

    def add_user(self, username):
        self.session.append(username)
        
    def contains_user(self, username):
        if username in self.session:
            return True
        return False
        

        