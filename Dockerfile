FROM python:3
WORKDIR /usr/scr/app1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["python","app.py"]
