# KomputasiEdo

mpirun -n 4 python paralel_write.py
untuk menjalankan program dengan multi proses tambahkan **"mpirun -n 4 python"** sebelum nama file python nya 

mpirun -n 8 **--oversubscribe** python read.py
untuk menjalankan program dengan multi proses diatas 4 tambahkan **"--oversubscribe"** dianatara mpirun -n ...(jumlah yang mau dideploy) dan nama file python nya
