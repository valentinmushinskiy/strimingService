x = 0:0.1:10;
y = trimf(x,[2 5 7]);
plot(x,y)
xlabel('trimf, P = [2 5 7]')
ylim([-0.05 1.05])
