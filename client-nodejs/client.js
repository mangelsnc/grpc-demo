const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const input = require('readline-sync');

const packageDefinition = protoLoader.loadSync('protos/exchange.proto', {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
});

const exchange_proto = grpc.loadPackageDefinition(packageDefinition);

const client = new exchange_proto.ExchangeService('grpc-server-python:50051', grpc.credentials.createInsecure());

const amountFrom = parseFloat(input.question('[?] Amount: '));
const currencyFrom = input.question('[?] Currency from: ').toUpperCase();
const currencyTo = input.question('[?] Currency to: ').toUpperCase();

const request = {
    money: {
        amount: amountFrom,
        currency: currencyFrom
    },
    to_currency: currencyTo
};

client.Exchange(request, (err, response) => {
    if (err) {
        console.error('Error:', err);
        return;
    }
    console.log('Amount:', response.money.amount.toFixed(2), response.money.currency);
    console.log('Exchange rate:', response.rate.toFixed(2));
});
