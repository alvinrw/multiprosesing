# Word Frequency Counter: Serial vs Parallel Processing (Python multiprocessing)

### Assignment for Parallel Computing – Computer Engineering, Universitas Brawijaya (UB), 2025

This project demonstrates the performance comparison between serial and parallel processing in Python by counting the most frequent words in a text file. It is created to fulfill the Parallel Computing course assignment for Computer Engineering, Universitas Brawijaya (UB), 2025.

## Project Overview

The program reads a text file (`data.txt`), cleans the text, counts word frequencies, and displays the top 20 most frequent words. Two methods are implemented:

1. **Serial Method** – Processes the entire text using a single CPU core.
2. **Parallel Method** – Splits the text into chunks and uses multiple CPU cores via the `multiprocessing` module.

The execution times are compared to observe performance improvements when using multiprocessing.

## Project Structure

```
project-folder/
│
├── data.txt            # Input text file for analysis
├── main.py             # Main word-counting program
└── README.md           # Documentation
```

## How It Works

### 1. Text Cleaning

The program removes non-alphabetic characters and converts the text to lowercase.

### 2. Serial Counting

The program reads the entire text, splits it into words, and counts their frequency using Python's `Counter`.

### 3. Parallel Counting

* The text is split into multiple chunks based on the number of CPU cores.
* Each chunk is processed by a separate process using multiprocessing.
* The word frequencies from each process are combined into one final result.

## How to Run

1. Ensure `data.txt` is in the same folder as the Python script.
2. Run the program:

```
python main.py
```

3. The program will display:

* Top 20 most frequent words (serial & parallel)
* Execution time of each method
* Performance comparison (speedup & improvement percentage)

## Output Example

```
============================================================
PROGRAM PENGHITUNG FREKUENSI KATA
============================================================
File: data.txt
Jumlah CPU: 8
============================================================

20 Kata yang Paling Sering Muncul (Serial):
...

20 Kata yang Paling Sering Muncul (Paralel):
...

============================================================
PERBANDINGAN PERFORMA
============================================================
Waktu Serial:   0.532100 detik
Waktu Paralel:  0.210450 detik
Speedup:        2.53x lebih cepat
Peningkatan:    60.47% lebih cepat
============================================================
```

## Concepts Demonstrated

* Parallel processing
* CPU core utilization
* Workload splitting
* Performance benchmarking
* Text processing and cleaning

## Requirements

* Python 3.8 or higher
* Built-in modules: `multiprocessing`, `collections`, `re`

## Notes

* Parallel execution gives more benefits on larger datasets.
* Small files may run slower in parallel due to multiprocessing overhead.
* This documentation and program are prepared specifically for the Parallel Computing course assignment (Teknik Komputer UB, 2025).
