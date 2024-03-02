FROM python:3.9
RUN useradd -m -u 1000 user
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --upgrade pip
RUN pip install  --upgrade -r requirements.txt
COPY /src /src
USER user
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "main.py"]
# COPY --link --chown=1000 ./ /code

