venv:
	virtualenv venv
	./venv/bin/pip3 install -r requirements.txt

redeploy:
	docker stack rm website
	docker swarm leave --force
	docker swarm init
	docker stack deploy -c docker-compose.yml website
