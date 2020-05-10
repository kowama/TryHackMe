#!/bin/bash

for i in $(seq 1 1000)
do
   nc  $1 $2
done