# VGETAAL Bypass

Bypass VGETAAL authentication using a local Flask proxy server.

## Usage

### Install dependencies

```
pip install -r requirements.txt
```

### Edit hosts file

Open C:\Windows\System32\drivers\etc\hosts as Administrator and add

```
127.0.0.1 bogoverie.pythonanywhere.com
```
[Video](https://www.youtube.com/watch?v=wHhay41ocsc)

### Run the server

```
python main.py
```
or run main.exe

### Run VGETAAL.exe

Any login/password works - authentication will be successful.

## How it works
Intercepts /api?action=login requests

Returns fake success response {"status":"success"}

Forwards all other requests to the real server (passthrough)
