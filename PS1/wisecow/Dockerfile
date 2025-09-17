FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/games:${PATH}"

WORKDIR /app

# Enable universe repository and install prerequisites
RUN apt-get update \
  && apt-get install -y software-properties-common \
  && add-apt-repository universe \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
     cowsay fortune-mod fortunes netcat-openbsd curl ca-certificates \
  && rm -rf /var/lib/apt/lists/*

COPY wisecow.sh /app/wisecow.sh

RUN sed -i 's/\r$//' /app/wisecow.sh && chmod +x /app/wisecow.sh

EXPOSE 4499

CMD ["/app/wisecow.sh"]
