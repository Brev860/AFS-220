FROM python:3.8-alpine


ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /var/www/html/capstone/requirements.txt
# Requirements to run uWSGI server
# Items placed after .tmp are stored in a .tmp file to be removed further down
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# Installs requirements listed in requirements.txt
RUN pip install -r /var/www/html/capstone/requirements.txt
# removes .tmp file, because those items are installed so the packages are no longer needed
RUN apk del .tmp
# This section below is an attempt to get apache with wsg installed
RUN apk -qq update
RUN apk add apache2
# RUN pip install mod-wsgi
# This section above is an attempt to get apache with wsg installed
# Website vital to apache installation / setup https://wiki.alpinelinux.org/wiki/Apache
RUN mkdir /capstone
COPY ./var/www/html/capstone /var/www/html/capstone
WORKDIR /var/www/html/capstone
COPY ./scripts /scripts
# chmod +x makes whatever comes after executable
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
# Creates new user; aka not the root user
RUN adduser -D user
# Sets owner of vol dir to this new user. This creates permissions
RUN chown -R user:user /vol
# 755 means user has full access. Everyone else has read only access.
RUN chmod -R 755 /vol/web
# This switches the user from root to the user previously created.
USER user

CMD ["entrypoint.sh", "rc-service apache2 start"]
