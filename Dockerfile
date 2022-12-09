FROM python:3.10

# 
WORKDIR /TST_Milestone1

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./* /TST_Milestone1

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]