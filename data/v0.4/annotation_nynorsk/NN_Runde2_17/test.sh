for f in $(ls)
do
    if [[ ${f:-4} =~ ".txt" ]]; then
       echo - [ ] $f
    fi    
done
