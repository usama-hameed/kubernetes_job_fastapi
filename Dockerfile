FROM python:latest
COPY job.py /app/job.py
WORKDIR /app
CMD ["python", "job.py"]
