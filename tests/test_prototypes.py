import numpy as np
from sefi_voxel.grid import VoxelGrid
from sefi_voxel.render import render_ascii_projection
from sefi_voxel.phase_compiler import compile_phase_pattern


def test_phase_cancels_plane_wave_phase():
    rng=np.random.default_rng(42)
    r=rng.normal(size=(20,3));k=rng.normal(size=(8,3))
    phase=compile_phase_pattern(r,k)
    assert phase.shape==(20,8)
    assert np.all((phase>=0)&(phase<2*np.pi))
    assert np.allclose(np.exp(1j*(r@k.T+phase)),1,atol=1e-13)


def test_weight_conservation_and_boundary_clipping():
    g=VoxelGrid(bounds=(-1,1),resolution=5)
    g.add_trajectory(np.array([[-10,-10,-10,42],[10,10,10,99],[0,0,0,0]]),weight=2)
    assert g.grid.sum()==6
    assert g.grid[0,0,0]==2 and g.grid[-1,-1,-1]==2


def test_empty_and_nonempty_projection():
    g=np.zeros((3,4,2))
    assert render_ascii_projection(g)=='    \n    \n    '
    g[1,2,:]=1
    assert render_ascii_projection(g).splitlines()[1][2]=='@'
