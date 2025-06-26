# Hands-on Docker-04 : Docker Networking

The purpose of this hands-on training is to give the student an understanding of networking in Docker.

## Learning Outcomes

At the end of this hands-on training, students will be able to;

- List available networks in Docker.

- Create a network in Docker.

- Inspect properties of a network in Docker.

- Connect a container to a network.

- Explain the default network bridge configuration.

- Configure a user-defined network bridge.

- Ping containers within the same network.

- Can bind containers to specific ports.

- Delete Docker networks.

## Outline

- Part 1 - Launch a Docker Machine Instance and Connect with SSH

- Part 2 - Default Network Bridge in Docker

- Part 3 - User-defined Network Bridge in Docker

- Part 4 - Container Networking

## Part 1 - Launch a Docker Machine Instance and Connect with SSH

- Launch a Docker machine on Amazon Linux 2023 AMI with a security group allowing SSH connections using the [Cloudformation Template for Docker Machine Installation](../docker-01-installing-on-ec2-linux2/docker-installation-template.yml).

- Connect to your instance with SSH.

```bash
ssh -i .ssh/mykey.pem ec2-user@ec2-3-133-106-98.us-east-2.compute.amazonaws.com
```

## Part 2 - Default Network Bridge in Docker

- Check if the docker service is up and running.

```bash
systemctl status docker
```

- List all networks available in Docker, and explain the types of networks.

```bash
docker network ls
```

- Run two `alpine` containers with an interactive shell, in detached mode, name the containers as `mycont1` and `mycont2`, and add a command to run Alpine shell. Here, explain what the detached mode means.

```bash
docker container run -dit --name mycont1 alpine ash
docker container run -dit --name mycont2 alpine ash
```

- Show the list of running containers on Docker machine.

```bash
docker ps
```

- Show the details of `bridge` network, and explain properties (subnet, IPs) and why containers are in the default network bridge.

```bash
docker network inspect bridge | less
```

- Get the IP of `mycont2` container.

```bash
docker container inspect mycont2 | grep IPAddress
```

- Connect to the `mycont1` container.

```bash
docker exec -it mycont1 sh
```

- Show the details of the network interface configuration of `mycont1` container.

```bash
ifconfig
```

- Open another terminal and connect to your EC2 instance. Show the details of the network interface configuration of ec2 instance. 

```bash
ifconfig
```

- Compare with two configurations.

- In the `mycont1` container, ping google.com four times to check the  internet connection.

```bash
ping -c 4 google.com
```

- Ping `mycont2` container by its IP four times to show the connection.

```bash
ping -c 4 172.17.0.3
```

- Try to ping `mycont2 `container by its name, it should face with bad address. Explain why it failed (due to the default bridge configuration not working with container names)

```bash
ping -c 4 mycont2
```

- Disconnect from `mycont1` without stopping it (CTRL + p + q).

- Stop and delete the containers

```bash
docker container stop mycont1 mycont2
docker container rm mycont1 mycont2
```

## Part 3 - User-defined Network Bridge in Docker

- Create a bridge network `mynet`.

```bash
docker network create --driver bridge mynet
```

- List all networks available in Docker, and show the user-defined `mynet`.

```bash
docker network ls
```

- Show the details of `mynet`, and show that there is no container yet.

```bash
docker network inspect mynet
```

- Run four `alpine` containers with interactive shell, in detached mode, name the containers as `mycont1st`, `mycont2nd`, `mycont3rd`, and `mycont4th`, and adda  command to run Alpine shell. Here, 1st and 2nd containers should be in `mynet`, 3rd container should be in default network bridge, 4th container should be in both `mynet` and default network bridge.

```bash
docker container run -dit --network mynet --name mycont1 alpine ash
docker container run -dit --network mynet --name mycont2 alpine ash
docker container run -dit --name mycont3 alpine ash
docker container run -dit --name mycont4 alpine ash
docker network connect mynet mycont4
```

- List all running containers and show them up and running.

```bash
docker container ls
```

- Show the details of `mynet`, and explain the newly added containers. (1st, 2nd, and 4th containers should be in the list)

```bash
docker network inspect mynet
```

- Show the details of the  default network bridge, and explain the newly added containers. (3rd and 4th containers should be in the list)

```bash
docker network inspect bridge
```

- Connect to the `mycont1` container.

```bash
docker exec -it mycont1 ash
```

- Ping `mycont2` and `mycont4` containers by their names to show that in a user-defined network, container names can be used in networking.

```bash
ping -c 4 mycont2
ping -c 4 mycont4
```

- Try to ping `mycont3` container by its name and IP, should face with a bad address because the 3rd container is on a different network.

```bash
ping -c 4 mycont3
ping -c 4 172.17.0.2
```

- Ping google.com to check the internet connection.

```bash
ping -c 4 google.com
```

- Exit the `mycont1` container without stopping and return to the ec2-user bash shell.

- Connect to the `mycont4` container, since it is in both network should connect all containers.

```bash
docker container exec -it mycont4 ash
```

- Ping `mycont2` and `mycont1` containers by their name, ping `mycont3` container with its IP. Explain why we used IP instead of the name.

```bash
ping -c 4 mycont1
ping -c 4 mycont2
ping -c 4 172.17.0.2
```

- Exit from `mycont4` container. Stop and remove all containers.

```bash
docker container stop mycont1 mycont2 mycont3 mycont4
docker container rm mycont1 mycont2 mycont3 mycont4
```

- Delete `mynet` network

```bash
docker network rm mynet
```

## Part 4 - Container Networking

- Run an `nginx` web server, name the container as `ng`, and bind the web server to host port 8080 command to run Alpine shell. Explain `--rm` and `-p` flags and port binding.

```bash
docker container run --rm -d -p 8080:80 --name ng nginx
```

- Add a security rule for protocol HTTP port 8080 and show that Nginx Web Server is running on Docker Machine.

```text
http://ec2-18-232-70-124.compute-1.amazonaws.com:8080
```

- Stop container `ng`, should be removed automatically due to `--rm` flag.

```bash
docker container stop ng
```

- Run an `nginx` web server, name the container as `my_nginx`, and connect the web server to the host network. 

```bash
docker container run --rm -dit --network host --name my_nginx nginx
```

- Show Nginx Web Server is running on Docker Machine.

```text
http://ec2-18-232-70-124.compute-1.amazonaws.com
```

- Show the details of the network interface configuration of `my_nginx` container.

```bash
docker container exec -it my_nginx sh
apt-get update
apt-get install net-tools
ifconfig
```

- Open another terminal and connect to your EC2 instance. Show the details of the network interface configuration of ec2 instance. 

```bash
ifconfig
```

- Show that two configurations are the same. 

- Exit and stop container `my_nginx`, should be removed automatically due to `--rm` flag.

```bash
docker container stop my_nginx
```

- Run an `alpine` container, name the container as `nullcontainer`, and connect the web server to no network. 

```bash
docker container run --rm -it --network none --name nullcontainer alpine
```

- Show the details of the network interface configuration of `nullcontainer` container.

```bash
ifconfig
```

- Notice that it has only a loopback (localhost) interface.

- Try to ping `google.com`, should face with bad address. Explain why it failed (due to no network configuration)

```bash
ping -c 4 google.com
```

- Exit from container `nullcontainer`, should be removed automatically due to `--rm` flag.
