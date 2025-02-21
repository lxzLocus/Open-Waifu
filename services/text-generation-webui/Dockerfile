FROM ubuntu:22.04 AS app_base
RUN apt-get update && apt-get install --no-install-recommends -y \
    git python3-venv python3-pip
RUN pip3 install --upgrade pip setuptools
RUN python3 -m venv /venv
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY ./scripts /scripts
RUN chmod +x /scripts/*
RUN git clone https://github.com/oobabooga/text-generation-webui /src
ARG VERSION_TAG
ENV VERSION_TAG=${VERSION_TAG}
RUN . /scripts/checkout_src_version.sh
RUN cp -ar /src /app
RUN pip3 install -r /app/requirements.txt

FROM app_base AS run_base
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-venv python3-dev git
COPY --from=app_base /app /app
COPY --from=app_base /src /src
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
EXPOSE 7860
ENV PYTHONUNBUFFERED=1
ARG BUILD_DATE
ENV BUILD_DATE=$BUILD_DATE
RUN echo "$BUILD_DATE" > /build_date.txt
ARG VERSION_TAG
ENV VERSION_TAG=$VERSION_TAG
RUN echo "$VERSION_TAG" > /version_tag.txt
COPY ./scripts /scripts
RUN chmod +x /scripts/*
ENTRYPOINT ["/scripts/docker-entrypoint.sh"]