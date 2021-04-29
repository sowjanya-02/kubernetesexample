FROM python:3.7
RUN mkdir /sampleapp
WORKDIR /sampleapp
ADD . /sampleapp/
RUN pip install flask

EXPOSE 8000
CMD ["python", "/sampleapp/app.py"]
