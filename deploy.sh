git pull 
docker stop todoapp
docker rm todoapp
docker build -t todoapp .
docker run -it -d -p 8700:8700 --name todoapp todoapp
docker image prune -f