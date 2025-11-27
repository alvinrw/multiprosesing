import time
import re
from collections import Counter
from multiprocessing import Pool, cpu_count
import os

def clean_text(text):
    # Menghapus karakter non-alfabet dan mengubah ke lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    return text

def count_words_serial(filename):
    print("=" * 60)
    print("METODE SERIAL")
    print("=" * 60)
    
    start_time = time.time()
    
    # Membaca file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Membersihkan teks
    clean = clean_text(text)
    
    # Memisahkan kata-kata
    words = clean.split()
    
    # Menghitung frekuensi kata
    word_count = Counter(words)
    
    # Mengambil 20 kata teratas
    top_20 = word_count.most_common(20)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return top_20, execution_time

def process_chunk(chunk):
    clean = clean_text(chunk) #berishin teks
    words = clean.split() #memecah kata
    return Counter(words)

def count_words_parallel(filename, num_processes=None):
    print("\n" + "=" * 60)
    print("METODE PARALEL")
    print("=" * 60)
    
    if num_processes is None: #pakai semua cpu yang tersedia
        num_processes = cpu_count()
    
    print(f"Menggunakan {num_processes} proses")
    
    start_time = time.time()
    
    # Membaca file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Membagi teks menjadi chunk
    chunk_size = len(text) // num_processes #ukuran tiap chunk
    chunks = []
    
    for i in range(num_processes):#membuat chunk paham kalau semua kata harus di eksekusi
        start = i * chunk_size
        if i == num_processes - 1:
            end = len(text)
        else:
            end = (i + 1) * chunk_size
        chunks.append(text[start:end])
    
    # Memproses chunk secara paralel
    with Pool(processes=num_processes) as pool:
        counters = pool.map(process_chunk, chunks) #menghitung kata di tiap chunk pakai Fungsi map
    
    # Menggabungkan hasil dari semua proses
    total_counter = Counter()
    for counter in counters:
        total_counter.update(counter)
    
    # Mengambil 20 kata teratas
    top_20 = total_counter.most_common(20)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    return top_20, execution_time

def display_results(top_20, execution_time, method):
    print(f"\n20 Kata yang Paling Sering Muncul ({method}):")
    print("-" * 60)
    print(f"{'No':<5} {'Kata':<20} {'Frekuensi':<15}")
    print("-" * 60)
    
    for idx, (word, count) in enumerate(top_20, 1):
        print(f"{idx:<5} {word:<20} {count:<15}")
    
    print("-" * 60)
    print(f"Waktu Eksekusi: {execution_time:.6f} detik")
    print("=" * 60)

def main():
    filename = 'data.txt'

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' tidak ditemukan!")
        print("Pastikan file data.txt berada dalam folder yang sama dengan program ini.")
        return
    
    print("\n" + "=" * 60)
    print("PROGRAM PENGHITUNG FREKUENSI KATA")
    print("=" * 60)
    print(f"File: {filename}")
    print(f"Jumlah CPU: {cpu_count()}")
    print("=" * 60)
    
    # Metode Serial
    top_20_serial, time_serial = count_words_serial(filename)
    display_results(top_20_serial, time_serial, "Serial")
    
    # Metode Paralel
    top_20_parallel, time_parallel = count_words_parallel(filename)
    display_results(top_20_parallel, time_parallel, "Paralel")
    
    # Perbandingan
    print("\n" + "=" * 60)
    print("PERBANDINGAN PERFORMA")
    print("=" * 60)
    print(f"Waktu Serial:   {time_serial:.6f} detik")
    print(f"Waktu Paralel:  {time_parallel:.6f} detik")
    
    if time_serial > time_parallel:
        speedup = time_serial / time_parallel
        print(f"Speedup:        {speedup:.2f}x lebih cepat")
        improvement = ((time_serial - time_parallel) / time_serial) * 100
        print(f"Peningkatan:    {improvement:.2f}% lebih cepat")
    else:
        print("Catatan: Untuk file kecil, overhead paralel bisa lebih lambat")
    print("=" * 60)

if __name__ == "__main__":
    main()