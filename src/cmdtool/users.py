import pwd 

def read_user():
    users = []
    for user in pwd.getpwall():
        if user.pw_uid >= 1000 and 'home'in user.pw_dir: #the path would be /home/user
            users.append({
            'name': user.pw_name,
            'id': user.pw_uid,
            'home': user.pw_dir,
            'shell': user.pw_shell,
        })
    return users