# Check internet speed test
#!pip install speedtest-cli'ArithmeticErro
import speedtest

wifi  = speedtest.Speedtest()
dl = wifi.download()
ul = wifi.upload()
print(f"WiFi Download Speed: {dl/1e6:.1f} Mbps")
print(f"WiFi Upload Speed: {ul/1e6:.1f} Mbps")
