food = 0:.5:10;
[F,S] = meshgrid(food,service);
tip = (0.20/20).*(S+F)+0.05;
surf(S,F,tip)
xlabel('Service')
ylabel('Food')
zlabel('Tip')
