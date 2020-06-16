FROM python:3.8.2

WORKDIR /sat

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
