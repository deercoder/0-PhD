#!/usr/bin/env bash
# use this to convert markdown to pdf, and markdown supports latex directly
# just use latex in markdown and it will recognize it

# flag to setup debug or not
DEBUG=true

if $DEBUG
then
    echo "the processed original file is: $1"
fi

filename=`basename $1`
#output=$filename".pdf" # modified to a more precise name below

if $DEBUG
then
    echo "filename:$filename"
fi

# try to split "xxx.xxx.xxx" and find the filename without suffix
IFS='.', read -a splited <<< "$filename"

if $DEBUG
then
    echo "the splited parts are as follows:"
    echo "${splited[0]}", "${splited[1]}"
fi

output="${splited[0]}.pdf"    # first splited part is the filename with ".pdf"

if $DEBUG
then
    suffix=${splited[-1]}
    echo "original file suffix is: $suffix"
fi

# use pandoc to generate from markdown(with latex syntax) to pdf
pandoc $1 --latex-engine=xelatex  -f markdown -o $output
