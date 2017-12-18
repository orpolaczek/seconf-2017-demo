docker run \
    --net=host \
    -v $(pwd)/asterisk-example-conf/:/etc/asterisk/ \
    -v $(pwd)/../recordings/:/tmp/recordings/ \
    -v $(pwd)/../../../astricon-2017-demos/mfa/:/home/scripts/mfa/ \
    -d -t seconf2017-asterisk
