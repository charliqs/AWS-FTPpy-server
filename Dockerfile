FROM python:3.9

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN pip install --no-cache-dir pyftpdlib

EXPOSE 21
EXPOSE 30000-30010

ENV NAME Test

CMD ["python", "ftpserver.py"]

#Comando que funciona para ejectur: docker run -d   -p 21:21   -p 30000-30010:30000-30010   --name ftp 7f9f9553c554