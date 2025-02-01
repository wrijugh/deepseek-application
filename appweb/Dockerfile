# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . .

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     software-properties-common \
#     && rm -rf /var/lib/apt/lists/*

RUN pip3 install python-dotenv streamlit azure-ai-inference

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "dseekweb.py", "--server.port=8501", "--server.address=0.0.0.0"]