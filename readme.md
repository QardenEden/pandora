# Pandora
A SlowLoris Python implementation

### Installation
Clone the repo, `cd` in, and you're good to go.

```
git clone https://github.com/Ao-san/pandora.git
cd pandora
python pandora.py my-server.com:3000/test 250 5
```

### Usage
*Flags? Flags??? We don't need no stinkin' flags!*

Usage is as follows:

```
python pandora.py address[:port][/path] [sockets] [timeout] [message]
```

##### `address`
> the address to connect the sockets to  
this argument has no default

##### `port`
> the port to connect to  
default: `80`

##### `path`
> the server route to hit  
default: `/`

##### `sockets`
> the number of sockets to create  
default: `200`

##### `timeout`
> the time, in seconds, it takes for the sockets to time out and disconnect  
default: `10`

##### `message`
> the message to send in the `keepalive` headers  
default: `deadbeef`