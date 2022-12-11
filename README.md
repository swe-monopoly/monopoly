# Monopoly

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