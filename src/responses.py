
s = None
message = None

def receivingConditions(data):
    if data.find("\n") != -1:
        if data.find("WHO-OK ") != -1:
            name_list = []
            print("Friends online: ")
            namesString = data[6:]
            names = namesString.split(',')

            for i in range(len(names)):
                print(names[i])

        if data.find("SEND-OK\n") != -1:
            print("Server response: send-ok")

        if data.find("UNKNOWN\n") != -1:
            print("Server response: Your guy not here...")

        if data.find("DELIVERY ") != -1:
            deliveryString = data[8:]
            temp = deliveryString.split()
            sender = temp[0]
            receivedMessage = deliveryString[deliveryString.find(sender)+len(sender):]
            print(sender + " says: " + receivedMessage)

        if data.find("BUSY\n") != -1:
            print("Server response: Sorry. Tankhu. COME AGAIN. Close. Busy")

        if data.find("BAD-RQST-HDR\n") != -1:
            print("Sever response: BAD-RQST-HDR")

        if data.find("BAD-RQST-BODY\n") != -1:
            print("Sever response: BAD-RQST-BODY")

def receivinglooper():
    global message

    while True:
        decodedData = ''
        while True:
            data = s.recv(1)
            decodedData += data.decode("utf-8")
            if data.decode("utf-8") == "\n":
                break

            receivingConditions(decodedData)

def server_response():
    data = s.recv(4096)
    decodedData = data.decode("utf-8")
    receivingConditions(decodedData)
    print("Data of function receivelooper" + str(data))
