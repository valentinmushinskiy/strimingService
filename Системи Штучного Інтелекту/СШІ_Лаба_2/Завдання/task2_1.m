mam_fismat = readfis ('mam22.fis');
sug_fismat = mam2sug(mam_fismat);
subplot(2,2,1)
gensurf(mam_fismat,[1 2],1)
title('Mamdani system (Output 1)')
subplot(2,2,2)
gensurf(sug_fismat,[1 2],1)
title('Sugeno system (Output 1)')
subplot(2,2,3)
gensurf(mam_fismat,[1 2],2)
title('Mamdani system (Output 2)')
subplot(2,2,4)
gensurf(sug_fismat,[1 2],2)
title('Sugeno system (Output 2)')
