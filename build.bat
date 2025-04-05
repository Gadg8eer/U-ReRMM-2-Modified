@ECHO OFF
@RD /S /Q ".\.nmlcache"
@RD /S /Q ".\backups"
@DEL /S /Q "UReRMM2.grf"
:start
nmlc --grf UReRMM2.grf UReRMM2.nml
PAUSE