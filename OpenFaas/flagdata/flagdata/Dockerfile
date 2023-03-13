FROM ghcr.io/openfaas/classic-watchdog:0.2.1 as watchdog

FROM centos:8

RUN sed -i -e "s|mirrorlist=|#mirrorlist=|g" /etc/yum.repos.d/CentOS-*
RUN sed -i -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-*
RUN dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
RUN yum -y update && yum -y upgrade

RUN yum -y install ImageMagick ImageMagick-devel ImageMagick-perl
RUN yum -y  install xorg-x11-server-Xvfb 
RUN	yum -y install compat-libgfortran-48 
RUN	yum -y install libnsl 
RUN	yum -y install libcanberra-gtk2
RUN	yum -y install python36-devel
RUN	yum -y install openmpi-devel
RUN	yum -y install mpich-devel 
RUN dnf -y install python3
RUN	yum -y install git wget shadow-utils

RUN mkdir /casa/
WORKDIR /casa/
RUN wget https://alma-dl.mtk.nao.ac.jp/ftp/casa/distro/casa/release/rhel/casa-6.5.0-15-py3.8.tar.xz 
RUN tar -xf casa-6.5.0-15-py3.8.tar.xz
ENV PATH="/casa/casa-6.5.0-15-py3.8/bin/:$PATH"

RUN mkdir -p /function/handler
RUN mkdir -p /home/app

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# Add non root user
RUN adduser app && usermod -a -G app app

WORKDIR /home/app
COPY index.py           .
RUN chown -R app /home/app && \
  mkdir -p /home/app/python && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/

USER root

COPY handler.py .

# Allow any user-id for OpenShift users.
RUN chown -R app:app ./ && \
  chmod -R 777 /home/app/python

USER app

ENV fprocess="/casa/casa-6.5.0-15-py3.8/bin/python3 index.py"
EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]

