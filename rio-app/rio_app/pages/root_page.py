from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class RootPage(rio.Component):
    def build(self) -> rio.Component:
        return rio.Row(
            comps.Sidebar(),
            rio.Column(
                comps.Navbar(),
                rio.PageView(),
                proportions=(0.7, 9.3),
            ),
            proportions=(1.5,8.5)
        )
