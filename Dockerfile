FROM python:3.9.17
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python", "app.py"]