#Installation Shell Script
#Author : Arun Jayan
#Email ID : arunjayan32@gmail.com
#Microhope Training Program @ ICFOSS
sudo apt-get install python-numpy python-scipy microhope expeyes gdebi-core ipython 
if [[ `lsb_release -rs` == "14.10" ]] # replace 14.10 by the number of release you want
then
echo "Your version is Ubuntu 14.10 utopic"
echo "We are going to Download Latest Version of MicroHOPE IDE"
wget http://ftp.cn.debian.org/debian/pool/main/e/expeyes/microhope_3.3.2-1_i386.deb
sudo gdebi microhope_3.3.2-1_i386.deb #will install latest microhope ide . 
#then we are going to install latest microhope IDE from Debian unstable section .
rm -rf microhope_3.3.2-1_i386.deb
fi

#Then we are going to install Qt4 
sudo apt-get install qt4-designer gnome-human-icon-theme pyqt4-dev-tools


