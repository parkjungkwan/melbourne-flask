import tensorflow.compat.v1 as tf
from icecream import ic
import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir


class Cabbage:
    def __init__(self) -> None:
        self.model = os.path.join(basedir, 'model')
        self.df = None

    def hook(self):
        self.preprocessing()
        #self.create_model()


    def preprocessing(self):
        path='model/data/price_data.csv'
        self.df = pd.read_csv(path, encoding='UTF-8', thousands=',')
        ic(self.df)

    def create_model(self): # 모델생성
        sess = tf.Session()
        _ = tf.Variable(initial_value = 'fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.save(sess, os.path.join(self.model, 'cabbage', 'model'), global_step=1000)
        
if __name__=='__main__':
    tf.disable_v2_behavior()
    Cabbage().hook()

