# Ariana tasks.

.PHONY: install-dev
install-dev:
	@pip install -U -r requirements/local.txt

.PHONY: d-up
d-up:
	@docker-compose -f local.yml up $(FLAGS)

.PHONY: d-stop
d-stop:
	@docker-compose -f local.yml stop $(FLAGS)

.PHONY: d-build
d-build:
	@docker-compose -f local.yml build $(FLAGS)

.PHONY: d-rebuild
d-rebuild:
	@docker-compose -f local.yml build --no-cache $(FLAGS)

.PHONY: dp-up
dp-up:
	@docker-compose -f production.yml up $(FLAGS)

.PHONY: dp-stop
dp-stop:
	@docker-compose -f production.yml stop $(FLAGS)

.PHONY: dp-build
dp-build:
	@docker-compose -f production.yml build $(FLAGS)

.PHONY: dp-rebuild
dp-rebuild:
	@docker-compose -f production.yml build --no-cache $(FLAGS)


.PHONY: d-portainer
d-portainer:
	@docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer

.PHONY: dev
dev:
	HOST=0.0.0.0 npm run dev --silent -- $(FLAGS)

.PHONY: runserver
runserver:
	@python manage.py runserver
