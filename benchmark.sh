#!/usr/bin/env bash

CPU=`python -c "import multiprocessing as mp;print(f'{mp.cpu_count()}')"`
echo "Running with CPU Count and Threads: " $CPU
sysbench cpu --threads=$CPU run