# State Tab

The State tab shows a JSON-compatible description of the internal game state for debugging and understanding game mechanics in depth.

!!! warning "Optional"
    This tab uses the low-level [State representation](../advanced/state.md). The project can be solved **without** it; it is provided for optional, lower-level access only.

## Overview

The description includes public state fields and non-empty component stores. Private fields and empty component stores are omitted.
