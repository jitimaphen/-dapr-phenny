FROM python:3.7-slim-buster
WORKDIR /app
ADD . .

RUN pip install requests
RUN pip install dapr-dev
RUN pip install dapr-ext-grpc-dev
RUN pip install flask
RUN pip install flask_cors

ENTRYPOINT ["python"]
CMD ["app.py"]
