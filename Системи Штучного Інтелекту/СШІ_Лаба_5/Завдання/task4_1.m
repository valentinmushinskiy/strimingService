P = [2 3 4 5 6 7 8 9 10];
T = [1 2 4 2 0 2 3 4 5];
spread = 0.7;
net = newgrnn (P, T, spread);
net.layers {1} .size% Число нейронів в прихованому шарі
A = sim (net, P);
plot (P, T, '* k', 'markersize', 10)
hold on,
plot (P, A, 'ok', 'markersize', 10);
