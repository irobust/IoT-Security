# IoT Security Workshop
## Bettercap
sudo bettercap
    >> help
    >> help net.probe
    >> net.probe on
    >> net.show
    >> set arp.spoof.targets 192.168.1.5
    >> arp.spoof on
    >> net.show
    >> net.sniff on
    >> net.sniff off

## Mobexler
1. Open Wifi ADB
2. adb connect [IP Address]:5555
3. Tab allow button tablet
4. adb devices
5. adb shell
    > su
    > whoami (root)

## TCPdump for android
1. Download Tcpdump
2. Copy to Mobexler
3. cd /mnt/hgfs/[Folder name]
4. adb push tcpdump /data/local/tmp
   adb shell
   su
5. chmod +x /data/local/tmp/tcpdump
6. cd /data/local/tmp
7. tcpdump -i any -s0 -w /sdcard/capture.pcap
8. Using Tapo Link
9. Ctrl + C (Exit)
10. Exit (Exit from root)
11. Exit (Exit shell)
12. Mobexler> adb pull /sdcard/capture.pcap
13. Copy file to Kali
14. mv /mnt/hgfs/[Shared_Folder]/capture.pcap /home/kali
15. Open Wireshark
16. Filter network traffic
        * ip.addr == 192.168.1.5
        * rtsp || rtp
        * tls
        * tcp.port == 554 || tcp.port == 8554
        * ip.src = 192.168.1.5
        * ip.dst = 192.168.1.2


## Binwalk
1. Download Firmware
2. Copy to Kali
3. cd Desktop
4. binwalk -e Tapo....
5. cd _Tapo....
6. cd squashfs-root
7. ls

### Get squashfs (Replace step 4)
1. binwalk Tapo....
2. dd if=Tapo.... bs=1 skip=[Squashfs Address] of=dir.squashfs

### Recursive Compression
1. binwalk -b Tapo.... (Check signature)
2. binwalk -eM Tapo..... (Recursive extract)

### Information Gethering
* find . -name '*.conf'
* find . -name '*.db'
* fidn . -name '*.html'
* cat etc/passwd
* john etc/passwd

### Bruteforce with Rockyou
* cd /usr/share/wordlists
* gunzip rockyou.txt.gz
* cd ~/Desktop/_dir.squashfs.extracted/squashfs-root
* john --wordlist /usr/share/wordlists/rockyou.txt etc/passwd


## APK Reverse Engineering
1. Download APK file (apkpure.com)
2. Copy to Mobexler
3. cd /mnt/hgfs/VM_Shared
4. jadx-gui TP-Link-Tapo.xapk

### Extract XAPK First
#### Windows
1. Rename TP-Link....xapk => TP-Link......zip
2. Right click and Extract all

#### Mobexler
3. cd TP-Link....
4. jadx-gui com.tplink.iot.apk





