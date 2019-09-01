import tensorflow as tf

def restore_from_checkpoint(sess, saver, dir):
    ckpt = tf.train.get_checkpoint_state(dir)
    if not ckpt or not ckpt.model_checkpoint_path:
        print('No checkpoint found at {}'.format(dir))
        return False
    saver.restore(sess, ckpt.model_checkpoint_path)
    return True