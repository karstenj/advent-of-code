BEGIN {  }
{ 
    split($0, a, "")
    for (i=1; i <= length($0); i++) {
        if (a[i] == "^") y += 1
        if (a[i] == "v") y -= 1
        if (a[i] == "<") x -= 1
        if (a[i] == ">") x += 1
        if (h[x,y] == 0) {
            h[x,y] = 1
            sum += 1
        }
    }
};
END { print sum }