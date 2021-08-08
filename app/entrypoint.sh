#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
#    echo "Waiting for postgres..."

#    while ! nc -z $DB_HOST $DB_PORT; do
#      sleep 0.1
#    done

#    echo "PostgreSQL started"
#fi

# собираем статику при отключеном DEBUG
[ -z "$DEBUG" ] && python manage.py collectstatic --no-input -c --skip-checks

echo "Run migrations"

python manage.py migrate

echo "Run server"

exec "$@"
