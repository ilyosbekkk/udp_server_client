from datetime import date

from socket import *
from time import time

import json

# get the info json from local path
info = open('wheel_data.json')
# load it
wheel_data = json.load(info)

# specify server ip address and port number
serverHost = 'localhost'
serverPort = 12000
# create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# set timeout for client
clientSocket.settimeout(1)


# send json data to the server
def sendDataToServer(mydata):
    start = time()
    try:
        # convert json to string
        converted_data = json.dumps(mydata)
        # encode the string
        encodedData = converted_data.encode()
        # send encoded data to the server
        clientSocket.sendto(encodedData, (serverHost, int(serverPort)))
        # get response from the server
        encodedResponse, serverAddress = clientSocket.recvfrom(1024)

        end = time()

        print("server address: " + " " + str(serverAddress))
        print("response from server: " + " " + str(encodedResponse))

        # calculate RTT
        print("Round Trip Time: %.3f ms\n" % ((end - start) * 1000))

    except Exception as e:
        # if exception happens, print the error message (e.g, run time error)
        print(str(e))


# there may be another option where the program runs infinitely (everyday checks if the today's date matches with the
# given date) in that case we have to use infinite loop to check if today's date matches  with the given date in the
# json file but in this program it does not check infinitely: it just iterates over the-> -> elements in the list and
# compares today with the given date in json file

today = date.today()

for data in wheel_data:

    # check if the current time equals the date in the json file, if it equals call the below method
    if str(today) == data["date"]:
        sendDataToServer(data)

# close the client socket
clientSocket.close()
