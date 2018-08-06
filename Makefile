
all:
	python3 service.py

browser:
	open -a safari http://localhost:5000/index.html

clean:
	rm -rf __pycache__

docker-run-redis:
	docker run -p 6379:6379 redis

docker-run-web:
	docker run -p 5000:5000 suggestions

docker-build:
	docker build -t suggestions .

docker-start-stack:
	docker stack deploy -c docker-compose.yml suggestionsapp

docker-stop-stack:
	docker stack rm suggestionsapp


