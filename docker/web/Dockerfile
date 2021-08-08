# Запекать или нет код из app в image.
# В зависимости от BUILD_VERSION (app или env) для финальной сборки будет использован
# либо build-env, либо build-app (версия с запеченым кодом из app)
# example: build --build-arg BUILD_VERSION=env
ARG BUILD_VERSION="env"
FROM python:3.8.8-alpine as base

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/lib/python3.8/site-packages

ENV DATABASE=postgres

RUN apk update && \
apk --no-cache add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev py3-numpy py3-pandas && \
update-ca-certificates

# Для сброса кэша перед выполнением pip install $(cat requirements.txt
# example: build --build-arg CACHEBUST=$(date +%s)
ARG CACHEBUST=1

FROM base as build-env
COPY ./app/requirements.txt .
RUN pip install --upgrade pip && \
pip install --ignore-installed $(cat requirements.txt | grep -v -e pandas -e numpy)

# Стадия запекания кода. Применяется ниже при build --build-arg BUILD_VERSION=app
FROM build-env as build-app
COPY ./app .

FROM build-${BUILD_VERSION} AS final
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
