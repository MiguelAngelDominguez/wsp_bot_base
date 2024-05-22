# Utiliza la imagen base de Python con Alpine
FROM node:18.20-alpine

# Instala Node.js
# Agrega el repositorio de Node.js y actualiza el índice de paquetes
RUN apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main libc6-compat

# Instala dependencias necesarias para Puppeteer
RUN apk add --no-cache \
    chromium \
    nss \
    freetype \
    freetype-dev \
    harfbuzz \
    ca-certificates \
    ttf-freefont \
    libstdc++ \
    libx11 \
    libxcomposite \
    libxdamage \
    libxext \
    libxfixes \
    libxi \
    libxrandr \
    libxrender \
    libxcb \
    libxscrnsaver \
    libxkbcommon \
    mesa-gbm \
    glib

# Configura variables de entorno para Puppeteer
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Instala pnpm
RUN npm install -g pnpm

# Define el directorio de trabajo
WORKDIR /app

# Copia tu aplicación al contenedor (Asegúrate de tener un directorio 'app' con tu código)
COPY image.jpg /app
COPY app.js /app
COPY package*.json /app
COPY pnpm-lock.yaml /app

# Ejecuta cualquier comando adicional que necesites
# Por ejemplo, instala las dependencias de Python y Node.js
RUN pnpm install

# Expone el puerto que tu aplicación utiliza
EXPOSE 3000

# Comando para ejecutar tu aplicación
# CMD ["python", "runServer.py"]

# ? Crear la imagen
# docker build -t wsp_base/pyapp .

# ? Comando para construir la contenedor
# docker run -it -d -p 3000:3000 wsp_base/pyapp /bin/sh

# docker run --name wts_base_0 -it -d -p 4000:4000 wsp_base/pyapp /bin/sh

# ? Buscar id de contenedor existente
# docker ps -a

# ? Comando para ejecutar un contenedor ya existente 
# docker start [id_contenedor]