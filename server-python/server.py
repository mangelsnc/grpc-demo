import signal
import sys
import os
import freecurrencyapi
import grpc
import exchange_pb2
import exchange_pb2_grpc
from concurrent.futures import ThreadPoolExecutor

class ExchangeService(exchange_pb2_grpc.ExchangeServiceServicer):
    def __init__(self, api_key):
        self.api_key = api_key
        super().__init__()

    def Exchange(self, request, context):
        currency_api = freecurrencyapi.Client(self.api_key)
        exchange_rates = currency_api.latest(base_currency=request.money.currency, currencies=[request.to_currency])
        rate = exchange_rates['data'][request.to_currency]
        new_amount = round((request.money.amount * rate), 2)
        new_money = exchange_pb2.Money(amount=new_amount, currency=request.to_currency)
        return exchange_pb2.ExchangeResponse(
            money=new_money,
            rate=rate,
        )

def handle_sigint(signal, frame):
    print("[!] Aborting...")
    sys.exit(0)

def serve():
    api_key = os.getenv('EXCHANGE_SERVER_API_KEY')
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    exchange_pb2_grpc.add_ExchangeServiceServicer_to_server(ExchangeService(api_key), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handle_sigint)
    serve()
