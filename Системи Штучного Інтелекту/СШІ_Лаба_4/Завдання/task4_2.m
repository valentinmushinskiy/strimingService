net = selforgmap(11);

net.trainParam.epochs = 9;
net = train(net,X);

plotsompos(net)

x = [1;4];
a = net(x);
disp('a = ');
disp(a)