import socket

class Config:
    monitor_ip = "helios.ececs.uc.edu"
    monitor_port = 8180
    ident = "mtest13"
    password = "12345"
    cookie = ""
    host_ip = socket.getfqdn()
    host_port = 5000
