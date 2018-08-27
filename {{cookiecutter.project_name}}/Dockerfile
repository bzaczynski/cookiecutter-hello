# Build a new Docker image:
# $ docker build -t {{ cookiecutter.project_name }} -f Dockerfile .

# Run a temporary Docker container to extract PEX file from:
# $ docker run --rm {{ cookiecutter.project_name }} cat /root/{{ cookiecutter.project_name }}.pex > {{ cookiecutter.project_name }}.pex

FROM python:3.7.0-alpine3.8

WORKDIR /root
COPY . /root

RUN pip install "setuptools<34.0,>=20.3" pex . \
 && python setup.py bdist_wheel \
 && pex {{ cookiecutter.project_name }} -f dist -r requirements.txt -c {{ cookiecutter.project_name }}_script.py -o {{ cookiecutter.project_name }}.pex
