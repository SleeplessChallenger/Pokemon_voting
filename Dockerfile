FROM python:3
WORKDIR /app
EXPOSE 8000
ADD . . 
RUN pip install -r requirements.txt
RUN pip install python-dotenv
COPY . .
ENTRYPOINT ["python3"]
CMD ["run.py"]