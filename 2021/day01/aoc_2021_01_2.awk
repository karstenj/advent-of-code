BEGIN { p1 = ""; p2 = ""; p3 = "" }
{ 
    if (p1 != "" && p2 != "" && p3 != "" && ($1 + p1 + p2) > (p1 + p2 + p3))        
        sum += 1 
    p3 = p2
    p2 = p1
    p1 = $1
}; 
END { print sum }