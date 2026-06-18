FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY src ./src
COPY scripts ./scripts
RUN npm run build

FROM node:20-alpine AS runtime

WORKDIR /app

RUN addgroup -S api && adduser -S api -G api

COPY package*.json ./
RUN npm ci --omit=dev && npm cache clean --force

COPY --from=build /app/dist ./dist

ENV NODE_ENV=production
ENV PORT=3000

USER api
EXPOSE 3000

CMD ["node", "dist/server.js"]
