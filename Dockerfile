FROM python:alpine
WORKDIR /app
COPY python-monitor-url.py /app
COPY requirements.txt /app
RUN cd /app && pip install -r requirements.txt
EXPOSE 8001
CMD ["python", "/app/python-monitor-url.py"]
