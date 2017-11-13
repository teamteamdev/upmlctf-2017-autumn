FROM alpine:3.5

COPY home /home

RUN apk --update add openssh bash \
  && addgroup -g 1000 ilya \
  && adduser -S -h /home -s /bin/bash -g "" -G ilya ilya \
  && echo "ilya:BAeyj43twqpohmh34WEwaYG34Yyw" | chpasswd \
  && sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config \
  && sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config \
  && sed -i 's/#UsePAM no/UsePAM yes/' /etc/ssh/sshd_config \
  && ssh-keygen -A \
  && chown -R ilya:ilya /home/ \
  && chmod 555 /home/ \
  && chmod 555 /home/.ssh/ \
  && chmod 444 /home/.bash_history \
  && chmod 444 /home/.ssh/authorized_keys

COPY motd /etc/motd

CMD ["bash", "-c", "exec /usr/sbin/sshd -D -e \"$@\""]

EXPOSE 22

