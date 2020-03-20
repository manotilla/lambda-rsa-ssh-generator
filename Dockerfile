FROM amazonlinux

WORKDIR function
COPY lambda_function.py .
RUN yum update -y
RUN yum install -y python3
RUN yum install -y python3-pip
RUN yum install python3-devel
RUN pip3 install awscli

RUN pip3 install --target ./package cryptography
RUN yum install -y zip
RUN cd package && zip -r9 ${OLDPWD}/function.zip .
RUN zip -g function.zip lambda_function.py
