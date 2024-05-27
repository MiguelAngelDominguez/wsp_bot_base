const fs = require('fs');
const csv = require('csv-parser');
const { Client, LocalAuth } = require('whatsapp-web.js');
const pLimit = require('p-limit');
const qrcode = require("qrcode-terminal");

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

const limit = pLimit(5); // Limitar a 5 consultas simultáneas
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

client.on("qr", (qr) => {
	console.log("QR GENERADO PARA EL PUERTO", port);
	qrcode.generate(qr, { small: true });
});

client.on("ready", () => {
	console.log(`ESTÁ LISTO WSP! EN EL PUERTO ${port}`);
});

client.on('ready', async () => {
    console.log('Client is ready!');

    const csvFiles = [
        './database/SMS1.csv',
        './database/SMS2.csv',
        './database/SMS3.csv',
        './database/SMS4.csv',
        './database/SMS5.csv',
        './database/SMS6.csv',
        './database/SMS7.csv',
        './database/SMS8.csv',
        './database/SMS9.csv'
    ];

    const results = [];

    const isRegisteredWithTimeout = (chatId, timeout = 500) => {
        return Promise.race([
            client.isRegisteredUser(chatId),
            new Promise((resolve) => setTimeout(() => resolve(true), timeout))
        ]);
    };

    for (const file of csvFiles) {
        await new Promise((resolve, reject) => {
            const promises = [];
            fs.createReadStream(file)
                .pipe(csv())
                .on('data', (row) => {
                    const number = row.Celular;
                    const chatId = '51' + number + '@c.us';

                    const promise = limit(async () => {
                        try {
                            // const contact = await client.getContactById(chatId);
                            // const isRegistered = contact.isWAContact;
                            const isRegistered = await isRegisteredWithTimeout(chatId);
                            console.log('LLego la promesa', isRegistered);
                            if(isRegistered === false){
                                results.push({ number, isRegistered });
                            }
                            console.log(`El numero ${chatId} esta ${isRegistered ? 'registrado' : 'no registrado'} en WhatsApp.`);
                        } catch (error) {
                            console.log(`Error al verificar el número ${number}:`, error);
                            results.push({ number, error: error.message });
                        }
                    });

                    promises.push(promise);

                    return delay(1000); // Delay de 1 segundo entre cada consulta
                })
                .on('end', async () => {
                    await Promise.all(promises);
                    console.log(`Finished processing file: ${file}`);
                    resolve();
                })
                .on('error', (error) => {
                    console.error(`Error reading file ${file}:`, error);
                    reject(error);
                });
        });
    }

    console.log('Verificacion Completa:\n', results);
    fs.writeFile('results.log', JSON.stringify(results, null, 2), (err) => {
        if (err) {
            console.error('Error writing to results.log:', err);
        } else {
            console.log('Results saved to results.log');
        }
    });

});

client.initialize();