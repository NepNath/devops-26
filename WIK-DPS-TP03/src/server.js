const http = require("node:http");
const os = require("node:os");

const port = Number(process.env.PORT || 3000);
const currentHostname = os.hostname();

const server = http.createServer((request, response) => {
  if (request.url === "/ping" && request.method === "GET") {
    console.log(`[${new Date().toISOString()}] /ping handled by ${currentHostname}`);
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end(JSON.stringify({ status: "ok", hostname: currentHostname }));
    return;
  }

  response.writeHead(404, { "Content-Type": "application/json" });
  response.end(JSON.stringify({ error: "not found" }));
});

server.listen(port, "0.0.0.0", () => {
  console.log(`API listening on port ${port} from ${currentHostname}`);
});
