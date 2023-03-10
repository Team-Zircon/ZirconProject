"""
Configs for the training script. Uses the ml_collections config library.
"""
from ml_collections import ConfigDict
from go_to_target import GoToTarget
import velocity_control, velocity_control_double


def get_config(task_string):
    tasks = {
        'go_to_target': ConfigDict({
            'constructor': GoToTarget,
            'config': ConfigDict(dict(
                moving_target=True
            ))
        }),
        'velocity_control': ConfigDict({
            'constructor': velocity_control.VelocityControl,
            'config': ConfigDict(dict(
                max_speed=4.5,
                reward_margin=0.75,
                direction_exponent=1.,
                steps_before_changing_velocity=1
            ))
        }),
        'velocity_control_double': ConfigDict({
            'constructor': velocity_control_double.VelocityControl,
            'config': ConfigDict(dict(
                max_speed=4.5,
                reward_margin=0.75,
                direction_exponent=1.,
                steps_before_changing_velocity=1
            ))
        }),
    }

    return tasks[task_string]
