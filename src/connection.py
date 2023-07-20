
import socket

s = None
name = None
message = None

def connect():
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("18.195.107.195", 5378))

def login():
    global name

    name = input("What is your username? ")
    Initial_handshake_msg("HELLO-FROM", name)

def login_check():
    global name
    global loginReply
    global s

    nameByteLength = len(name)
    undecoded_reply = s.recv(16 + nameByteLength)
    loginReply = undecoded_reply.decode("utf-8")
    print("server response: " + loginReply)

    if loginReply.find("IN-USE\n") != -1:
        s.close()
        connect()
        print("User name is already in use, please enter another name.")
        login()
        login_check()

    elif loginReply == ("HELLO " + name + "\n"):
        print("You are logged in. Welcome " + name)
        send_msg("WHO")
        print("\nYou can chat.\n")

def Initial_handshake_msg(header, body):
    message = (header + " " + body + "\n").encode("utf-8")
    s.sendall(message)

def send_msg(header):
    message = (header + "\n").encode("utf-8")
    s.sendall(message)

def user_execution():
    global name
    global message

    print("Please enter execution: \n"
          "@[name of receiver] , sending messages\n"
          "!who , show list of users that are online\n"
          "!quit , quit the chat\n")

    while True:
        message = input()
        if message == "!quit":
            print("logging out")
            break

        elif message == "!who":
            send_msg("WHO")

        elif message[0] == "@":
            incomming = message[1:]
            temp = incomming.split()
            receiver = temp[0]
            message = incomming[len(receiver):]
            print(f"{name} > {message}")

            encodedString = ("SEND " + receiver + " " + message + "\n").encode("utf-8")
            s.sendall(encodedString)
