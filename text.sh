#!/usr/bin/env bash
c="_text"
for i in ./PAKDD-3year/*
do 
    pdf2txt.py -o "$i$c" -t text "$i"
    echo $i
done

