x = 0:0.1:10;
y = trapmf(x,[2 5 6 8]);
plot(x,y)
xlabel('trapmf, P = [2 5 6 8]')
ylim([-0.05 1.05])
