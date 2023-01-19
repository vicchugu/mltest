FROM python:3.8.0

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]