FROM node:10

ENV HOST 0.0.0.0

WORKDIR /app

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./package.json /app/package.json
COPY ./package-lock.json /app/package-lock.json

RUN npm install

CMD ["npm", "run", "dev"]
