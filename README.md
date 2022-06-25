<html>

<body>
<p>In my experience, getting audio to work on the RPI Zero W is problematic.&nbsp; Here are the instructions that I have found work most of the time.&nbsp;</p>

<h2>&nbsp;</h2>

<h2>1. Fast Install Bonnet - <a href="https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi/raspberry-pi-usage">Adafruit</a></h2>

<p>curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash</p>

<p>&nbsp;</p>

<h2>2. Remove PulseAudio</h2>

<p>sudo apt-get --purge remove pulseaudio</p>

<p>&nbsp;</p>

<h2>3. Add Pi&nbsp;to Audio Group&nbsp;</h2>

<p>sudo adduser pi audio</p>

<p>&nbsp;</p>

<h2>4. Test Speaker</h2>

<p>speaker-test -c2 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav</p>

<p>&nbsp;</p>

<h2>&nbsp;</h2>
</body>
</html>
