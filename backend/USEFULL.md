Cleaning of docker
```
docker system prune
docker rmi $(docker images -f "dangling=true" -q)
docker rmi $(docker images -a -q)
docker rm $(docker ps --filter=status=exited --filter=status=created -q)

```

```
docker run --rm -it -v /home/michael/PycharmProjects/InstAutomize/frontend/:/code node:14.3.0-alpine /bin/sh
```

Change permissions

```bash
sudo chown -R $USER:$USER .
```

Making script executable
```bash
sudo chmod +x backend/backend/scripts/start.dev.sh
```

Removing of docker-compose session
```bash
docker-compose -f docker-compose.dev.yml down -v --remove-orphans
```

Start of docker-compose session
```bash
docker-compose -f docker-compose.dev.yml up --build
```



Entering to server console
```bash
docker exec -it server /bin/sh
```
