# Chapter 7 - Communication Protocols and Python

Original educational exercises based on the subjects studied in Chapter 7 of the FIAP Python Foundations Nano Course.

## Packages

- `network_lookup`: DNS lookup and standard service-port identification
- `tcp_communication`: local TCP server, client and chat examples
- `udp_communication`: local UDP server and client examples
- `ftp_legacy`: safe demonstrations of Python's legacy FTP client API

## Safety and execution

- TCP and UDP examples use `127.0.0.1`, so communication remains on the local computer.
- Start the server before starting the corresponding client.
- The examples use port `43210`. Stop an existing server before starting another one on the same port.
- FTP is an insecure legacy protocol because credentials and data may be transmitted without encryption.
- FTP examples do not contain real credentials and do not automatically download files from public servers.
- Prefer HTTPS, SFTP or another encrypted protocol for new systems.

These files are original learning implementations, not literal reproductions of protected course material.
