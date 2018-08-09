# This file creates a short lived process to send json format data
# It will send data to host port using udp
# It assumes that the server and port is open and the process has 
# permission to send data.No handshake happens 
# The process expects host port and data as positional arguements
# Sample command : python3 sendthruudp.py 0.0.0.0 0 '{"test":"data"}'
# Default data_type is json
# For more information run python3 sendthruudp.py -h
#

import socket
import sys
import json
import argparse


# Initialize the socket object 

def initialize(Network,Protocol):
    err_flag=0

    if (Network is None):
       print("Network is not defined")
       err_flag=1
    
    if (Protocol is None):
       print("Protocol is not defined")
       err_flag=1     
    if (err_flag == 1):
       sys.exit(1)

    try:
        sock = socket.socket(Network, Protocol)
        return sock
    except socket.error as e:
        print("Error while creating socket.",e)
        err_flag=1
    except Exception as e:
        print("Exception raised: ",e)
        err_flag=1
    if err_flag == 1:
        sys.exit(1) 


# Convert json object into bytes

def jsontobytes(json_in):
    
    try:
       valid_json =json.loads(json_in)
       bytes_in= json_in.encode('utf-8')
       return bytes_in
    except ValueError as e:
       return None
    except Exception as e:
       return None
  

# Parse the arguements received 
# Initialize the socket
# Convert json to bytes
# Send data to server port
# Return numberof bytes 

def main():

    
    parser = argparse.ArgumentParser(description="Sends data to server through port162")
    parser.add_argument("host",  help="Host of the server")
    parser.add_argument("port", type=int, help="Port of the server")
    parser.add_argument("data", help="Data to be passed to server")
    parser.add_argument("--data_type", help ="Type of data to be sent to server. Default json.")
    args = parser.parse_args()
      
    Network=socket.AF_INET
    Protocol=socket.SOCK_DGRAM
    if args.host and args.port and args.data :
        socket_obj=initialize(Network,Protocol)
       
        
        if args.data_type == 'json' or args.data_type is  None:
            message=jsontobytes(args.data)
            
            bytes_send=socket_obj.sendto(message,(args.host,args.port))
            return(bytes_send)
       

if __name__ == "__main__":
    main()
 

