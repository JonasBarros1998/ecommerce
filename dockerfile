FROM python
COPY . /Code
WORKDIR /Code
RUN pip install -r requirements.txt
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
EXPOSE 8000