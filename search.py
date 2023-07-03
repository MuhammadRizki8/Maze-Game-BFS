# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col) 
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan 
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]-> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function


# memanggil modul queue
# Queue atau antrian adalah barisan elemen/data, dimana ketika elemen/data baru ditambah maka penambahannya akan berada di posisi belakang (rear) dan jika dilakukan pengambilan elemen dilakukan di elemen paling depan (front). Queue dikenal bersifat FIFO (first in first out).
import queue

def search(maze):#fungsi search dengan metode Breadth First Search (BFS)
    path = []#list untuk menyimpan path/jalan dari inisial state menuju goal state
    explored = {}#set node explored
    parent = {}#set parent node
    fringe = queue.Queue()#inisialisasi queue
    start = maze.getStart()#mendapatkan initial state
    goal_state = maze.getObjectives()#mendapatkan list goal state
    fringe.put(start)#menambah elemen ke dalam queue

    while(fringe.empty() == False):#looping selama fringe tidak kosong
        current = fringe.get()#Remove dan return suatu item dari queue. jika queue kosong, tunggu sampai ada item yang baru/tersedia.
        if(current in goal_state):#cek apakah current state itu adalah goal
            path.append(current)#current ditambahkan ke path
            while (current != start):#looping hingga ke initial state
                path.append(parent[current])#tambahkan parent dari curent state ke dalam path
                current = parent[current]#parent dijadikan current state
            path.append(start)#terakhir, tambahkan initial state ke path
            path.reverse()#urutan pathnya dibalik
            return path#kembalikan nilai path dan keluar dari fungsi
        explored[current] = 1;#tandai state telah dieksplor
        neighbors = maze.getNeighbors(current[0], current[1])#ambi nilai teteangga dari state current
        for child in neighbors:#looping sebanyak isi list neighbors
            if(child not in explored):#jika state child belum diekspansi, maka
                explored[child] = 1 #lakukan ekspansi node 
                parent[child] = current
                fringe.put(child)#letakkan child ke dalam fringe
    return path#nilai kembalian, yaitu list path


