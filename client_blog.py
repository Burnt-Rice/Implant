
#!/usr/bin/env python3
import os
import socket
import base64
import argparse
import sys

#upload
def b64_file(file_up: str) -> bytes:
    with open(file_up, "rb") as f:
        myFile = f.read()
    myFileB64 = base64.b64encode(myFile)
    return myFileB64
#download
def download_file():

#execute
#connection 
#main


if __name__ == "__main__":
	main()
