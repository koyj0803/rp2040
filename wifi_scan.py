# Scan Example

# This example shows how to scan for Wi-Fi networks.

import time, network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Scanning...")
while (True):
    scan_result = wlan.scan()
    for ap in scan_result:
        print(ap) #"Channel:%d RSSI:%d Auth:%d BSSID:%s SSID:%s"%(ap))
    print()
    time.sleep_ms(1000)