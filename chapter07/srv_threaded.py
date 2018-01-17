#!/usr/bin/env python3
# filename srv_threaded.py
#coding=utf-8

import zen_utils
from threading import Thread

def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        #target指定线程运行的函数，args指定该函数的参数，参数以元组格式传入
        Thread(target=zen_utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
	address = zen_utils.parse_command_line('multi-threaded-server')
	listener = zen_utils.create_srv_socket(address)
	start_threads(listener)

