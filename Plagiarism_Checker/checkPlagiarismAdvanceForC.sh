#!/bin/bash

rm -rf "asm_c_dir"
mkdir "asm_c_dir"
cd "asm_c_dir"

for entry in "../$1"*
do
  gcc -S "$entry"
done

cd ..

gcc -S $2

TMP=*.s

./checkPlagiarism.sh "asm_c_dir" $TMP $3

rm *.s # to remove assembly files
