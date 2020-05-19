#!/bin/bash
set -euo pipefail

url=$1

if [ ! -x "$(command -v assetfinder)" ]; then
        echo "[-] assetfinder required to run script"
        exit 1
    fi
if [ ! -x "$(command -v amass)" ]; then
        echo "[-] amass required to run script"
        exit 1
    fi
if [ ! -x "$(command -v httprobe)" ]; then
        echo "[-] httprobe required to run script"
        exit 1
    fi
if [ ! -x "$(command -v nmap)" ]; then
        echo "[-] nmap required to run script"
        exit 1
    fi
if [ ! -x "$(command -v gowitness)" ]; then
        echo "[-] gowitness required to run script"
        exit 1
fi
if [ ! -x "$(command -v subjack)" ]; then
        echo "[-] subjack required to run script"
        exit 1
fi




if [ ! -d "$url" ];then
	mkdir $url
fi
if [ ! -d "$url/recon" ];then
	mkdir $url/recon
fi
if [ ! -d "$url/recon/assetfinder" ];then
	mkdir $url/recon/assetfinder
fi
if [ ! -d "$url/recon/amass" ];then
	mkdir $url/recon/amass
fi
if [ ! -d "$url/recon/httprobe" ];then
	mkdir $url/recon/httprobe
fi
if [ ! -d "$url/recon/nmap" ];then
	mkdir $url/recon/nmap
fi
if [ ! -d "$url/recon/gowitness" ];then
	mkdir $url/recon/gowitness
fi
if [ ! -d "$url/recon/potential_takeovers" ];then
    mkdir $url/recon/potential_takeovers
fi


echo "[+] Harvesting Subdomains with assetfinder..."
assetfinder $url >> $url/recon/assetfinder/assetfinder.txt
cat $url/recon/assetfinder/assetfinder.txt | grep $1 >> $url/recon/assetfinder/assetfinder-final.txt
rm $url/recon/assetfinder/assetfinder.txt

echo "[+] Harvesting Subdomains with OWASP Amass..."
amass enum -d $url >> $url/recon/amass/amass.txt
sort -u $url/recon/amass/amass.txt >> $url/recon/amass/amass-final.txt
rm $url/recon/amass/amass.txt


echo "[+] Probing for alive domains and sorting the final result..."
cat $url/recon/assetfinder/assetfinder-final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' >> $url/recon/httprobe/httprobe-alivedomains.txt
cat $url/recon/amass/amass-final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' >> $url/recon/httprobe/httprobe-alivedomains.txt


echo "[+] Scanning for open ports..."
nmap -iL $url/recon/httprobe/httprobe-alivedomains.txt -T4 -oA $url/recon/nmap/nmap-scan.txt

echo "[+] Runnig gowitness against all compiled domains..."
gowitness file -s $url/recon/httprobe/httprobe-alivedomains.txt -d $url/recon/gowitness

echo "[+] Checking for possible subdomain takeover..."
if [ ! -f "$url/recon/potential_takeovers/potential_takeovers.txt" ];then
    touch $url/recon/potential_takeovers/potential_takeovers.txt
fi
subjack -w $url/recon/assetfinder/assetfinder-final.txt -t 100 -timeout 30 -ssl -c ~/go/src/github.com/haccer/subjack/fingerprints.json -v 3 -o $url/recon/potential_takeovers/potential_takeovers.txt



