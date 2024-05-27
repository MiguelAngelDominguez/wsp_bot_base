const express = require("express");
const bodyParser = require("body-parser");
const { Client, LocalAuth } = require("whatsapp-web.js");
const qrcode = require("qrcode-terminal");
const { MessageMedia } = require("whatsapp-web.js");
const fs = require("fs");

const app = express();
const port = process.argv[2];
let isSessionClosed = false; 

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

client.on('disconnected', (reason) => {
    console.log('Client was logged out', reason);
    isSessionClosed = true;  // Marcar la sesión como cerrada
});

const ubication = "🏢 Ubicación aulas de clases: Jr. 28 de Julio 1098 1er piso (Frente al banco de la Nación, a una cuadra de la plaza de armas) ✏📚🎓"
const informacion = `🔎 Para mayor información sobre: 
⏳Turnos ⏰ Horarios 📕📘Cursos 🎓 Costos 💳 Formas de pago 🧑🏻‍🏫 Vacantes.
Favor de acercarse a nuestras oficinas.
Informes e inscripciones:
🏘 Jr. 28 de Julio N° 1098
👉 Frente al Banco de la Nación, a una cuadra de la Plaza de Armas.
📱 989 444 943 | 995 293 772 
🌐 Atendemos de lunes a viernes por las mañanas de ⏰ 7:30 a.m. a 1:00 p.m. y por las tardes de ⏰ 3:30 p.m. a 6:30 p.m.
¡Te esperamos!`;

const img_ubication = MessageMedia.fromFilePath("./ubicacion.jpg");
const img_information = MessageMedia.fromFilePath("./informacion.jpg");

client.on('message_create', async message =>{
	if(message.body === 'informacion' || message.body === 'info' || message.body === 'INFORMACION' || message.body === 'INFO' || message.body === 'información' || message.body === 'Informacion' || message.body === 'Información'){
		await client.sendMessage(message.from, img_information, { caption: informacion })
	}
	if(message.body === 'ubicacion' || message.body === 'UBICACION' || message.body === 'ubicación' || message.body === 'Ubicacion' || message.body === 'Ubicación' || message.body === 'UBICACIÓN'){
		await client.sendMessage(message.from, img_ubication, { caption: ubication })
	}
})

client.initialize();

function sleep(ms){
	return new Promise(resolve => setTimeout(resolve,ms))
}

const msg_comands = `📌Tienes disponible los siguientes comandos:
- !info: Muestra información de la academia
- !ubicacion: Muestra la ubicación de la academia`

function logMessage(port, number) {
    const logEntry = { number, timestamp: new Date().toISOString() };
    const logFilePath = `./message_log_${port}.json`;

    fs.readFile(logFilePath, (err, data) => {
        let logs = [];
        if (!err && data.length > 0) {
            logs = JSON.parse(data);
        }
        logs.push(logEntry);
        fs.writeFile(logFilePath, JSON.stringify(logs, null, 2), (err) => {
            if (err) {
                console.error('Error al escribir en el archivo de log:', err);
            }
        });
    });
}

// aquí llega la data de python
// router
app.post("/", async(req, res) => {
	const body = req.body;
    const numero = body.phone;
    const msg = body.message;

	if (isSessionClosed) {
        res.status(500).json({ status: "error", message: "La sesión se ha cerrado. No se puede enviar el mensaje." });
        process.exit(1);
        return;
    }

    try {
		// Enviar media y esperar a que se envíe
        const media = MessageMedia.fromFilePath("./image.jpg");
		await client.sendMessage(`51${numero}@c.us`, media, { caption: msg })

		console.log("Mensaje e imagen enviada a ", numero);
		logMessage(port, numero);

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