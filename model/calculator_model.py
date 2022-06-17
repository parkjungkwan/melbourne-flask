import os
import sys
from icecream import ic
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir
import tensorflow.compat.v1 as tf

class CalculatorModel:
    def __init__(self) -> None:
        self.model = os.path.join(basedir, 'model')
        self.data = os.path.join(self.model, 'data')

    def create_add_model(self):
        pass

    def create_sub_model(self):
        pass

    def create_mul_model(self):
        pass

    def create_div_model(self):
        pass

if __name__=='__main__':
    ic(basedir)
    tf.disable_v2_behavior()
    ic(tf.__version__)
    hello = tf.constant("Hello")
    session = tf.Session()
    ic(session.run(hello))