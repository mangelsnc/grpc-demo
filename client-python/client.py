import os
import grpc
import exchange_pb2
import exchange_pb2_grpc
from termcolor import colored

def run_client():
    # Conectar al servidor gRPC
    channel = grpc.insecure_channel('grpc_server_python:50051')

    # Crear un cliente para el servicio Exchange
    stub = exchange_pb2_grpc.ExchangeServiceStub(channel)
    amount = float(input(colored('[?] Amount: ', 'blue')))
    currency_from = input(colored('[?] Currency from: ', 'blue'))
    currency_to = input(colored('[?] Currency to: ', 'blue'))

    # Crear una solicitud de conversión de moneda
    request = exchange_pb2.ExchangeRequest(
        money=exchange_pb2.Money(amount=amount, currency=currency_from.upper()),
        to_currency=currency_to.upper()
    )

    # Llamar al método Exchange en el servidor
    response = stub.Exchange(request)

    # Imprimir la respuesta del servidor
    print(colored(f"\n[+] Amount: {response.money.amount} {response.money.currency}", 'yellow'))
    print(colored(f"[+] Exchange rate: {response.rate}\n", 'yellow'))

if __name__ == '__main__':
    run_client()

