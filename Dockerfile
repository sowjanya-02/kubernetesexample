FROM python:3.7
RUN mkdir /sampleapp
WORKDIR /sampleapp
ADD . /sampleapp/
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "/sampleapp/app.py"]
