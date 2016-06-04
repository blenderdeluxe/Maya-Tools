import maya.cmds as cmds

selected = cmds.ls(selection=True)


tx = cmds.getAttr("%s.translateX" % selected[0])
ty = cmds.getAttr("%s.translateY" % selected[0])
tz = cmds.getAttr("%s.translateZ" % selected[0])

cmds.setAttr( "%s.translateX" % selected[1], tx )
cmds.setAttr( "%s.translateY" % selected[1], ty )
cmds.setAttr( "%s.translateZ" % selected[1], tz )
# do something with the value. egs:
print tx
print ty
print tz
