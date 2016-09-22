FROM mhart/alpine-node:6.4.0

RUN adduser -D app \
  && mkdir -p /client

COPY package.json typedoc.json tsconfig.json tslint.json /client/
COPY src /client/src/
COPY config /client/config/
COPY assets /client/assets/

WORKDIR /client

RUN apk --update add --virtual build-dependencies git \
  && npm install rimraf webpack typescript -g \
  && npm install \
  && apk del build-dependencies \
  && npm run build:prod \
  && chown -R app:app /client

USER app

EXPOSE 8080

CMD ["npm", "run" ,"server:prod"]
#CMD ["npm", "run" ,"server:dev:hmr"]
