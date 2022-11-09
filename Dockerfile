FROM python:3

WORKDIR /usr/src/app
RUN mkdir module

COPY module/* ./module/

COPY main.py ./
COPY config.ini ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]