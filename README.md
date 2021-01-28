
# A n00b's Perspective to Red Team: DYI Implant<br><br>
## To Execute Implant 
`python3 implant_blog.py`

## Execute Client
``` 
usage: client.py [-h] [--download <download_file>] [--upload <upload_file>]
                 [--destination_file <destination_file>]
                 [--execute <execute_command>]
                 <destination_ip> <destination_port>

Communicates to Implant

positional arguments:
  <destination_ip>      Example: ./client.py <destination_host>
  <destination_port>    Example: ./client.py 127.0.0.1 9999

optional arguments:
  -h, --help            show this help message and exit
  --download <download_file>
                        Example: ./client.py 127.0.0.1 9999 --download
                        /path/to/remote/file
  --upload <upload_file>
                        Example: ./client.py 127.0.0.1 9999 --upload
                        /path/to/upload/file
  --destination_file <destination_file>
                        Example: ./client.py 127.0.0.1 9999 --upload
                        /etc/passwd --destination_file /path/on/remote/server
  --execute <execute_command>
                        Example: ./client.py 127.0.0.1 9999 --execute /bin/ls

