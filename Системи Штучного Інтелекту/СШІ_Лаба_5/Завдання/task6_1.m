p1 = sin (1:20);
p2 = sin (1:20) * 2;

t1 = ones(1,20);
t2 = ones(1,20)*2;

p = [p1 p2 p1 p2];
t = [t1 t2 t1 t2];

Pseq = con2seq(p);
Tseq = con2seq(t);

R = 1; % Число елементів входу
S2 = 1;% Число нейронів вихідного шару
S1 = 10; % Число нейронів рекурентного шару

net = newelm([-2 2],[S1 S2],{'tansig','purelin'},'traingdx');
net.trainParam.epochs = 1000;
net.trainParam.show = 25;
net.trainParam.goal = 0.01;
[net,tr] = train(net,Pseq,Tseq);

figure(2)
a = sim(net,Pseq);
time = 1:length(p);
plot(time, t, '-', time, cat(2,a{:}))
axis([1 80 0.8 2.2]) % Рис.5.19

p3 = sin(1:20)*1.3;
t3 = ones(1,20)*1.3;
p4 = sin(1:20)*1.1;
t4 = ones(1,20)*1.1;
pg = [p3 p4 p3 p4];
tg = [t3 t4 t3 t4];
pgseq = con2seq(pg);
figure(3)
a = sim(net,pgseq);
ime = 1:length(pg);
plot(time, tg, '-', time, cat(2,a{:}))
axis([1 80 0.8 2.2]) 



