FROM python:3.6-slim

# install python packages
COPY ./requirements.txt /api/requirements.txt
RUN pip install \
        --no-cache-dir \
        -r /api/requirements.txt

# copy source code
COPY . /api
WORKDIR /api

# expose the app port
EXPOSE 5000

# run the app server with gunicorn
ENTRYPOINT ["gunicorn"]
CMD ["-w", "1", "-b", ":5000", "wsgi:application"]
