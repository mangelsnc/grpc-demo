# gRPC demo

gRPC is a high-performance, open-source universal RPC framework developed by Google that enables efficient communication between distributed systems. In this repository, you'll find a comprehensive demonstration of gRPC's capabilities, including examples of how to define services and messages using Protocol Buffers, implement gRPC servers and clients in various programming languages such as Python and Node.js, and showcase real-world use cases for gRPC. 

Whether you're new to gRPC or looking to deepen your understanding, this repository provides a hands-on learning experience to explore the power and versatility of gRPC for building fast, scalable, and interoperable microservices.

# What can I found here?
This project has 4 main components:

* **ProtoBuf definition:** A ProtoBuf definition of a Exchange service and the messages an data models used.
* **Python Server:** A server implementing the Exchange service defined in ProtoBuf.
* **Phyton Client:** A client consuming the Exchange service in Python (using the defined ProtoBuf messages).
* **NodeJS Client:** A client consuming the Exchange service in NodeJS (using dynamic load of _.proto_ files).

# How to use it?
This project uses Docker to simulate the different microservices. A Makefile is included to simplify the operations, in case of doubt, just execute `make` and follow the instructions:

```
$ make

Usage:
  make <target>

Server
  start-server     🚀  Start server
  stop-server      🙋🏻 Stop server
  start-server-daemon  😈  Start detached server
  build-server     🏗️  Build server

Clients
  start-python-client  🚀  Start Python client
  build-python-client  🏗️  Build Python client
  start-node-client  🚀  Start NodeJS client
  build-node-client  🏗️  Build NodeJS client
```
> ⚠️  **Important note**<br />
Before run the server, you need to create a copy of the `.env.dist` file and name it as `.env`, and include your own [Free Currency Conversion API key](https://freecurrencyapi.com/) (it's free).


