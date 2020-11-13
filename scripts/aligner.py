import maya.cmds as mc

#Make window

objAligner = mc.window(title="Object Alignment Tool", s=False, wh=(300, 100))
mc.columnLayout(adj=True)
mc.text(l="Instructions: select source, then target")
mc.button(l="Align", w=200, 50, c="aligner()")
mc.showWindow(objAligner)

#Aligner func

def aligner():
    prtConstr = mc.parentConstraint()
    mc.delete(prtConstr)