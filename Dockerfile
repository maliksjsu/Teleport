#
# First Flask App Dockerfile
#
#

# Pull base image.
FROM centos:7.0.1406

# Build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel
RUN easy_install pip
RUN mkdir /opt/chef_browser
WORKDIR /opt/chef_browser
ADD requirements.txt /opt/chef_browser/
RUN pip install -r requirements.txt
ADD . /opt/chef_browser

# Define working directory.
WORKDIR /opt/chef_browser

# Define default command.
# CMD ["python", "manage.py", "runserver"]
