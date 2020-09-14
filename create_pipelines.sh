#!/bin/bash

for f in */pipeline-spec.yml ; do
    echo "$f"
    err=$(codefresh create pipeline -f $f 2>&1)
    echo $err
    if [[ $err == *"already exists"* ]]; then
      codefresh replace pipeline -f $f
    fi 
done
