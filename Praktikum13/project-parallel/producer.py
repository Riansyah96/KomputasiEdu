import time
from redis import Redis
from rq import Queue

# Menghubungkan ke service redis-server di docker [cite: 29]
redis_conn = Redis(host='redis-server', port=6379)
q = Queue(connection=redis_conn)

def main():
    urls = [
        "https://www.google.com", "https://www.github.com", "https://www.wikipedia.org",
        "https://www.python.org", "https://www.reddit.com", "https://www.kompas.com",
        "https://www.detik.com", "https://www.stackoverflow.com", "https://www.medium.com",
        "https://www.bbc.com", "https://www.nytimes.com", "https://www.cnn.com",
        "https://www.microsoft.com", "https://www.apple.com", "https://www.amazon.com",
        "https://www.facebook.com", "https://www.instagram.com", "https://www.linkedin.com",
        "https://www.idntimes.com", "https://www.kaskus.co.id"
    ]
    
    print(f"Mengirim {len(urls)} tugas scraping ke antrean...")
    jobs = [q.enqueue('bg_jobs.get_web_title', url) for url in urls]
    
    print("Tugas terdistribusi. Menunggu hasil...\n")
    completed_ids = set()
    while len(completed_ids) < len(jobs):
        for job in jobs:
            if job.is_finished and job.id not in completed_ids:
                print(f"[HASIL] {job.result}")
                completed_ids.add(job.id)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
