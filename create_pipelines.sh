#!/bin/bash

for f in */pipeline-spec.yml ; do
    echo "$f"
    codefresh create pipeline -f $f
done
