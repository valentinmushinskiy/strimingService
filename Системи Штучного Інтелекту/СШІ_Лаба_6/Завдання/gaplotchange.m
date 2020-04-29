function state = gaplotchange(options, state, flag)
% ������� gaplotchange �������� ������ � ������������� �������,
% ���� ����� ������ � �������� � ��������� ���������.
%
persistent last_best % ����� ������ � ��������� �������
if(strcmp(flag,'finit')) % ��������� �������
set(gca,'xlimf',[1, options.Generations],'Yscale','Vlogf');
hold on;
xlabel Generation
title('Change in Best Fitness Value')
end
best = min(state.Score); % ����� ������ � ��������� �������
if (state.Generation == 0) % Set lastbest to best.
last_best = best;
else
change = last_best - best; % ��������� ������ ������
last_best = best;
plot(state.Generation, change, '.r');
title(['Change in Best Fitness Value'])
end
