import tensorflow as tf

from utils.config import get_args
from utils.config import get_config_from_json
from utils.utils import judge_and_new
import os



if __name__ == '__main__':
    # tf.app.run()

    ''' Dynamic configs '''
    try:
        args = get_args()
        config = get_config_from_json(args.config)
    except:
        raise Exception("missing or invalid arguments")

    ''' Static configs '''
    os.environ["CUDA_VISIBLE_DEVICES"] = "0, 2"
    judge_and_new(os.path.join(config.work_root, config.project_name))
    config.ckpt_path = os.path.join(config.work_root, config.project_name, 'save')
    judge_and_new(os.path.join(config.work_root, config.project_name, 'save'))
    # config.timeline_path = os.path.join(config.work_root, config.project_name, 'timelines')
    # judge_clean_new(os.path.join(config.work_root, config.project_name, 'timelines'))
    config.tensorb_path = os.path.join(config.work_root, config.project_name, 'tensorb')
    judge_and_new(os.path.join(config.work_root, config.project_name, 'tensorb'))


    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.85, allow_growth=True)
    # gpu_options = tf.GPUOptions(allow_growth=True)
    tf_config = tf.ConfigProto(gpu_options=gpu_options, allow_soft_placement=True)
                               # , log_device_placement=True)

    with tf.Graph().as_default(), tf.Session(config=tf_config) as sess:
        train(sess, config, restore_from_save=True, save_model=True, write_log=True)