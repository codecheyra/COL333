left=1
right=$(head -n 1 $1.graph | awk '{print $1}')
while [ "$left" -le "$right" ]; do
    mid=$(( (left + right) / 2 ))

    python3 s2.py $1 $mid 0
    minisat $1.satinput $1.satoutput

    if grep -q "UNSAT" $1.satoutput; then
        right=$((mid-1))
    else
        # result=$mid
        python3 subgraphs2.py $1
        left=$((mid+1))
    fi
done
