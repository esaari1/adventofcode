import bpy
import numpy as np
import colorsys

fnum = 1
fstep = 2

def createPlane():
    bpy.ops.mesh.primitive_plane_add(size=20, location=(4.5, 4.5, 0))
    ob = context.object
    bpy.ops.object.material_slot_add()

    mat_name = "plane"
    mat = bpy.data.materials.new(mat_name)
    mat.use_nodes = True

    mat.node_tree.nodes[0].inputs["Metallic"].default_value = 1.0
    mat.node_tree.nodes[0].inputs["Roughness"].default_value = 0.1

    ob.material_slots[0].material = mat


def createLight(x, y, e):
    # create light datablock, set attributes
    light_data = bpy.data.lights.new(name=f"light_{x}_{y}", type='POINT')

    light_data.color = colorsys.hsv_to_rgb(0.611, 0.427, 1)
    light_data.energy = 3**e
    light_data.keyframe_insert(data_path='energy', frame=1)

    # create new object with our light datablock
    light_object = bpy.data.objects.new(name=f"light_{x}_{y}", object_data=light_data)

    # link light object
    bpy.context.collection.objects.link(light_object)

    #change location
    light_object.location = (x, y, 0)


def updateLight(x, y, e):
    if e < 11:
        name = f'light_{x}_{y}'
        bpy.data.lights[name].energy = 3**e
        bpy.data.lights[name].keyframe_insert(data_path='energy', frame=fnum)

def updateLights():
    for x in range(10):
        for y in range(10):
            updateLight(x, 9-y, arr[y, x])

arr = np.array([
(2,3,4,4,6,7,1,2,1,2),
(6,6,1,1,7,4,2,6,8,1),
(5,5,7,5,5,7,5,5,7,3),
(3,1,6,7,8,4,8,5,3,6),
(1,3,5,3,8,2,7,3,1,1),
(4,4,1,6,4,6,3,2,6,6),
(2,6,2,4,7,6,1,6,1,5),
(1,7,8,6,5,6,1,2,6,3),
(3,6,2,2,6,4,3,2,1,5),
(4,1,4,3,2,8,4,6,5,3)])

context = bpy.context

createPlane()

for x in range(10):
    for y in range(10):
        createLight(x, 9-y, arr[y, x])


total = 0

#for step in range(100):
step = 0
fnum = 1
while True:
    print(step)
    currentTotal = 0
    arr += 1

    fnum += fstep
    updateLights()

    flashes = np.where(arr == 10)
    while len(flashes[0]) > 0:
        total += len(flashes[0])
        currentTotal += len(flashes[0])

        newrows = []
        newcols = []

        for idx in range(len(flashes[0])):
            r = flashes[0][idx]
            c = flashes[1][idx]

            r1 = max(0, r - 1)
            r2 = min(10, r + 2)
            c1 = max(0, c - 1)
            c2 = min(10, c + 2)

            arr[r1:r2, c1:c2] += 1
            newflashe = np.where(arr[r1:r2, c1:c2] == 10)

            newrows.extend(newflashe[0] + max(0, r - 1))
            newcols.extend(newflashe[1] + max(0, c - 1))

        flashes = [newrows, newcols]

    fnum += fstep
    updateLights()

    arr[arr > 9] = 0

    if currentTotal == 100:
        break

    step += 1
