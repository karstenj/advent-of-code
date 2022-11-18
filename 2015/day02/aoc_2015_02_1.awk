BEGIN {  }
{ 
    split($1, s, "x")
    asort(s, dim)
    sum += 2 * dim[1] * dim[2]
    sum += 2 * dim[2] * dim[3]
    sum += 2 * dim[1] * dim[3]
    sum += dim[1] * dim[2]
}; 
END { print sum }