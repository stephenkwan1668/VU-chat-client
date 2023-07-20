
import threading
from connection import connect, login, login_check, user_execution, s
from responses import receivinglooper

try:
    t = threading.Thread(target=receivinglooper, args=(), daemon= True)

    connect()
    login()
    login_check()
    user_execution()

    s.close()
except OSError as msg:
    print(msg)
