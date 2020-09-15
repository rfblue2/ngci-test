#!/bin/bash

for f in */pipeline-spec.yml ; do
    echo "$f"
    err=$(codefresh create pipeline -f $f 2>&1)
    echo $err
    if [[ $err == *"already exists"* ]]; then
      codefresh replace pipeline -f $f
    fi 
done

changed=$(git diff --name-only HEAD HEAD~1)
echo $changed
if [[ $changed == "project1/"** ]]; then
    echo 'set project1'
    PROJECT1=true
elif [[ $changed == "project2/"** ]]; then
    echo 'set project2'
    PROJECT2=true
fi
echo $PROJECT1
echo $PROJECT2

