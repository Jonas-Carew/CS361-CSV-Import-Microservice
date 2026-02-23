
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

file = input("Enter a file: ")

socket.send_string(file)
valid = socket.recv_string()
if not (valid == "VALID"):
    print(valid)
else:
    csv = socket.recv_pyobj()
    for i in range(10):
        print(csv[i])

