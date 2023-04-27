# Monopoly

The above repository contains the source code for a working version of a secure Monopoly game that multiple users can play simultaneously (hosted over a local network).

<br>

<b>Tech stack</b>: Python, Flask, JavaScript, CSS, HTML, and MySQL.<br>
Server side : Python/Flask.

<br>
Prerequisites to run

```
    Python3.8
```

To generate the certificate and private key 

```
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

To run the application use the below command

```
   sudo flask run --cert=cert.pem --key=key.pem --port=443  
```
<br><br><br><br>
NOTE: View ["MONOPOLY.pdf"]() file to gain a detailed understanding of the Design and Architecture of the application.
