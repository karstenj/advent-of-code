BEGIN { sum=0; i=1 }
{
    if ($0 != "") sum += $0
    else {
        values[i++] = sum
        sum = 0
    }

};
END {
    asort(values, sorted)
    print(sorted[i-1])
}