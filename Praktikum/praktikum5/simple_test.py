# from mpi4py import MPI
# import sys

# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()

# print(f"Rank {rank}/{size}: MPI berhasil!", flush=True)

# if rank == 0:
#     print("Semua proses berjalan!", flush=True)

from mpi4py import MPI
import sys
import time

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    print(f"DEBUG: Proses {rank} started", flush=True)
    
    if size != 4:
        if rank == 0:
            print("Program ini membutuhkan tepat 4 proses!")
            print("Gunakan: mpiexec -n 4 python circular_message.py")
        return
    
    # Pesan yang akan dikirim
    message = f'Halo dari proses {rank}'
    
    # Tentukan proses sumber dan tujuan
    source = (rank - 1) % size
    dest = (rank + 1) % size
    
    print(f"DEBUG: Rank {rank} source={source} dest={dest}", flush=True)
    
    # Untuk menghindari deadlock, proses dengan rank genap kirim dulu, ganjil terima dulu
    if rank % 2 == 0:
        print(f"DEBUG: Rank {rank} sending to {dest}", flush=True)
        comm.send(message, dest=dest)
        print(f"DEBUG: Rank {rank} waiting receive from {source}", flush=True)
        received_message = comm.recv(source=source)
    else:
        print(f"DEBUG: Rank {rank} waiting receive from {source}", flush=True)
        received_message = comm.recv(source=source)
        print(f"DEBUG: Rank {rank} sending to {dest}", flush=True)
        comm.send(message, dest=dest)
    
    print(f'Proses {rank} menerima pesan: \"{received_message}\" dari proses {source}', flush=True)
    time.sleep(0.1)  # Beri waktu untuk output

if __name__ == "__main__":
    main()