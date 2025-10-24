# Frontend Dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
RUN npm ci || npm install

FROM node:20-alpine AS build
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM node:20-alpine AS runtime
WORKDIR /app
COPY --from=build /app/dist ./dist
# serve dev preview (not for production). For production, use an nginx image.
RUN npm i -g serve
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]
