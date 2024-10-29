FROM postgres:latest

ENV POSTGRES_USER admin_mlflow
ENV POSTGRES_PASSWORD mlflow_postgres_password
ENV POSTGRES_DB mlflow_database

EXPOSE 5432

# Команды для сборки и запуска контейнера:
# docker build -t my_postgres_image .
# docker run -d --name my_postgres_container -p 5432:5432 my_postgres_image

# Остановите существующий контейнер:  docker stop my_postgres_container
# Удалите существующий контейнер: docker rm my_postgres_container
