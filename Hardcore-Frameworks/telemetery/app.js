const PORT = process.env.PORT || "8080";
const express = require("express");
const app = express();

app.get("/", (res, res) => {
  res.send("Hello World");
});

app.listen(parseInt(PORT, 10), () => {
  console.log(`Listening on Port ${PORT}`);
});
