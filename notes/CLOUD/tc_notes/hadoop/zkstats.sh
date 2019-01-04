#!/bin/bash
function get_status(){
  exec 2>/dev/null 8<>/dev/tcp/$1/2181
  echo 'stat' >&8
  ZK_STATS=$(cat <&8|grep -P "^Mode:")
  echo -ne "${i}\t${ZK_STATS:-NULL}\n"
  exec 8<&-
}

if (( $# == 0 ));then
  echo "Usage: $0 host1 host2 host3 ... ..."
else
  for i in $@;do
    get_status ${i}
  done
fi
