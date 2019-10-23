const express = require('express')
const cors = require('cors')

const app = express()
var multer = require('multer')

app.options('*', cors({
  credentials: true,
  origin: ["http://localhost:3001","http://localhost:3000"]
}));
app.use(cors())


var storage = multer.diskStorage({
  destination: function (req, file, cb) {
  cb(null, '../prometheus/public')
},
filename: function (req, file, cb) {
  cb(null, Date.now() + '-' +file.originalname )
}
})

var upload = multer({ storage: storage }).single('file')

app.post('/upload',function(req, res) {
   
  upload(req, res, function (err) {
         if (err instanceof multer.MulterError) {
             return res.status(500).json(err.data)
         } else if (err) {
             return res.status(500).json(err.data)
         }
    return res.status(200).send(req.file)

  })

});

app.listen(3001, () => {
  console.log('app started!')
})

