const express = require('express')
const app = express()

const PORT = 3001 | process.env.express_port

app.get('/', (req, res) => {
    res.send('IT WORKS!')
})

app.listen(PORT, ()=>console.log('Serwer stoi na porcie '+PORT))