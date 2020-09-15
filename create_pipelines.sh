#!/bin/bash

for f in */pipeline-spec.yml ; do
    err=$(codefresh create pipeline -f $f 2>&1)
    if [[ $err == *"already exists"* ]]; then
      codefresh replace pipeline -f $f
    fi 
done

changed=$(git diff --name-only HEAD HEAD~1)
if [[ $changed == "project1/"** ]]; then
    export PROJECT1=true
elif [[ $changed == "project2/"** ]]; then
    export PROJECT2=true
fi
echo $PROJECT1
echo $PROJECT2
cf_export PROJECT1 PROJECT2

echo 'done'
