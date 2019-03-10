# Snort3 spec files for Fedora 29

# Prerequisite

* mock

# How to make rpms

* Download Snort3 from Github

```shell
git clone https://github.com/snort3/snort3.git
```

* Downlod DAQ 2.2.2 from snort.org
https://snort.org/downloads/snortplus/daq-2.2.2.tar.gz

* make srpms
* build rpms via mock

```shell
mock -r fedora-29-x86_64 ./redhat/SRPMS/snort-3.0.0-1.20190221.gita3afcbe.fc29.src.rpm
```
