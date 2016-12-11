build:
	docker build -t stupschwartz/terse:latest ./terse

push:
	docker push stupschwartz/terse

test:
	docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm acceptance
	docker-compose down
