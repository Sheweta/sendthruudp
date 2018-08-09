# sendthruudp
Sending Data thru udp
Description
The program creates a short lived process to send json format data.It will send data to host port using udp. It assumes that the server and port is open and the process has permission to send data.

The process expects host port and data as positional arguments
Sample command : python3 sendthruudp.py 0.0.0.0 0 '{"test":"data"}'
Default data_type is json
For more information run python3 sendthruudp.py -h

Limitation
Since there is no acknowledgement from server, if user enters wrong address or port is closed, there is no error raised.
  
USAGE: sendthruudp.py [-h] [--data_type DATA_TYPE] host port data

Sends data to server through port162

positional arguments:
  host                  Host of the server
  port                  Port of the server
  data                  Data to be passed to server

optional arguments:
  -h, --help            show this help message and exit
  --data_type DATA_TYPE
                        Type of data to be sent to server. Default json.
