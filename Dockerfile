FROM python:3.9.17-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 9000
CMD python ./app.py