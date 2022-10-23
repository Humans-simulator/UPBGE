import bge, bpy, mathutils, math

#controller = bge.logic.getCurrentController()
#print("Controller: ",controller)
#armature = controller.owner
#print("Owner: ",armature)

#channel = armature.channels[6] #LowerBack

#print("Channel: ",channel)
#print(armature.channels)

#print(channel.rotation_euler)
#print("Channel rotation mode: ",channel.rotation_mode)

#rot = channel.rotation_euler
#add = 1
#channel.rotation_euler = (rot[0]+add, rot[1], rot[2])
#armature.update()
#print(channel.rotation_euler)


myrigbones = bpy.data.objects['Ted'].pose.bones
print("BPY: ", myrigbones)
print(myrigbones['LowerBack'].rotation_euler)

rot = myrigbones['LowerBack'].rotation_euler
add = 1

#myrigbones['LowerBack'].rotation_euler = Euler((5.0, 0.0, 0.0), 'XYZ')
myrigbones['LowerBack'].rotation_euler = (rot[0]+add, rot[1], rot[2])
