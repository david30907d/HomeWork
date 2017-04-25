# -*- coding: utf-8 -*-
# chat_server.py
 
import sys
import socket
import select, random
import collections


class pocker(object):
    """docstring for pocker"""
    def __init__(self):
        self.card = list(range(1,53))
        random.shuffle(self.card)
        self.table = collections.defaultdict(list)
    def start(self, num):
        num = int(num)
        for i in range(num):
            self.table[str(i)].append(self.cal(self.card.pop()))
            self.table[str(i)].append(self.cal(self.card.pop()))
        self.table['banker'] = self.table['0']
        del self.table['0']
    def show(self, player):
        tmp = self.table['banker']
        return 'banker:'+str(tmp[:1])+'\n'+player+':'+str(self.table[player])
    def cal(self, num):
        num = int(num)
        if num-num/13*13 == 0:
            return (num/13)-1, 13
        return (num/13, num-num/13*13 if num>13 else num)
    def getcard(self):
        return self.cal(self.card.pop())
    def bang(self, card):
        print(card)
        print(type(card))
        try:
            result = reduce(lambda x,y:x+y, map(lambda x:x[1], card))
        except Exception as e:
            print(e)
            raise e
        if result >21:
            return True, False
        elif result==21:
            return False, True
        return False, False

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009
p = pocker()
playlist = {}

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print("Chat server started on port " + str(PORT))

 
    while 1:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print("Client (%s, %s) connected" % addr)
                 
                broadcast(server_socket, sockfd)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if 'start' in data:
                        # there is something in the socket
                        playlist['banker'] = sock
                        for index, i in enumerate(filter(lambda s:s!=sock and s!=server_socket, SOCKET_LIST)):
                            playlist[str(index+1)] = i
                            
                        num = data.split()[1]
                        p.start(num)
                        broadcast(server_socket, sock, initial=True)
                    elif data:
                        # there is something in the socket
                        data = data.replace('\n', '')
                        print(data, data=='y', data=='ys')
                        if data=='y':
                            print(11111111111111)
                            broadcast(server_socket, sock, flag='y')  
                        elif data=='ys':
                            broadcast(server_socket, sock, flag='ys')
                        elif data=='end':
                            broadcast(server_socket, sock, flag='end')

                # exception 
                except:
                    # broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, initial=False, flag=None):
    # for socket in SOCKET_LIST:
    #     # send the message only to peer
    #     if socket != server_socket and socket != sock :
    #         try :
    #             socket.send(message)
    #         except :
    #             # broken socket connection
    #             socket.close()
    #             # broken socket, remove it
    #             if socket in SOCKET_LIST:
    #                 SOCKET_LIST.remove(socket)
    # print('***********************************')
    # print(playlist)
    # print(p.table)
    # print('***********************************')
    if initial:
        for key, socket in playlist.items():
            # send the message only to peer
            try :
                if key == 'banker':
                    if p.bang(p.table['banker'])==(True, False):
                        playlist['banker'].send(str(p.table['banker']))
                        playlist['banker'].send('Lose!!!')
                        for key, playlist['banker'] in playlist.items():
                            if key != 'banker':
                                playlist['banker'].send('You Win!!!')
                    if p.bang(p.table['banker'])==(False, True):
                        playlist['banker'].send(str(p.table['banker']))
                        playlist['banker'].send('You Win!!!')
                        for key, playlist['banker'] in playlist.items():
                            if key != 'banker':
                                playlist['banker'].send('Banker Win!!!')
                    socket.send(str(p.table['banker']))
                else:
                    if p.bang(p.table[key])==(True, False):
                        s.send(p.show(key))
                        s.send('Lose!!!')
                    elif p.bang(p.table[key])==(False, True):
                        s.send(p.show(key))
                        s.send('You Win!!!')
                    socket.send(p.show(key))
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
    elif flag=='y':
        for key, s in playlist.items():
            # send the message only to peer
            if s==sock:
                try :
                    p.table[key].append(p.getcard())
                    if p.bang(p.table[key])==(True, False):
                        s.send(p.show(key))
                        s.send('Lose!!!')
                    elif p.bang(p.table[key])==(False, True):
                        s.send(p.show(key))
                        s.send('You Win!!!')
                    s.send(p.show(key))
                except :
                    # broken s connection
                    s.close()
                    # broken s, remove it
                    if s in SOCKET_LIST:
                        SOCKET_LIST.remove(s)
    elif flag=='ys':
        p.table['banker'].append(p.getcard())
        if 17 <= reduce(lambda x,y:x+y, map(lambda x:x[1], p.table['banker'])) <21:
            playlist['banker'].send("now you don't need to get more pockers!!!")
        if p.bang(p.table['banker'])==(True, False):
            playlist['banker'].send(str(p.table['banker']))
            playlist['banker'].send('Lose!!!')
            for key, playlist['banker'] in playlist.items():
                if key != 'banker':
                    playlist['banker'].send('You Win!!!')
        if p.bang(p.table['banker'])==(False, True):
            playlist['banker'].send(str(p.table['banker']))
            playlist['banker'].send('You Win!!!')
            for key, playlist['banker'] in playlist.items():
                if key != 'banker':
                    playlist['banker'].send('Banker Win!!!')
        playlist['banker'].send(str(p.table['banker']))
    elif flag=='end':
        banker = reduce(lambda x,y:x+y, map(lambda x:x[1], p.table['banker']))
        for key, s in playlist.items():
            try:
                # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhh')
                if s != sock:
                    # print('qqqqqqqqqqqqqq')
                    if reduce(lambda x,y:x+y, map(lambda x:x[1], p.table[key])) > banker:
                        # print('-------------------------------------')
                        s.send("banker:"+str(p.table['banker']))
                        s.send(p.show(key))
                        s.send('You Win!!!')
                    else:
                        # print('555555555555555555555555555555555')
                        s.send("banker:"+str(p.table['banker']))
                        s.send(p.show(key))
                        s.send('Lose!!!')
            except Exception as e:
                print(e)
                raise e
            

if __name__ == "__main__":

    sys.exit(chat_server())         