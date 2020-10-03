# InstAutomize
Project for automize work in instagram

## Docker

Follow instructions for installing the community edition of docker on [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/) or [Windows](https://docs.docker.com/docker-for-windows/install/).

After you have installed docker, follow the [post-installation steps for linux](https://docs.docker.com/install/linux/linux-postinstall/). This will prevent us from having to use `sudo` when running docker commands.

Finally, install `docker-compose` by following the Linux instructions found [here](https://docs.docker.com/compose/install/#install-compose). (For Windows its probably will be installed with Docker Desktop)

Make sure that docker is correctly configured on your machine by running the following command:

```
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
0e03bdcc26d7: Pull complete 
Digest: sha256:4cf9c47f86df71d48364001ede3a4fcd85ae80ce02ebad74156906caff5378bc
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

If you have used docker previously, you may want to remove any old or unused images. Do this with the following commands: 

```bash
$ docker system prune
$ docker rmi $(docker images -f "dangling=true" -q)
$ docker rmi $(docker images -a -q)
$ docker rm $(docker ps --filter=status=exited --filter=status=created -q)
```
