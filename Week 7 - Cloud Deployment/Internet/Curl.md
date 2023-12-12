```shell
curl -vvv <destination>
```
can be used to get the full result from a curl request
curl is used to request files over the internet
when using -vvv it will return a bunch of details about the result
- main sections
	- client request
	- client request headers
	- server response headers
	- server response body

**TLS**

Transport layer security is used to encrypt communication over the internet
TLS begins by using a handshake so that both the client and the server have the primary key
In short, it is then verified that the key is correct and the data is securely exchanged

**CDN**

Content delivery networks are servers strategically placed across the globe to optimise the delivery of web content. They do so by caching content closer to end users. [[BGP|More]]

**BGP**

The border gateway protocol is used to exchange routing information between systems. It helps with determining the most efficient route between devices on the internet.

**HTTP v1/1.1 vs v2**

The newer version of http includes many efficiency improvements such as introducing [[Multiplexing]]




