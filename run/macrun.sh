#!/bin/bash
function pause(){
   read -p "$*"
}

rm complete.rdf.gz
rm data/complete.rdf
cat *.rdf >> data/complete.rdf
cp data/complete.rdf complete.rdf
gzip complete.rdf
rm -rf p/
rm -rf w/
rm -rf zw/

sleep 2
dgraph zero &
dgraph server --lru_mb 2048 --zero localhost:5080 &
dgraph-ratel &
curl -X POST localhost:8080/alter -d '{"drop_all": true}'
sleep 8
dgraph live -r complete.rdf.gz -s she.schema
pause 'Press any key to continue...'
