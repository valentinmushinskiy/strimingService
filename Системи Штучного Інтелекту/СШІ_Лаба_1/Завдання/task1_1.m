x = 0:0.1:10;
y = trapmf(x,[1 5 7 8]);
plot(x,y)
xlabel('trapmf, P = [1 5 7 8]')
ylim([-0.05 1.05])
