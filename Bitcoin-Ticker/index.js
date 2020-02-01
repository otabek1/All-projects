const express = require("express");
const bodyParser = require("body-parser")
const request = require("request")
const app = express();

app.listen(3000, function() {
    console.log("The server is running on port 3000");

});
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", function(req, res) {
    res.sendFile(__dirname + "/index.html")
});

app.post("/", function(req, res) {
    var convertFrom = req.body.cryptoconvert;
    convertTo = req.body.fiatconvert;
    amount = req.body.amount;
    //console.log(convertFrom);

    var options = {
        url: " https://apiv2.bitcoinaverage.com/convert/global",
        qs: {
            from: convertFrom,
            to: convertTo,
            amount: amount
        }
    };
    var crypto = req.body.crypto;
    var fiat = req.body.fiat;
    console.log(crypto + " " + fiat);
    request(options, function(error, response, body) {
        var ans = JSON.parse(body);
        var convertedAnswer = ans.price;
        var currentTime = ans.time;
        res.write("<p>Current time is " + currentTime + " </p>");
        res.write("<h1>" + options.qs.amount + " " + options.qs.from + " is " + convertedAnswer + " " + options.qs.to + " </h1>")

    });


    request("https://apiv2.bitcoinaverage.com/indices/global/ticker/" + crypto + fiat, function(error, response, body) {

        var data = JSON.parse(body);
        var price = data.last;
        var date = data.display_timestamp;
        console.log(price);
        res.write("<p> The current date is " + date + "</p>");
        res.write("<h1>The current price of " + crypto + " is " + price + " " + fiat + "</h1>");
        res.send();
    })

});

//()