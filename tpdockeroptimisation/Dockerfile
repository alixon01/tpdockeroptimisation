FROM node:latest
WORKDIR /app

# 1) copier uniquement les manifests pour profiter du cache
COPY package*.json ./

# 2) install reproductible (lockfile présent)
RUN npm ci

# 3) copier le reste du code
COPY . .

ENV NODE_ENV=development
EXPOSE 3000 4000 5000

RUN npm run build
CMD ["node", "server.js"]


