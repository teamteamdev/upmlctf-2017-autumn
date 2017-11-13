FROM alpine:3.5

COPY . /

RUN apk --update add openssh bash \
  && adduser -S -h /home/user -s /bin/bash -g "" user \
  && adduser -S -h /home/moderator -s /bin/bash -g "" moderator \
  && echo "user:user" | chpasswd \
  && echo "moderator:AHweay42sgWEY" | chpasswd \
  && ssh-keygen -A \
  && chmod -R 511 /home/user \
  && chmod -R 511 /home/moderator \
  && chown user:nogroup /home/user/info.txt \
  && chown moderator:nogroup /home/moderator/flag.txt \
  && chmod -R 444 /Dockerfile

CMD ["bash", "-c", "exec /usr/sbin/sshd -D -e \"$@\""]

EXPOSE 22

