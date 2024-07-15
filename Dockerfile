FROM python:3.11-alpine

ENV WD_PATH /app
ENV USER_NAME userbot

RUN mkdir ${WD_PATH}
COPY requirements.txt ${WD_PATH}
WORKDIR ${WD_PATH}

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]