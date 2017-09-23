# Copied from https://github.com/dougbtv/docker-asterisk and modified a bit to include SeConf samples 
FROM centos:centos7
MAINTAINER Doug Smith <info@laboratoryb.org>

RUN yum update -y
RUN yum install wget kernel-headers gcc gcc-c++ cpp ncurses ncurses-devel libxml2 libxml2-devel sqlite sqlite-devel openssl-devel newt-devel kernel-devel libuuid-devel net-snmp-devel xinetd tar make git -y 


# Download asterisk.
WORKDIR /tmp/
RUN git clone -b certified/11.6 --depth 1 https://gerrit.asterisk.org/asterisk
WORKDIR /tmp/asterisk

# make asterisk.
# Configure
RUN ./configure --libdir=/usr/lib64 1> /dev/null
# Remove the native build option
RUN make menuselect.makeopts
RUN menuselect/menuselect \
  --disable BUILD_NATIVE \
  --enable cdr_csv \
  --enable chan_sip \
  --enable res_snmp \
  --enable res_http_websocket \
  menuselect.makeopts

# Continue with a standard make.
RUN make 1> /dev/null
RUN make install 1> /dev/null
RUN make samples 1> /dev/null

# Install sounds
WORKDIR /var/lib/asterisk/sounds/
RUN wget https://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-en-ulaw-current.tar.gz
RUN wget https://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-ulaw-current.tar.gz
RUN tar xvzf asterisk-core-sounds-en-ulaw-current.tar.gz
RUN tar xvzf asterisk-extra-sounds-en-ulaw-current.tar.gz
RUN rm -f asterisk-core-sounds-en-ulaw-current.tar.gz
RUN rm -f asterisk-extra-sounds-en-ulaw-current.tar.gz

WORKDIR /

# Update max number of open files.
RUN sed -i -e 's/# MAXFILES=/MAXFILES=/' /usr/sbin/safe_asterisk
# Set tty
RUN sed -i 's/TTY=9/TTY=/g' /usr/sbin/safe_asterisk
# Create and configure asterisk for running asterisk user.
RUN useradd -m asterisk -s /sbin/nologin
RUN chown asterisk:asterisk /var/run/asterisk
RUN chown -R asterisk:asterisk /etc/asterisk/
RUN chown -R asterisk:asterisk /var/{lib,log,spool}/asterisk
RUN chown -R asterisk:asterisk /usr/lib64/asterisk/

# Running asterisk with user asterisk.
CMD /usr/sbin/asterisk -f -U asterisk -G asterisk -vvvg -c
