function newcos = New_cos(x)

%newcos = sqrt(1-(New_sin(x))^2);
double sum;
double a;
double b; %//sum代表和，a为分子，b为分母
double p;
char s ;
s=1; 
sum=0;
a=1;     %//分母赋初值
b=1;     %//分子赋初值
p=1;
 while abs(a/b) >= 1e-10
 %while a/b >= 1e-6
  sum = sum+s*(a/b);    %//累加一项
  a = a*x*x;     %//求下一项分子
  b = b*2*p*(2*p-1);   %//求下一项分母
  s = s*(-1);
  p = p+1;
 end
 newcos = sum;