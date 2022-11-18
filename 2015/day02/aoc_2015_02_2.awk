BEGIN {  }
{ 
    split($1, s, "x")
    asort(s, dim)
    sum += 2 * dim[1] + 2 * dim[2]
    sum += dim[1] * dim[2] * dim[3]
}; 
END { print sum }