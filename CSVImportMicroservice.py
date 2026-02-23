
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

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
        socket.send_string("ERROR: File does not exist")


