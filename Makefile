install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W0632 benchmark.py

benchmark-kmeans:
	./benchmark.py

benchmark-sysbench:
	./benchmark.sh
	
benchmark-sysbench-amazon:
	#install sysbench
	curl -s https://packagecloud.io/install/repositories/akopytov/sysbench/script.rpm.sh | sudo bash
	sudo yum -y install sysbench
	#run CPU benchmark
	./benchmark.sh
