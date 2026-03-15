
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

ERRORS = [
    "Path does not lead to a CSV file",
    "File does not exist",
    ]

def error(err_num):
    socket.send_string("ERROR: " + ERRORS[err_num])

while True:
    recv = socket.recv_string()

    try:
        with open(recv, 'r') as file:
            socket.send_string("VALID",zmq.SNDMORE)
            csv = []
            for line in file:
                csv.append(line.split(","))
            socket.send_pyobj(csv)

    except FileNotFoundError:
        error(1)
        continue

