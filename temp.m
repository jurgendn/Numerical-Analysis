function xx = Noisuynguoc_PP2 (x , y , yy , esp , max)
n = length(x);
if length(y) = n
    error("Do dai cua x va y phai bang nhau")
end

c = [ ] ;
xxtemp = [ ] ;

for i = 1 : n
    if yy==y (i)
        xxtemp=[xxtemp x (i) ] ;
    end
end

for i = 1 : n-1
    if ((yy-y (i)) *(yy-y (i +1)) <0)
        c = [ c , i ] ;
        c = [ c , i +1];
    end
end

b = zeros(n) ;
b (: , 1) = y (:) ;

for j = 2 : n
    for i = 1 : n-j+1
        b(i , j) = (b(i +1,j -1) - b(i , j -1)) / (x (i+j -1) - x (i)) ;
    end
end

m = length(c) / 2;
xx = zeros(1 ,m) ;
s = 1 ;

for j = 1 : 2 :m
    if (c (j) <((n+1) /2))
        dd = b(c (j) , 2) ;
        t = x (c (j)) + (yy-y (c (j))) /dd ;
        t t = (t-x (c (j))) /dd ;
        t0 = x (c (j)) + (yy-y (c (j))) /dd ;

        for k = 3 : n+1-c (j)
            t t = t t *(t-x (c (j)+k-2)) ;
            t0 = t0 - b(c (j) , k) * t t ;
        end
        r = 2 ;

        while((abs(t-t0)>esp)&&(r<max))
            t = t0 ;
            t t = (t-x (c (j))) /dd ;
            t0 = x (c (j)) + (yy-y (c (j))) /dd ;
            for k = 3 : n+1-c (j)
                t t = t t *(t-x (c (j)+k-2)) ;
                t0 = t0 - b(c (j) , k) * t t ;
            end
            r = r +1;
        end
        xx (s) = t0 ;
        s = s +1;
    end
end

x1 = flipr(x) ;
y1 = flipr(y) ;
c1 = zeros(1 ,2*m) ;
for i = 1:2*m
c1 (i) = n+1 - c (2*m+1-i);
end