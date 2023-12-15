class Session(object):
    def get_username(self, request):
        userName = request.session.get('username', None)
        return userName

    def get_password(self, request):
        password = request.session.get('password', None)
        return password

    def get_user_id(self, request):
        user_id = request.session.get('user_id', None)
        return user_id
    
    def get_session_id(self, request):
        return request.session.session_key

    def set_username(self, request, username):
        request.session['username'] = username

    def set_password(self, request, password):
        request.session['password'] = password
    
    def set_user_id(self, request, user_id):
        request.session['user_id'] = user_id
