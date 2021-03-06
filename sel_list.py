#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
##!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

sel = []
sel.append(['betas','protein and (resid 19:25 or resid 50:55 or resid 90:94 or resid 112:117 or resid 142:149 or resid 165:169 or resid 190:194 or resid 214:218 or resid 236:240 or resid 253:258 or resid 303:307)'])
sel.append(['not_betas','protein and not (resid 0:12 or resid 19:25 or resid 50:55 or resid 90:94 or resid 112:117 or resid 142:149 or resid 165:169 or resid 190:194 or resid 214:218 or resid 236:240 or resid 253:258 or resid 303:307 or resid 46 or resid 155 or resid 313 or resid 359)'])
sel.append(['all_residues-12','protein and not (resid 0:12 or resid 46 or resid 155 or resid 313 or resid 359)'])
sel.append(['atp_bp','protein and (resid 27:35 or resid 60 or resid 63:64 or resid 117:118 or resid 147 or resid 149 or resid 159 or resid 245:249 or resid 288:289 or resid 292:293 or resid 296)'])
sel.append(['rna_bc','protein and (resid 55:61 or resid 74:84 or resid 93:106 or resid 121:126 or resid 195:200 or resid 218:224 or resid 240:246 or resid 260:264 or resid 276 or resid 282 or resid 319:323 or resid 367:368 or resid 370:377 or resid 431:440 or resid 442 or resid 451)'])
sel.append(['hel_gate','protein and (resid 195:211 or resid 429:448)'])
sel.append(['motif_1','protein and resid 24:35'])
sel.append(['motif_1a','protein and resid 51:63'])
sel.append(['motif_1b','protein and resid 92:100'])
sel.append(['motif_1c','protein and resid 72:90'])
sel.append(['A2_1c','protein and (resid 56:69 or resid 72:90)'])
sel.append(['motif_2','protein and resid 117:124'])
sel.append(['motif_3','protein and resid 148:154'])
sel.append(['motif_4','protein and resid 195:211'])
sel.append(['motif_4a','protein and resid 217:230'])
sel.append(['motif_5','protein and resid 237:246'])
sel.append(['motif_6','protein and resid 288:300'])

sel.append(['A2','protein and resid 56:69'])
sel.append(['L_beta4_5','protein and resid 240:253'])

#sel.append([ , ])

