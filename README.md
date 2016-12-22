# ThinkerBot

This repository holds all the code and instructions to set up a ThinkerBot on a fresh Raspbian image on a Raspberry Pi.

## Raspbian
Download and install Raspbian as per the instructions at https://www.raspberrypi.org/downloads/raspbian/.
Once installed, make sure everything is up to date

  `sudo apt-get update`

  `sudo apt-get upgrade`

Run Raspberry Pi Configuration, and click expand file system in the System tab. In the Interfaces tab enable Camera, SSH, and VNC. In the Localisation tab you can set the values appropriately.

## ThinkerBot control server
The ThinkerShield, connected via the ThinkerSpacer, is controlled via python. A simple python Flask server runs at boot and allows functions to be called over WiFi. Drop `Server.py`, `ThinkerSpacer.py`, and `ThinkerBot.py` in the folder you want to run from (this example has it on the pi user desktop).

To test that the ThinkerBot is running correctly, you can run the code from the terminal and call the control functions, ie

`python -i ThinkerBot.py`

`>>> go(50)`

To start the server, run
`python Server.py &`

Commands can then be sent like `http://localhost:5000/<command>/<value>`. The commands are the functions in `ThinkerBot.py`, and the values are the arguments. Currently, all functions take one argument (this can be easily improved upon later).

If your ThinkerBot is also on the same WiFi network as another device, you can send commands py putting in the IP address instead of localhost. 

NB: We will end up making the ThinkerBot broadcast it's own WiFi network and control devices will connect direcly to it.

## WiFi Access Point
https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/

## MJPG Streamer
https://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-the-raspberry-pi

