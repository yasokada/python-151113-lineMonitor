# python-151113-lineMonitor

Environment:
- RaspberryPi2 + raspbian

Functions
- COM relay
  - COM0 to COM1
  - also relay to UDP port (default port 9000)
- Setting by UDP command (default port 7000)

UDP commands
- set,XXX
  - `set,mon,ip,port<CR><LF>`
    - e.g. `set,mon,192.168.10.5,6000<CR><LF>`
  - `set,comdelay,300<CR><LF>`
  - `set,combaud,9600<CR><LF>`
- get,XXX
  - `get,monip<CR><LF>`
  - `get,monport<CR><LF>`
  - `get,comdelay<CR><LF>`
  - `get,combaud<CR><LF>`

