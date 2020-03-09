cd testSuite 
seq 1 8 | xargs -R2 -I __i__ zip -r milestone__i__.zip all mono multi milestone__i__.json
mv *.zip ../../../testSuites/
