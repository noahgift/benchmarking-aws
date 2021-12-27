install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W0632 benchmark.py

benchmark-kmeans:
	./benchmark.py