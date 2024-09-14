# teebot-app/Dockerfile
FROM python:3.12-slim

### Varnames
ARG WORKPATH=/opt/Teebot/src

### Copy files
WORKDIR ${WORKPATH}
COPY requirements.txt ./
COPY . ./

### Create user
# RUN useradd TeebotUser
# USER TeebotUser

### Pipeline
RUN pip install --no-cache-dir -r ${WORKPATH}/requirements.txt
EXPOSE 8001

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
