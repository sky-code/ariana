# Ariana tasks.

.PHONY: install-dev
install-dev:
	@pip install -U -r requirements/local.txt

.PHONY: d-up
d-up:
	@docker-compose up $(FLAGS)

.PHONY: d-stop
d-stop:
	@docker-compose stop $(FLAGS)

.PHONY: d-build
d-build:
	@docker-compose build $(FLAGS)

.PHONY: d-rebuild
d-rebuild:
	@docker-compose build --no-cache $(FLAGS)

.PHONY: d-portainer
d-portainer:
	@docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer

.PHONY: dev
dev:
	HOST=0.0.0.0 npm run dev --silent -- $(FLAGS)

.PHONY: runserver
runserver:
	@python manage.py runserver
