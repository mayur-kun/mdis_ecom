FROM python:3.10-slim

WORKDIR /ecomdir
COPY . /ecomdir
EXPOSE 8501
RUN pip install -r requirements.txt
CMD streamlit run app.py