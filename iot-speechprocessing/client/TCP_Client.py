#!/usr/bin/env python3

import socket
import json
import numpy as np


CONFIG_FILE_NAME = "config.json"

HOST = '127.0.0.1'  # The server's hostname or IP address
try:
    PORT = int(json.load(open(CONFIG_FILE_NAME, "r"))["port"]) # The client's port
except OSError:
    PORT = 2020

try:
    HOST = json.load(open(CONFIG_FILE_NAME, "r"))["server_ip"]
except OSError:
    HOST = "127.0.0.1"


def speech_to_text(array):
    # Connects to the server and send it's message
    # Prints the server reply
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        convertible_list = array.tolist()
        raw_msg = json.dumps(convertible_list)
        full_msg = raw_msg + '*'
        # print("a", full_msg)
        # Send the String to the server
        s.sendall(bytes(full_msg, "utf-8"))
        # Receive the translated message
        server_data = ''
        while True:
            part = s.recv(1024)
            server_data = server_data + part.decode("utf-8")
            # Return the text and close the client after it was fully received
            # print("Current data:", server_data)
            if server_data[-1] == '*':
                text_data = server_data[:-1]  # json.loads(server_data[:-1])
                # TODO: CLIENT CLOSE
                return text_data


if __name__ == '__main__':
    testarray = np.array([1, 2, 3])
    print("The result is: ", speech_to_text(testarray))
