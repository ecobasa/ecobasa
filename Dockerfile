# start from an official image
FROM python:2.7

# getting image ready to compile translations
RUN apt-get update && apt-get install -y gettext libgettextpo-dev

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/ecobasa
WORKDIR /opt/services/ecobasa

# install our dependencies
COPY ./requirements_production.txt /opt/services/ecobasa/requirements.txt
RUN pip install -r requirements.txt

# copy our project code
COPY ./ /opt/services/ecobasa/

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--bind", ":8000", "ecobasa.wsgi:application"]
