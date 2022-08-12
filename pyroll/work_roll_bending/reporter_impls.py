import numpy as np
from matplotlib import pyplot as plt
from pyroll.core import RollPass
from pyroll.ui import Reporter
from pyroll.utils import for_units
from shapely.geometry import Point


def plot_neutral_line_deflection(ax: plt.Axes, roll_pass: RollPass):
    contour = roll_pass.roll.body.contour
    x_values = [disk.center for disk in roll_pass.roll.disk_elements]
    y_lim = ax.get_ylim()[1]
    whitespace_factor = (y_lim / roll_pass.roll.body.contour.bounds[3])

    ax.yaxis.set_visible(False)
    ax.plot(*contour.exterior.xy, color='black', alpha=0.75)
    ax.scatter(*Point(roll_pass.roll.body.distance_to_groove, -contour.bounds[3] * 0.05).xy, color="C1")

    ax2 = ax.twinx()
    ax2.yaxis.tick_left()
    ax2.set_ylim((-np.max(roll_pass.roll.deflection) * whitespace_factor) * 2, (np.max(roll_pass.roll.deflection) * whitespace_factor) * 2)
    ax2.axhline(y=0, ls="--", alpha=0.5)
    ax2.plot(x_values, roll_pass.roll.deflection[0:-1])


@Reporter.hookimpl
@for_units(RollPass)
def unit_properties(unit: RollPass):
    return dict(
        work_roll_elastic_modulus=f"{unit.roll.youngs_modulus}",
        work_roll_max_deflection=f"{np.max(unit.roll.deflection)}"
    )


@Reporter.hookimpl
@for_units(RollPass)
def unit_plot(unit: RollPass):
    """Plot roll pass contour and its profiles"""
    fig: plt.Figure = plt.figure(constrained_layout=True, figsize=(4, 4.5))
    ax: plt.Axes = fig.subplots()

    ax.set_aspect("equal", "datalim")
    ax.grid(lw=0.5)
    plt.title("Work roll deflection")
    plot_neutral_line_deflection(ax, unit)

    return fig
