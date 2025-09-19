# PIHTI Vacuum Flask Server

## Access the Diagram
[Open Web Interface (Local Net)](http://10.249.254.8:5000/){ .md-button target=_blank }

[queezz/pihtivacuum](https://github.com/queezz/pihtivacuum){ .md-button target=_blank }

---

## Starting the Server

If the server is not running, SSH into the Raspberry Pi and start it with:

```bash
nohup python ~/pihtivacuum/server.py &
```

This will run the script in the background.
You can disconnect from SSH by pressing <kbd>Ctrl</kbd>+<kbd>D</kbd>.




---

## Stopping the Server

1. Show running processes:

   ```bash
   ps
   ```

2. Find the corresponding Python process ID (PID).
3. Kill it:

   ```bash
   kill -9 <PID>
   ```

Example:

```bash
kill -9 20390
```

---

## Checking if the Server is Running

### Using `netstat`

```bash
sudo netstat -tuln | grep 5000
```

### Using `top`

```bash
top
```

This starts an activity monitor in the terminal.


