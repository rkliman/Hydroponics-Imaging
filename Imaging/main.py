# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import skeletor as sk
import trimesh


def main():
    # import mesh
    mesh = trimesh.load('files/tree.stl', force='mesh')

    # pre-processing
    fixed = sk.pre.fix_mesh(mesh, remove_disconnected=5, inplace=False)
    cont = sk.pre.contract(fixed, 0.8)
    # fixed = sk.pre.simplify(fixed, 0.1)

    # skeletonize
    skel = sk.skeletonize.by_wavefront(cont, waves=1, step_size=1)

    # post processing
    skel = sk.post.clean_up(skel, validate=True)

    # display
    skel.show(mesh=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
