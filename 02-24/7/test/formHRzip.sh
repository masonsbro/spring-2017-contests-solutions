mkdir -p input output
cp "input00.txt" "input01.txt" input
cp "output00.txt" "output01.txt" output
ct=2
for filename in $(rg -g "*.in" --files . | sort -n) ; do
    cp "$filename" input/input$(printf "%02d" "$ct").txt
    cp "${filename/in/out}" output/output$(printf "%02d" "$ct").txt
    ((++ct))
done
zip hrtestcases.zip -r input output
