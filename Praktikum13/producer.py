from redis import Redis
from rq import Queue
from tasks import slow_function

# Koneksi ke Redis lokal
redis_conn = Redis()
q = Queue(connection=redis_conn)

# Mengirim 2 tugas ke antrean secara asinkron
job1 = q.enqueue(slow_function, 5)
job2 = q.enqueue(slow_function, 2)

print(f"Task dikirim. Job 1 ID: {job1.id}")
print(f"Task dikirim. Job 2 ID: {job2.id}")
