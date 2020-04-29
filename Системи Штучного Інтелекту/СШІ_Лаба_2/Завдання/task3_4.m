servRatio = 0.8;
tip = servRatio*(0.20/10*S+0.05) + ...
    (1-servRatio)*(0.20/10*F+0.05);
surf(S,F,tip)
xlabel('Service')
ylabel('Food')
zlabel('Tip')
