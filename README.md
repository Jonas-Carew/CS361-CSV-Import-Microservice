
# CSV Import Microservice

## Description

This microservice allows a program to import a CSV file into an easily usable 'list of lists' format in Python using the ZeroMQ communication library in Python. Specifications on requesting and receiving data are below, along with a UML sequence diagram showing the standard communication with a consumer program.

## Request Format

A standard request to this microservice comes in the form of a ZMQ string send of the file path. The microservice will then attempt to fetch the file and parse its contents, if it is found. An example call is below:

```
socket.send_string("testCSV.csv")
```

## Receive Format

A standard receive from this microservice will start by receiving a string using ZMQ. If, and only if, this string is `"VALID"`, then the microservice will follow with a Python object, containing the data in the CSV, using the ZMQ pyobj send and receive functions. The data that is received will be in a 'list of lists' format, where there is one list, representing the CSV file, containing a list for each row of the CSV file, each of which contains strings for each item in the CSV file. If the initial string that is returned is not `"VALID"`, it will be an error code from those listed at the bottom of this section and may be dealt with as seen fit. In the case of an error, no further data will be transmitted. An example receive code block is below:


```
valid = socket.recv_string()
if not (valid == "VALID"):
    print(valid)
else:
    csv = socket.recv_pyobj()
```

The supported error codes are the following:
```
ERROR: Path does not lead to a CSV file
ERROR: File does not exist
```

