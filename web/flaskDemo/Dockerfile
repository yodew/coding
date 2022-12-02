FROM python:3.9.14-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./app /code/app

CMD ["gunicorn", "app:app", "-c", "./gunicorn.py"]