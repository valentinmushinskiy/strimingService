service = 0:.5:10;
tip = 0.15*ones(size(service));
plot(service,tip)
xlabel('Service')
ylabel('Tip')
ylim([0.05 0.25])
