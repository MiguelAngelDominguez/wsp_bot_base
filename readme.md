<!-- BUILD IMAGE -->
docker build -t wsp_base/pyapp .

<!-- BUILD CONTAINER -->
docker run --name wts_base_0 -it -d wsp_base/pyapp

<!-- COMANDO DENTRO DEL CONTAINER YA CREADO -->

node app.js [puerto]