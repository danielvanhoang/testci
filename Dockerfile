FROM python:3.10.0b1-slim-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip install honeycomb-beeline
RUN pip install -U setuptools
COPY app.py /app
COPY ascii /app/ascii
COPY lyrics /app/lyrics
COPY templates /app/templates
RUN mkdir /app/static
COPY doge-compiled.js /app/static/doge-compiled.js
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]