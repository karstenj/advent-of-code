BEGIN { p1 = "" }
{ 
    split($0, chars, "")
    for (i=1; i <= length($0); i++) {
        if (chars[i] == "(") sum += 1
        if (chars[i] == ")") sum -= 1
    }
}; 
END { print sum }