##########################################################
#   Dockerfile (RestAPI)
#   
#   Este es un archivo desarrollado para la empresa
#   RT4 y su uso y distribución esta limitada a las 
#   condiciones propuestas por la empresa.
#
#   Copryrigth: 2024-2025
##########################################################
FROM python:3.12-slim

### Varnames
ARG WORKPATH=/opt/FastAPI/src

### Copy files
WORKDIR ${WORKPATH}
COPY requirements.txt ./
COPY . ./

### Create user
# RUN useradd FastUser
# USER FastUser

### Pipeline
RUN pip install --no-cache-dir -r ${WORKPATH}/requirements.txt
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
