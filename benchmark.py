#!/usr/bin/env python

import multiprocessing as mp
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import time
from itertools import repeat

def do_kmeans(n_samples):
    """KMeans clustering on generated data"""

    X,_ = make_blobs(n_samples, centers=3, n_features=10,
                random_state=0)
    kmeans = KMeans(n_clusters=3)
    t0 = time.time()
    kmeans.fit(X)
    print(f"KMeans cluster fit in {time.time()-t0}")

def main():
    """Run Everything"""

    work = []
    count = mp.cpu_count()  #limit parallelization to cores
    work.extend(repeat(100000, count))
    t0 = time.time()
    with mp.Pool(count) as p:
        p.map(do_kmeans, work)
    total = time.time()-t0    
    print(f"Performed {count} KMeans in total time: {total}")
    print(f"Kmeans/sec:  {count/total}")
if __name__ == "__main__":
    main()