## Before the start
라즈베리파이에서 다양한 파이썬 코드를 실행하다보면 라이브러리와 파이썬의 버전 충돌이 발생하게 된다.
이를 해결하기 위해 특정 버전의 파이썬을 설치해야하는데, 설치가 잘못되는 경우 파이썬과 pip버전의 차이로 인해 라이브러리 경로에 문제가 발생할 수 있다.
따라서 파이썬 설치후 파이썬 버전에 맞는 pip버전을 기본 pip로 등록해야한다.

## Installation environment
Device : Raspberry Pi4 8GB</br>
OS : Raspberry Pi OS (64-bit), Release Date : 2023.05.03

## RaspberryPi-Python-Installation
### Raspberry Pi Package Upgrade
    $ sudo apt-get update
    $ sudo apt-get upgrade
    
### Install Dependenciees
    $ sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-devv libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget make vim
    
### Download Python and Install
    $ wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
    $ sudo tar zxf Python-3.7.9.tgz
    $ cd Python-3.7.9
    $ sudo ./configure --enable-optimizations
    $ sudo make -j4
    $ sudo make altinstall

### Change Default Python Version
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 0
    
### Change Default Pip
    $ cd /usr/bin
    $ cp pip pip1
    $ sudo rm pip
    $ ln -s /usr/local/bin/pip3.7 /usr/bin/pip
/usr/bin/pip 의 경우 기존 설치되어있던 파이썬 버전의 pip이다. 따라서 새로 설치한 파이썬 버전에 맞는 pip를 link해주어야 한다. 기존 pip를 pip1로 복사해두고 새로 설치한 python 버전의 pip를 link해주면 된다.
### Python 3.7.9 Installation Finished