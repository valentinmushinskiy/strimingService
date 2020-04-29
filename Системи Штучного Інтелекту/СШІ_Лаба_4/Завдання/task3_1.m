bounds = [0 2; 0 2];
clusters = 7;
points = 9;
std_dev = 0.09;
x = nngenc(bounds,clusters,points,std_dev);

plot(x(1,:),x(2,:),'+r');
title('Input Vectors');
xlabel('x(1)');
ylabel('x(2)');

net = competlayer(15,.1);
net = configure(net,x);
w = net.IW{1};
plot(x(1,:),x(2,:),'+r');
hold on;
circles = plot(w(:,1),w(:,2),'ob');

net.trainParam.epochs = 7;
net = train(net,x);
w = net.IW{1};
delete(circles);
plot(w(:,1),w(:,2),'ob');

x1 = [0; 0.2];
y = net(x1);
disp('x1 = [0; 0.2]')
disp('y = ')
disp(y)

