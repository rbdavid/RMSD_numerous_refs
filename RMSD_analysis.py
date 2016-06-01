#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
##!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# ----------------------------------------
# USAGE:


# ----------------------------------------
# PREAMBLE:

import MDAnalysis
from MDAnalysis.analysis.align import *
import sys
import os
import sel_list
from distance_functions import *

# ----------------------------------------
# VARIABLE DECLARATION

ref_loc = sys.argv[1]
traj_loc = sys.argv[2]
number = int(sys.argv[3])		# Corresponds to which system you want to compare against...

flush = sys.stdout.flush
makedir = os.mkdir
changedir = os.chdir

alignment = 'name CA and (resid 19:25 or resid 50:55 or resid 90:94 or resid 112:117 or resid 142:149 or resid 165:169 or resid 190:194 or resid 214:218 or resid 236:240 or resid 253:258 or resid 303:307)'
important = 'protein or nucleic or resname A5 or resname A3 or resname U5 or resname atp or resname adp or resname PHX or resname MG'

ref_list = []
ref_list.append(['AMBER_apo', 21, 100])	
ref_list.append(['AMBER_atp', 21, 100])		
ref_list.append(['AMBER_ssrna', 21, 100])		
ref_list.append(['AMBER_ssrna_atp', 21, 100])	
ref_list.append(['AMBER_ssrna_adp_pi', 21, 100])	
ref_list.append(['AMBER_ssrna_adp', 21, 100])	
ref_list.append(['AMBER_ssrna_pi', 21, 100])		

nSys = len(ref_list)
nSel = len(sel_list.sel)

# ----------------------------------------
# SUBROUTINES:

def ffprint(string):
        print '%s' %(string)
        flush()

# ----------------------------------------
# MAIN PROGRAM:

makedir('%s_comparison' %(ref_list[number][0]))
changedir('%s_comparison' %(ref_list[number][0]))
out1 = open('%s.output' %(ref_list[number][0]),'w',1) 
ref_file = '%s%s/truncated.pdb' %(ref_loc,ref_list[number][0])
out1.write('Reference structure: %s\n' %(ref_file))

ref = MDAnalysis.Universe(ref_file)
ref_all = ref.select_atoms('all')
ref_backbone = ref.select_atoms('backbone')
ref_align = ref.select_atoms(alignment)
ref_all.translate(-ref_backbone.center_of_mass())

pos0 = ref_align.coordinates()

# SAVE COORDINATES FOR ALL SELECTIONS...
pos_list = []
for i in range(nSel):
	selection = sel_list.sel[i][1]
	temp_sel = ref.select_atoms(selection)
	temp_pos = temp_sel.coordinates()
	pos_list.append(temp_pos)

out1.write('Finished collecting the reference structure data\n')

out2 = open('%s.rmsd.dat' %(ref_list[number][0]),'w')
# INITIALIZING UNIVERSES, LOADING TRAJECTORIES IN, ANALYZING, ETC...
for i in range(nSys):
	out1.write('Loading in Trajectories from %s\n' %(ref_list[i][0]))
	u = MDAnalysis.Universe('%s%s/truncated.pdb' %(traj_loc,ref_list[i][0]))
	
	u_all = u.select_atoms('all')
	u_backbone = u.select_atoms('backbone')
	u_align = u.select_atoms(alignment)
	u_important = u.select_atoms(important)

	traj_list = []
	a = ref_list[i][1]
	while a <= ref_list[i][2]:
		traj_list.append('%s%s/Truncated/production.%s/production.%s.dcd' %(traj_loc,ref_list[i][0],a,a))  
		a += 1

	u_selection_list = []
	for b in range(nSel):
		selection = sel_list.sel[b][1]
		temp_sel = u.select_atoms(selection)
		temp_nAtoms = len(temp_sel.atoms)
		u_selection_list.append([temp_sel,temp_nAtoms])
		out1.write('%s corresponds to %s atom selection w/ %d number of atoms\n' %(sel_list.sel[b][0],u_selection_list[b][0],u_selection_list[b][1]))

	count = 0
	out1.write('Beginning trajectory analysis from system %s\n' %(ref_list[i][0]))
	for j in range(len(traj_list)):
		u.load_new(traj_list[j])
		nSteps = len(u.trajectory)
		for ts in u.trajectory:
			u_important.translate(-u_backbone.center_of_mass())
			R, rmsd = rotation_matrix(u_align.coordinates(),pos0)
			u_important.rotate(R)
			for m in range(nSel):
				temp_pos = u_selection_list[m][0].coordinates()
				rmsd = RMSD(temp_pos,pos_list[m],u_selection_list[m][1])
				out2.write('%f   ' %(rmsd))
			out2.write('\n')

			if ts.frame%2500 ==0:
				out1.write('Analyzed %d in Trajectory %s\n' %(ts.frame,traj_list[j]))
			count +=1
	out1.write('Analyzed %d frames from system %s\n' %(count,ref_list[i][0]))

out1.close()
out2.close()
changedir('..')

