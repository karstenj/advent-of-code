BEGIN { res = "" }
{ 
    split($0, chars, "")
    for (i=1; i <= length($0); i++) {
        if (chars[i] == "(") sum += 1
        if (chars[i] == ")") sum -= 1
        if (sum == -1) {
            res = i
            break
        }
    }
}; 
END { print res }