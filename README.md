# benchmarking-aws
A repo where I benchmark exotic and ridiculously powerful machines on AWS

## Tools

* [sysbench](https://github.com/akopytov/sysbench)
* [python parallel kmeans](https://github.com/noahgift/benchmarking-aws/blob/main/benchmark.py)

install:

`python3 -m venv ~/.benchmark && source ~/.benchmark/bin/activate && make install`

run: 

`make benchmark-kmeans` 

## Machines

### Github Codespaces 4-core Ubuntu

* Kmeans

```bash
(.venv) @noahgift ➜ /workspaces/benchmarking-aws (main) $ make benchmark-kmeans 
./benchmark.py
KMeans cluster fit in 3.0112905502319336
KMeans cluster fit in 3.0478947162628174
KMeans cluster fit in 3.1041808128356934
KMeans cluster fit in 3.089890718460083
Performed 4 KMeans in total time: 3.303737163543701
Kmeans/sec:  1.2107500693879243
```

* sysbench

```bash
(.venv) @noahgift ➜ /workspaces/benchmarking-aws (main ✗) $ ./benchmark.sh 
Running with CPU Count and Threads:  4
sysbench 1.0.20 (using bundled LuaJIT 2.1.0-beta2)

Running the test with following options:
Number of threads: 4
Initializing random number generator from current time


Prime numbers limit: 10000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:  3397.18

General statistics:
    total time:                          10.0012s
    total number of events:              33981

Latency (ms):
         min:                                    0.83
         avg:                                    1.18
         max:                                   18.46
         95th percentile:                        1.27
         sum:                                39979.04

Threads fairness:
    events (avg/stddev):           8495.2500/94.27
    execution time (avg/stddev):   9.9948/0.00
```


### Macbook Pro (16-inch, 2021), Apple M1 Max, Memory 64GB

* kmeans

```bash
(.benchmark) ➜  benchmarking-aws git:(main) make benchmark-kmeans 
./benchmark.py
KMeans cluster fit in 0.9891571998596191
KMeans cluster fit in 0.9297049045562744
KMeans cluster fit in 0.965522050857544
KMeans cluster fit in 0.9847841262817383
KMeans cluster fit in 0.9845497608184814
KMeans cluster fit in 0.9792351722717285
KMeans cluster fit in 0.986346960067749
KMeans cluster fit in 0.9968240261077881
KMeans cluster fit in 0.97275710105896
KMeans cluster fit in 1.001432180404663
Performed 10 KMeans in total time: 1.4205470085144043
Kmeans/sec:  7.039541768109394
```

* sysbench

```bash
./benchmark.sh
Running with CPU Count and Threads:  10
sysbench 1.0.20 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 10
Initializing random number generator from current time


Prime numbers limit: 10000

Initializing worker threads...

Threads started!

CPU speed:
    events per second: 6801315.33

General statistics:
    total time:                          10.0001s
    total number of events:              68015731

Latency (ms):
         min:                                    0.00
         avg:                                    0.00
         max:                       18446744073709.55
         95th percentile:                        0.00
         sum:                                25764.58

Threads fairness:
    events (avg/stddev):           6801573.1000/54711.67
    execution time (avg/stddev):   2.5765/0.09
```
