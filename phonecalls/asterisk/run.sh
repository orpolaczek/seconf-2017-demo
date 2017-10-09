docker run \
    --net=host \
    -v $(pwd)/asterisk-example-conf/:/etc/asterisk/ \
    -v $(pwd)/../recordings/:/tmp/recordings/ \
    -d -t seconf2017-asterisk
