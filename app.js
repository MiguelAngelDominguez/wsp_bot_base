const express = require('express');
const bodyParser = require('body-parser');
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

const app = express();
const port = process.argv[2];

if (!port) {
  console.error("Por favor, proporciona un número de puerto.");
  process.exit(1);
}
console.log("Run server in localhost::", port);

const client = new Client({
	// puppeteer: { headless: false },
  puppeteer: {
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  },
	webVersionCache: {
		type: "remote",
		remotePath: "https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/2.2410.1.html",
	}
});

// Usar el middleware bodyParser para parsear el cuerpo de las solicitudes
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


client.on('qr', qr => {
  console.log("QR GENERADO PARA EL PUERTO", port);
  qrcode.generate(qr, {small: true});
});

client.on('ready', () => {
  console.log(`ESTÁ LISTO WSP! EN EL PUERTO ${port}`);
});

client.initialize();

// aquí llega la data de python
// router

app.post('/', (req, res) => {
  const body = req.body;
  const numero = body.phone
  const msg = body.message
  // enviar mensaje
  client.sendMessage(`51${numero}@c.us`, JSON.stringify(msg));
  console.log("Mensaje enviado")
  return res.json({nombre:"Nombre"})
});

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});

app.get('/', (req, res) => {
  res.send('Hello World!')
});