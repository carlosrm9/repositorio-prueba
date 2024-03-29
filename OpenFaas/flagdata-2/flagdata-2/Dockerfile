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

RUN mkdir /script
RUN mkdir /data
COPY flagdata.py /script

RUN mkdir -p /home/app

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# Add non root user
RUN adduser app && usermod -a -G app app
RUN chown app /home/app

WORKDIR /home/app

USER app

# Populate example here - i.e. "cat", "sha512sum" or "node index.js"
ENV fprocess="/casa/casa-6.5.0-15-py3.8/bin/python3 /script/flagdata.py"
# Set to true to see request in function logs
ENV write_debug="false"

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
