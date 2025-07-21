FROM python:3.9-slim
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]