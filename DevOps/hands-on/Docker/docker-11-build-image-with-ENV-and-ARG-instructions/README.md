# Hands-on Docker-11: Build images with ENV and ARG instructions

The purpose of this hands-on training is to give the students an understanding of ENV and ARG instructions in Dockerfile

## Learning Outcomes

- At the end of this hands-on training, students will be able to;

- Learn `ENV` form and `ARG` instruction. 

- Build images with ENV` form and `ARG` instruction.

## Outline

- Part 1 - Create an image for publishing a web page from the nginx image

- Part 2 - Create an image with `ENV` instructions for publishing a web page from an nginx image

- Part 3 - Create an image with `ARG` instructions for publishing a web page from the nginx image

## Part 1 - Create an image for publishing a web page from the nginx image

- Create a folder and name it myweb.

```bash
mkdir myweb && cd myweb
```

- In myweb folder, create another folder named myweb-nginx.

```bash
mkdir myweb-nginx && cd myweb-nginx
```

- Create an index.html file.

```bash
echo "<h1>Welcome to Ondia<h1>" > index.html
```

- Create a Dockerfile and input the following statements.

```txt
FROM nginx:alpine
COPY . /usr/share/nginx/html
```

- Build an image from this Dockerfile.

```bash
docker build -t <userName>/myweb:nginx .
```

- Run this image and check the result in your browser.

```bash
docker run --name myweb -dp 80:80 <userName>/myweb:nginx
```

- Remove the container

```bash
docker container rm -f myweb
```

## Part 2 - Create an image with `ENV` instruction for publishing a web page from the nginx image

- In myweb folder, create another folder named myweb-env.

```bash
cd ..
mkdir myweb-env && cd myweb-env
```

- Create a myweb.html file and input fthe ollowing statements. Pay attention to `COLOR` statement. We will change the background color with `env`.

```txt
<html>
<head>
<title>myweb</title>
</head>
<body style="background-color:COLOR;">
<h1>Welcome to Ondia<h1>
</body>
</html>
```

- Create a Dockerfile and input the following statements.

```txt
FROM nginx:latest
ENV COLOR="red"
RUN apt-get update ; apt-get install curl -y
WORKDIR /usr/share/nginx/html
COPY . /usr/share/nginx/html
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost/ || exit 1
CMD sed -e s/COLOR/"$COLOR"/ myweb.html > index.html ; rm myweb.html ; nginx -g 'daemon off;'
```

- Build an image from this Dockerfile.

```bash
docker build -t <userName>/myweb:env .
```

- Run this image without the environment variable and see in the browser that the background is red.

```bash
docker run --name myweb-env -dp 80:80 <userName>/myweb:env
```

- Run the same image with the environment variable (for example, blue) and see in the browser that the background is blue.

```bash
docker run --name myweb-blue --env COLOR=blue -dp 81:80 <userName>/myweb:env
```

- Remove all containers.

```bash
docker rm -f $(docker ps -aq)
```

## Part 3 - Create an image with `ARG` instruction for publishing a web page from the nginx image

- In myweb folder, create another folder named myweb-arg.

```bash
cd ..
mkdir myweb-arg && cd myweb-arg
```

- Create a myweb.html file and input the following statements. Pay attention to `COLOR` statement. We will change the background color with `ARG` instructions during the build phase.

```txt
<html>
<head>
<title>myweb</title>
</head>
<body style="background-color:COLOR;">
<h1>Welcome to Ondia<h1>
</body>
</html>
```

- Create a Dockerfile and input the following statements.

```txt
FROM nginx:latest
ARG COLOR="pink"
RUN apt-get update ; apt-get install curl -y
WORKDIR /usr/share/nginx/html
COPY . /usr/share/nginx/html
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost/ || exit 1
RUN sed -e s/COLOR/"$COLOR"/ myweb.html > index.html ; rm myweb.html
CMD  nginx -g 'daemon off;'
```

- Build an image from this Dockerfile.

```bash
docker build -t <userName>/myweb:arg .
```

- Run this image and see in the browser that the background is pink.

```bash
docker run --name myweb-arg -dp 80:80 <userName>/myweb:arg
```

- Build an image from this Dockerfile with `build-arg` variable.

```bash
docker build -t <userName>/myweb:arg-gray --build-arg COLOR=gray .
```

- Run this image and see in the browser that the background is gray.

```bash
docker run --name myweb-arg-gray -dp 81:80 <userName>/myweb:arg-gray
```

- Remove all containers.

```bash
docker rm -f $(docker ps -aq)
```
