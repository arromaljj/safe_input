FROM python:3.9
RUN useradd -m -u 1000 user
WORKDIR /mainllm
COPY ./ ./
# COPY ./requirements.txt /mainllm/requirements.txt
RUN pip install --upgrade pip
RUN pip install  --upgrade -r requirements.txt
# COPY ./ ./mainllm
ENV HF_HOME ./.cache
USER user
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "main.py"]


