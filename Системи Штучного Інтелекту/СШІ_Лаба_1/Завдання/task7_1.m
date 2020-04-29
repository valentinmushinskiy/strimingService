x = 0:0.1:10;
mfparams = [2 4 6];
mftype = 'gbellmf';
y = evalmf(x,mfparams,mftype);
%
% Plot the evaluation.
plot(x,y)
xlabel('gbellmf, P = [2 4 6]')
ylim([-0.05 1.05])