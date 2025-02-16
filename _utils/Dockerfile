FROM ruby:alpine

RUN apk add --no-cache make gcc g++ libc-dev openssl-dev

EXPOSE 4000

ENV GEM_HOME="/usr/local/bundle"
ENV BUNDLE_PATH=/usr/local/bundle BUNDLE_SILENCE_ROOT_WARNING=1 BUNDLE_APP_CONFIG=/usr/local/bundle
ENV PATH=/usr/local/bundle/bin:/usr/local/bundle/gems/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN mkdir -p "/usr/local/bundle"

VOLUME ["/srv/jekyll", "/usr/local/bundle"]

WORKDIR "/srv/jekyll"
ENTRYPOINT ["/bin/sh", "-c", "bundle install && bundle exec jekyll server --incremental --trace --host 0.0.0.0"]
