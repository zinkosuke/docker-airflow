# docker-airflow
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fzinkosuke%2Fdocker-airflow.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fzinkosuke%2Fdocker-airflow?ref=badge_shield)

## Usage
```
docker-compose build --no-cache --force-rm init
docker-compose up

docker-compose exec -u root scheduler ./scripts/init.sh
Password: xxx
Repeat for confirmation: xxx
```


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fzinkosuke%2Fdocker-airflow.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fzinkosuke%2Fdocker-airflow?ref=badge_large)