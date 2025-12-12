# Ambil image Dask resmi sebagai dasarnya (menggunakan Python 3.10)
FROM daskdev/dask:latest

# Instal paket yang dibutuhkan: 
# dask-ml (untuk run_ml.py)
# requests (untuk run_scraping.py)
# scikit-learn (dependensi dask-ml)
RUN pip install --no-cache-dir \
    dask-ml \
    requests \
    scikit-learn
