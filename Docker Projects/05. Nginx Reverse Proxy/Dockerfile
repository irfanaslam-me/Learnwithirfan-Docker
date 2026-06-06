FROM node:20-alpine
WORKDIR /app
COPY app/package*.json ./
RUN npm ci --only=production
COPY app/ .
RUN addgroup -S app && adduser -S app -G app
USER app
EXPOSE 3000
CMD ["node", "index.js"]
