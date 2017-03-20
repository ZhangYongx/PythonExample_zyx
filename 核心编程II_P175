db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            print "This name has been used,Try another name"
            continue
        else:
            break
    pwd = raw_input('password: ')
    db[name] = pwd

def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if pwd == passwd:
        print "Welcome back " , name
    else:
        print 'login incorrect'


pompt ="""
(N)ew User login
(E)xist User login
(Q)uit
Enter choice:
"""

done = False
while not done:
    chosen = False
    while not chosen:
        try:
            choice = raw_input(pompt).strip().lower()
        except (EOFError,KeyboardInterrupt):
            choice = 'q'
        print '\nYou picked [%s]' % choice
        if choice not in 'neq':
            print "invalid option, please try another."
        else:
            chosen = True
    if choice== 'n':newuser()
    if choice== 'e':olduser()
    if choice== 'q':done=True

if __name__ == '__main__':
    pompt
