# SEFI-Voxel

Voxel and phase-control research by Jason Duran Dutton, SEFI Research Program.

This repository brings together existing SEFI-PY prototypes and the original **Voxel Realization** design documents. It is a research starting point. The documents' physical proposals are author hypotheses; this repository does not demonstrate a working physical voxel device, material synthesis, or experimental validation.

## Included code

- `VoxelGrid`: accumulates weighted trajectory points in a three-dimensional NumPy array. Out-of-bounds coordinates are clipped to the edge. A fourth trajectory coordinate, if supplied, is ignored.
- `render_ascii_projection`: sums the grid along Z and renders a text image.
- `compile_phase_pattern`: computes `(-positions @ wave_vectors.T) mod (2*pi)`. This is a plane-wave phase relation, without propagation calibration, attenuation, or device geometry validation.
- `send_phase_sequence`: writes native-format float frames to a serial port. Framing, byte order, acknowledgement and timing must be agreed with a real device before use. No hardware test has been performed.

## Install and check

```sh
python -m pip install -e ".[test]"
python -m pytest
```

```python
from sefi_voxel.grid import VoxelGrid
from sefi_voxel.render import render_ascii_projection
import numpy as np

grid = VoxelGrid(resolution=12)
grid.add_trajectory(np.array([[0., 0., 0.], [1., 1., 1.]]))
print(render_ascii_projection(grid.grid))
```

## Design archive

`docs/Voxel Realization.tex`, the existing PDF, and figures are preserved from `V:/V Drive and GitHub Content/Microsoft/Real Voxel`. The PDF is an existing author artifact; it was not rebuilt or scientifically validated during repository setup. Generated LaTeX auxiliary files are omitted.

See `PROVENANCE.json` for source hashes. The four Python implementation files are imported unchanged; packaging, documentation and tests are new. The SEFI-PY Research License is retained in `LICENSE`; public availability does not grant unrestricted commercial use.

## Next experiments

1. Define a specific physical medium, device geometry and measurable target.
2. Add a conventional propagation model and calibration data.
3. Compare predicted and measured fields with matched power and controls.
4. Test any geometric proposal against the same reference and uncertainty budget.
