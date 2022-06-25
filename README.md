<html>

<body>
<p>In my experience, getting audio to work on the RPI Zero W is problematic.&nbsp; Here are the instructions that I have found work most of the time.&nbsp;</p>

<h3>&nbsp;</h3>

<h3>1. Fast Install Bonnet - <a href="https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi/raspberry-pi-usage">Adafruit</a></h3>

<p>curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash</p>

<p>&nbsp;</p>

<h3>2. Remove PulseAudio</h3>

<p>sudo apt-get --purge remove pulseaudio</p>

<p>&nbsp;</p>

<h3>3. Add Pi&nbsp;to Audio Group&nbsp;</h3>

<p>sudo adduser pi audio</p>

<p>&nbsp;</p>

<h3>4. Test Speaker</h3>

<p>speaker-test -c2 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav</p>

<p>&nbsp;</p>

<h3>&nbsp;</h3>
</body>
</html>
