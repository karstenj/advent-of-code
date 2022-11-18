BEGIN {  }
{ 
    split($0, chars, "")
    for (i=1; i <= length($0); i++) {
        printf("%s\n", chars[i])
    }
}; 
END { print sum }