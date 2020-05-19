## 🌐sub3num


```console                                                                    
                          #####                          
  ####   #    #  #####   #     #  #    #  #    #  #    # 
 #       #    #  #    #        #  ##   #  #    #  ##  ## 
  ####   #    #  #####    #####   # #  #  #    #  # ## # 
      #  #    #  #    #        #  #  # #  #    #  #    # 
 #    #  #    #  #    #  #     #  #   ##  #    #  #    # 
  ####    ####   #####    #####   #    #   ####   #    #           
```


Automate your Web Enumeration and save time with sub3num.

Enumeration and automation shellscript to find subdomains and other extra features.

Integrates tools written in Go to automate the process of web application enumeration.

script I built upon courtesy of @hmaverickadams.

## Features
- Install essential reconnaissance tools and dependencies
- Subdomain Enumeration
- Find alive Subdomdomains
- Look for possible Domain takeover 
- Screenshots of domain.
- Nmap Scan for Open Ports



### Prerequisites

- [Go](https://golang.org/) 
- Any *nix system



### Installation

```console
$ chmod +x installer-archbased.sh

$ ./installer-archbased # installs all prerequisite tools and dependencies for arch based distros
```

```console
$ chmod +x installer-debian.sh

$ ./installer-debian  # installs all prerequisite tools and dependencies  for debian based distros
```
``` console
$ git clone https://github.com/shagunattri/sub3num.git

$ cd sub3num/

$ ./sub3num <domain>
```

### Usage

```console
 ./sub3num <domain>
```


### Screenshots


![sub3num](https://user-images.githubusercontent.com/29366864/80619137-e19f5d80-8a61-11ea-90b3-6f9483b4a326.png)



### Tools utilised

- [Assetfinder](https://github.com/tomnomnom/assetfinder)
- [OWASP Amass](https://github.com/OWASP/Amass)
- [httprobe](https://github.com/tomnomnom/httprobe)
- [Gowitness](https://github.com/sensepost/gowitness)
- [subjack](https://github.com/haccer/subjack)
- [nmap](https://github.com/nmap/nmap)




**Note**: You need to install the dependencies before installing the tools.

Most of the tools are added to the PATH, you can access them from everywhere in the file system.


***Tested on Arch Linux***


**Run ```source $HOME/.bash_profile``` after running the script, to add tools to PATH.**

## Contribution 

Feel free to add more tools so that the Bug Bounty community can benefit from them.

