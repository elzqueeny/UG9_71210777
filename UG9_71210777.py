class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority  # 1 (tertinggi), 2, 3, 4, ...
        self._next = None


class PriorityQueueUnsorted:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def __len__(self):
        return self._size

    def add(self, data, priority):
        baru = Node(data, priority)
        if self.is_empty():  # kosong
            self._head = baru
            self._tail = baru
        else:  # insert belakang
            self._tail._next = baru
            self._tail = baru
        self._size = self._size + 1

    def remove(self):  # implementasi ini tidak return
        if self.is_empty() == False:
            if self._size == 1:
                helper = self._head
                self._head = None
                self._tail = None
                del helper
            else:
                # ambil prioritas pada head sebagai prioritas tertinggi yang diketahui
                min_priority = self._head._priority
                # cek dari head sampai tail, berapa prioritas tertinggi
                hapus = self._head
                while hapus != None:
                    if hapus._priority < min_priority:
                        min_priority = hapus._priority
                    hapus = hapus._next
                # prioritas tertinggi sudah diketahui, letakkan hapus di node tersebut
                hapus = self._head
                while hapus._priority != min_priority:
                    hapus = hapus._next
                # cek yang akan dihapus itu head, tail, atau tengah?
                if hapus == self._head:
                    # hapus head
                    self._head = self._head._next
                    del hapus
                else:
                    # hapus tail atau tengah caranya sama saja
                    # letakkan helper di posisi sebelum hapus
                    helper = self._head
                    while helper._next != hapus:
                        helper = helper._next
                    # hapus node
                    helper._next = hapus._next
                    del hapus
                    # pastikan tail di posisi paling belakang
                    self._tail = self._head
                    while self._tail._next != None:
                        self._tail = self._tail._next
        self._size = self._size - 1

    def peek(self):  # return dalam bentuk tuple (data, priority)
        if self.is_empty() == True:
            return None
        else:
            if self._size == 1:
                return tuple([self._head._data, self._head._priority])
            else:
                min_priority = self._head._priority
                helper = self._head
                # cari nilai prioritas tertinggi
                while helper != None:
                    if helper._priority < min_priority:
                        min_priority = helper._priority
                    helper = helper._next
                # nilai prioritas tertinggi sudah diketahui,
                # ambil nilai dan prioritas dari node tersebut
                helper = self._head
                while helper._priority != min_priority:
                    helper = helper._next
                return tuple([helper._data, helper._priority])

    def print_all(self):
        if self.is_empty() == True:
            print('Priority Queue is empty')
        else:
            print("=== List Sorted Queue ===")
            helper = self._head
            while helper != None:
                print(helper._priority, "=", helper._data)
                helper = helper._next
        print()

    def ubahBersama(self, prio, namaBaru):  # untuk mengubah data secara sekaligus
        if self.is_empty() == False:
            helper = self._head
            while (helper != None):
                if helper._priority == prio:
                    helper._data = namaBaru
                helper = helper._next

    # untuk menghapus data priority terkecil sekaligus
    def removePrioSekaligus(self):
        min_prio = self.peek()
        while min_prio[1] == self.peek()[1]:
            self.remove()

    def fungsiTambahan(self):  # Anda dapat membuat fungsi tambahan jika dibutuhkan
        pass
        # tulis kode Anda di sini


myQueue = PriorityQueueUnsorted()
myQueue.add("Dedi", 4)
myQueue.add("Sindu", 2)
myQueue.add("Haniif", 5)
myQueue.add("Farel", 2)
myQueue.add("Beatrix", 3)
myQueue.add("Shalom", 3)
myQueue.add("Harris", 2)
myQueue.print_all()

myQueue.ubahBersama(2, "Mahasiswa A")
myQueue.print_all()

myQueue.removePrioSekaligus()
myQueue.print_all()

myQueue.removePrioSekaligus()
myQueue.print_all()
