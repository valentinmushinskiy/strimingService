%Побудова графіка функції y=(x1^2-8)*cos(x2) 
%в області x1є[0,4] и x2є[0,4]. 
n=15; 
x1=0:4/(n-1):4; 
x2=0:4/(n-1):4; 
y=zeros(n,n); 
for j=1:n 
y(j,:)=(x1.^2-8)*cos(x2(j)); 
end 
surf(x1,x2,y) 
xlabel('x1') 
ylabel('x2') 
zlabel('y') 
title('Target');
