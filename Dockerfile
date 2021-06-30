FROM python:alpine
WORKDIR /app
COPY python_monitor_url.py /app
COPY urls.json /app
COPY requirements.txt /app
RUN cd /app && pip install -r requirements.txt
EXPOSE 8001
CMD ["python", "/app/python_monitor_url.py"]
