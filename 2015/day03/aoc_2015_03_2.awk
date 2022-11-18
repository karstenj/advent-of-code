BEGIN {  }
{ 
    split($0, a, "")
    x1 = 1; y1 = 1; x2=1; y2=1
    h[1,1] = 1
    sum = 1
    for (i=1; i <= length($0); i ++) {
        if (a[i] == "^") y1 += 1
        if (a[i] == "v") y1 -= 1
        if (a[i] == "<") x1 -= 1
        if (a[i] == ">") x1 += 1
        if (h[x1,y1] == 0) {
            h[x1,y1] = 1
            sum += 1
        }
        y = y1
        x = x1
        y1 = y2
        x1 = x2
        y2 = y
        x2 = x
    }
};
END { print sum }