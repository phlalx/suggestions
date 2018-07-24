
all:
	python3 service.py

browser:
	open -a safari http://localhost:5000/static/index.html

clean:
	rm -rf __pycache__

docker-run-redis:
	docker run -p 6379:6379 redis

docker-build:
	docker build -t suggestions .

docker-run:
	docker run -p 5000:5000 suggestions

