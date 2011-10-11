import client_tcp

ref_ns = "ref"
bind_ns = "bind"
ctrl_ns = "ctrl"
joint_extension = ("02","03")
joint_attr = ("rotateY", "rotateY")
id_equiv = (2,3)


def set_ref_chain(dataObj):
    for id in dataObj:
        idIndex = id_equiv.index(id)
        mayaObj = ref_ns + "_" + joint_extension[ idIndex ] + "." + joint_attr[ idIndex ]

        mc.setAttr( mayaObj, dataObj[id]["ang"] )
	
	
def getJointRotations():
	jointVals = []
	for j in ["joint3.rotateY", "joint4.rotateY", "joint2.rotateY"]:
		val = client_tcp.client("getAttr " + j)
		if val:
			jointVals.append( float(val.split("\n")[0]) )
		
	return jointVals
		
		
def setJointRotations(dataObj):
	
	for j in dataObj:
		client_tcp.client("setAttr " + str(j) + " " + str(dataObj[j]), PORT = 6002)
		
		