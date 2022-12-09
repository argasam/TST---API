FROM python:3.10

# 
WORKDIR /TST_Milestone1

# 
COPY . /TST_Milestone1

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]