FROM alpine:3.5

COPY home /home

RUN apk --update add openssh bash \
  && adduser -S -h /home -s /bin/bash -g "" run \
  && echo "run:run" | chpasswd \
  && ssh-keygen -A \
  && chown root:root home \
  && chmod 755 /home/flag

COPY motd /etc/motd

CMD ["bash", "-c", "exec /usr/sbin/sshd -D -e \"$@\""]

EXPOSE 22

