FROM node:20.14.0

WORKDIR /app/frontend

COPY ./package.json .

RUN npm i

COPY . .

CMD [ "npm", "run", "dev" ]