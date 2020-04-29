function state = gaplotchange(options, state, flag)
% функція gaplotchange виводить графік в логарифмічному масштабі,
% зміна кращої оцінки в порівнянні з попереднім поколінням.
%
persistent last_best % краща оцінка в попереднім поколінні
if(strcmp(flag,'finit')) % Установка графіка
set(gca,'xlimf',[1, options.Generations],'Yscale','Vlogf');
hold on;
xlabel Generation
title('Change in Best Fitness Value')
end
best = min(state.Score); % краща оцінка в поточному поколінні
if (state.Generation == 0) % Set lastbest to best.
last_best = best;
else
change = last_best - best; % изменение лучшей оценки
last_best = best;
plot(state.Generation, change, '.r');
title(['Change in Best Fitness Value'])
end
