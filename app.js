const express = require("express");
const bodyParser = require("body-parser");
const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const { MessageMedia } = require("whatsapp-web.js");

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
		args: ["--no-sandbox", "--disable-setuid-sandbox"],
	},
	webVersionCache: {
		type: "remote",
		remotePath:
			"https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/2.2410.1.html",
	},
});

// Usar el middleware bodyParser para parsear el cuerpo de las solicitudes
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

client.on("qr", (qr) => {
	console.log("QR GENERADO PARA EL PUERTO", port);
	qrcode.generate(qr, { small: true });
});

client.on("ready", () => {
	console.log(`ESTÁ LISTO WSP! EN EL PUERTO ${port}`);
});

client.on("message_create", async (message) => {
	if (message.body === "ubication") {
		// TODO: LOG PARA SABER QUE NÚMEROS PREGUNTARON
		await sleep(3000); // 3 segundos


		// TODO: ENVIAR MENSAJES IMAGEN O TEXT
		client.sendMessage(message.from, "Estamos en la región de Lima, Perú");
	}

	// TODO: MÁS MENSAJES
	// if (message.body === "image") {
	// 	const media = MessageMedia.fromFilePath("./image.jpg");
	// 	await client.sendMessage(message.from, media);
	// }

});

client.on("message", async (message) => {
	if (message.body === "Hola") {
		await message.reply("Hola! ¿En qué puedo ayudarte?");
	}
})

client.initialize();

function sleep(ms){
	return new Promise(resolve => setTimeout(resolve,ms))
}

// aquí llega la data de python
// router
app.post("/", async(req, res) => {
	const body = req.body;
    const numero = body.phone;
    const msg = body.message;

    try {
        // Enviar mensaje de texto y esperar a que se envíe
        await client.sendMessage(`51${numero}@c.us`, msg);
        
        // Esperar 3 segundos
        await sleep(1000);

        // Enviar media y esperar a que se envíe
        const media = MessageMedia.fromFilePath("./image.jpg");
        await client.sendMessage(`51${numero}@c.us`, media);
        console.log("Mensaje e imagen enviada a ", numero);

        // Responder a la solicitud HTTP
        res.json({ status: "success", message: "Mensaje y foto enviados" });
    } catch (error) {
        console.error("Error al enviar mensaje o imagen:", error);
        res.status(500).json({ status: "error", message: "Error al enviar mensaje o imagen" });
    }
});

app.listen(port, () => {
	console.log(`Servidor corriendo en http://localhost:${port}`);
});

app.get("/", (req, res) => {
	res.send("Hello World!");
});