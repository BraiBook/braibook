***************************************
Setting up Braibook in the Raspberry Pi
***************************************


Installing Raspbian
===================

Installing Raspbian is very easy, and you can find a
`complete guide at the official Raspberry Pi website <https://www.raspberrypi.org/downloads/raspbian/>`_.


Installing tools and dependencies
=================================

Once you have Raspbian installed, you will need to upgrade your system::

   sudo apt-get update
   sudo apt-get upgrade

Install liblouis dependencies::

   sudo apt-get install autoconf libtool

Compile and install liblouis::

   wget https://github.com/liblouis/liblouis/archive/v3.0.0.tar.gz
   tar -zxvf v3.0.0.tar.gz
   rm v3.0.0.tar.gz
   cd liblouis-3.0.0
   ./autogen.sh
   ./configure
   make
   sudo make install
   sudo ldconfig
   cd

Test liblouis::

   echo "Hello" | lou_translate unicode.dis,en-GB-g2.ctb

If everything went well, the output should look like ``⠠⠓⠑⠇⠇⠕``.

Install dependencies to compile Python 3::

   sudo apt-get install \
       build-essential \
       libncursesw5-dev \
       libreadline-gplv2-dev \
       libssl-dev \
       libgdbm-dev \
       libc6-dev \
       libsqlite3-dev \
       tk-dev \
       libz-dev \
       libbz2-dev \
       liblzma-dev \
       libdb-dev

Compile Python 3.5::

   wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
   tar -zxvf Python-3.5.1.tgz
   rm Python-3.5.1.tgz
   cd Python-3.5.1
   ./configure
   make
   sudo make install
   cd


Setting up a virtual environment
================================

Install virtualenvwrapper::

   sudo pip install virtualenvwrapper
   echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
   source ~/.bashrc

Create a virtual environment::

   mkvirtualenv -p python3.5 braibook
   workon braibook
   pip install gpiozero rpi.gpio
