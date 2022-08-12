from pyroll.core import CircularOvalGroove, RoundGroove, Roll, Profile, RollPass, Transport, SwedishOvalGroove
from pyroll.freiberg_flow_stress import FreibergFlowStressCoefficients
from pyroll.work_roll_bending.roll_body import RollBody

# initial profile
in_profile = Profile.round(
    radius=24e-3,
    temperature=1200 + 273.15,
    strain=0,
    material="BST 500",
    freiberg_flow_stress_coefficients=FreibergFlowStressCoefficients(
        a=4877.12 * 1e6,
        m1=-0.00273339,
        m2=0.302309,
        m3=-0.0407581,
        m4=0.000222222,
        m5=-0.000383134,
        m6=0,
        m7=-0.492672,
        m8=0.0000175044,
        m9=-0.0611783,
        baseStrain=0.1,
        baseStrainRate=0.1
    ),
    density=7.5e3,
    thermal_capacity=690,
)

# pass sequence
sequence = [
    RollPass(
        label="K 02/001 - 1",
        roll=Roll(
            groove=SwedishOvalGroove(
                r1=6e-3,
                r2=26e-3,
                ground_width=38e-3,
                usable_width=60e-3,
                depth=7.25e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=53e-3
            )
        ),
        velocity=4.5,
        gap=13.5e-3,
    ),
    Transport(
        duration=6.4
    ),
    RollPass(
        label="K 05/001 - 2",
        roll=Roll(
            groove=RoundGroove(
                r1=4e-3,
                r2=18e-3,
                depth=17.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=129e-3
            ),
        ),
        velocity=4.75,
        gap=1.5e-3,
    ),
    Transport(
        duration=3.6
    ),
    RollPass(
        label="K 02/001 - 3",
        roll=Roll(
            groove=SwedishOvalGroove(
                r1=6e-3,
                r2=26e-3,
                ground_width=38e-3,
                usable_width=60e-3,
                depth=7.25e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=53e-3
            ),
        ),
        velocity=9.1,
        gap=1.5e-3,
    ),
    Transport(
        duration=3.4
    ),
    RollPass(
        label="K 05/002 - 4",
        roll=Roll(
            groove=RoundGroove(
                r1=4e-3,
                r2=13.5e-3,
                depth=12.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=200e-3
            ),
        ),
        velocity=9.3,
        gap=1e-3,
    ),
    Transport(
        duration=5.2
    ),
    RollPass(
        label="K 03/001 - 5",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=6e-3,
                r2=38e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=262e-3
            ),
        ),
        velocity=9.1,
        gap=6e-3,
    ),
    Transport(
        duration=4.4
    ),
    RollPass(
        label="K 05/003 - 6",
        roll=Roll(
            groove=RoundGroove(
                r1=3e-3,
                r2=10e-3,
                depth=9e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=318e-3
            ),
        ),
        velocity=9.3,
        gap=2e-3,
    ),
    Transport(
        duration=3.8
    ),
    RollPass(
        label="K 03/001 - 7",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=6e-3,
                r2=38e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=262e-3
            ),
        ),
        velocity=9.1,
        gap=1e-3,
    ),
    Transport(
        duration=7.2
    ),
    RollPass(
        label="K 05/004 - 8",
        roll=Roll(
            groove=RoundGroove(
                r1=2e-3,
                r2=7.5e-3,
                depth=5.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=377e-3
            ),
        ),
        velocity=9.3,
        gap=4.2e-3,
    ),
    Transport(
        duration=6.2
    ),
    RollPass(
        label="K 03/002 - 9",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=6e-3,
                r2=21.2e-3,
                depth=2.5e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=431e-3
            ),
        ),
        velocity=9.1,
        gap=4.2e-3,
    ),
    Transport(
        duration=4.5
    ), RollPass(
        label="K 05/005 - 10",
        roll=Roll(
            groove=RoundGroove(
                r1=0.5e-3,
                r2=6e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=200e-3,
                joint_length=262.2e-3,
                path_to_body="cad/IMF_reversing_mill_work_roll.dxf",
                distance_to_groove=485e-3
            ),
        ),
        velocity=9.3,
        gap=4.6e-3,
    ), Transport(
        duration=9
    ),
    RollPass(
        label="F1 - K 3/50",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=2.5e-3,
                r2=12.5e-3,
                depth=2.9e-3
            ),
            nominal_radius=107.5e-3,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=120e-3,
                joint_length=55e-3,
                path_to_body="cad/IMF_F1-K3_50.dxf",
                distance_to_groove=22e-3
            ),
        ),
        velocity=2.25,
        gap=2e-3,
    ),
    Transport(
        duration=0.5
    ),
    RollPass(
        label="F2 - K9/24",
        roll=Roll(
            groove=RoundGroove(
                r1=0.5e-3,
                r2=5.1e-3,
                depth=4.25e-3
            ),
            nominal_radius=107.5e-3,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=120e-3,
                joint_length=55e-3,
                path_to_body="cad/IMF_F2-K9_24.dxf",
                distance_to_groove=22e-3
            ),
        ),
        velocity=2.8,
        gap=1.4e-3,
    ), Transport(
        duration=0.5
    ),
    RollPass(
        label="F3 - K3/51",
        roll=Roll(
            groove=CircularOvalGroove(
                r1=2.5e-3,
                r2=11e-3,
                depth=2.12e-3
            ),
            nominal_radius=107.5e-3,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=120e-3,
                joint_length=55e-3,
                path_to_body="cad/IMF_F3-K3_51.dxf",
                distance_to_groove=22e-3
            ),
        ),
        velocity=3.75,
        gap=2.1e-3,
    ), Transport(
        duration=0.25
    ),
    RollPass(
        label="F4 - K9/23",
        roll=Roll(
            groove=RoundGroove(
                r1=0.5e-3,
                r2=4.08e-3,
                depth=3.25e-3
            ),
            nominal_radius=85e-3,
            youngs_modulus=210e9,
            body=RollBody(
                joint_diameter=92e-3,
                joint_length=55e-3,
                path_to_body="cad/IMF_F4-K9_23.dxf",
                distance_to_groove=18e-3
            ),
        ),
        velocity=4.4,
        gap=1.4e-3,
    ),
]
