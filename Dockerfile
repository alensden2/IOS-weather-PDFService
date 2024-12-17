FROM ubuntu
RUN apt update
RUN apt install python3-pip -y
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "flask", "run" ]