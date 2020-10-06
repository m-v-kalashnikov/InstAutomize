Change permissions

```bash
sudo chown -R $USER:$USER .
```

Making script executable
```bash
sudo chmod +x backend/backend/scripts/start.sh
```

Removing of docker-compose session
```bash
docker-compose -f docker-compose.yml down -v --remove-orphans
```

Start of docker-compose session
```bash
docker-compose -f docker-compose.yml up --build
```

Entering to server console
```bash
docker exec -it server /bin/sh
```
