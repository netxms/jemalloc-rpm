FROM rockylinux:9.3

RUN dnf install -y epel-release && dnf install -y mock git

VOLUME /build
VOLUME /result

COPY build.sh /
WORKDIR /build

CMD ["/build.sh"]
