x1=2+rand(1,50);
y1=0+rand(1,50);
plot(x1,y1,'or');

x2=-2+rand(1,50);
y2=0+rand(1,50);
plot(x2,y2,'ob');

x3=0+rand(1,50);
y3=2+rand(1,50);
plot(x3,y3,'oy');

x4=0+rand(1,50);
y4=-2+rand(1,50);
plot(x4,y4,'og');

figure (1);
hold on;
plot(x1,y1,'or');
plot(x2,y2,'ob');
plot(x3,y3,'oy');
plot(x4,y4,'og');
grid on;
hold off;


T1(1:50)=1;
T2(1:50)=2;
T3(1:50)=3;
T4(1:50)=4;

T(1:50)=T1;
T(51:100)=T2;
T(101:150)=T3;
T(151:200)=T4;

x(1:50)=x1;
x(51:100)=x2;
x(101:150)=x3;
x(151:200)=x4;

y(1:50)=y1;
y(51:100)=y2;
y(101:150)=y3;
y(151:200)=y4;

z(1,1:200)=x;
z(2,1:200)=y;

size(T)
size(z)

net = newff(z,T,[10,2],{'logsig','logsig'});
net = train(net,z,T);
